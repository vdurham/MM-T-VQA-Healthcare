from .base_dataset import BaseDataset


class VQAEHRXQADataset(BaseDataset):
    def __init__(self, *args, split="", **kwargs):
        assert split in ["test"]
        self.split = split

        if split == "test":
            names = ["vqa_ehr_xqa_test"]

        super().__init__(
            *args,
            **kwargs,
            names=names,
            text_column_name="questions"
        )

    def __getitem__(self, index):
        image_tensor = self.get_image(index)["image"]
        text = self.get_text(index)["text"]

        index, question_index = self.index_mapper[index]
        qid = self.table["question_id"][index][question_index].as_py()

        answers = self.table["answers"][index][question_index].as_py()
        labels = self.table["answer_labels"][index][question_index].as_py()
        scores = self.table["answer_scores"][index][question_index].as_py()
        answer_types = self.table["answer_type"][index][question_index].as_py()

        return {
            "image": image_tensor,
            "text": text,
            "vqa_answer": answers,
            "vqa_labels": labels,
            "vqa_scores": scores,
            "answer_types": answer_types,
            "qid": qid,
        }
