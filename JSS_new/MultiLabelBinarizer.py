[
    {
        "description": "From /preprocessing/_label.py:MultiLabelBinarizer:fit, Exception: raise ValueError(     'The classes argument contains duplicate classes. Remove these duplicates before passing them to MultiLabelBinarizer.'     ) ",
        "anyOf": [
            {"type": "object", "properties": {"classes": {"enum": [None]}}},
            {"XXX TODO XXX": "len(set(self.classes)) >= len(self.classes)"},
        ],
    }
]
