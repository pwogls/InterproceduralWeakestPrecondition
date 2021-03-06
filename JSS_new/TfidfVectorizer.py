[
    {
        "description": "From /feature_extraction/text.py:_VectorizerMixin:_validate_params, Exception: raise ValueError(     'Invalid value for ngram_range=%s lower boundary larger than the upper boundary.'      % str(self.ngram_range)) ",
        "XXX TODO XXX": "self.ngram_range[0] <= self.ngram_range[1]",
    },
    {
        "description": "From /feature_extraction/text.py:_VectorizerMixin:_validate_vocabulary, Exception: raise ValueError(msg) ",
        "anyOf": [
            {"type": "object", "properties": {"vocabulary": {"enum": [None]}}},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {"XXX TODO XXX": "isinstance(self.vocabulary, set)"},
                            {
                                "XXX TODO XXX": "isinstance(sorted(self.vocabulary), Mapping)"
                            },
                            {
                                "XXX TODO XXX": "[i, t] not in enumerate(sorted(self.vocabulary))"
                            },
                            {"XXX TODO XXX": "{}.setdefault(t, i) == i"},
                        ]
                    },
                    {
                        "anyOf": [
                            {"XXX TODO XXX": "isinstance(self.vocabulary, set)"},
                            {"XXX TODO XXX": "isinstance(self.vocabulary, Mapping)"},
                            {
                                "XXX TODO XXX": "[i, t] not in enumerate(self.vocabulary)"
                            },
                            {"XXX TODO XXX": "{}.setdefault(t, i) == i"},
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": "From /feature_extraction/text.py:_VectorizerMixin:_validate_vocabulary, Exception: raise ValueError('Vocabulary contains repeated indices.') ",
        "anyOf": [
            {"type": "object", "properties": {"vocabulary": {"enum": [None]}}},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {"XXX TODO XXX": "isinstance(self.vocabulary, set)"},
                            {
                                "XXX TODO XXX": "isinstance(sorted(self.vocabulary), Mapping)"
                            },
                            {
                                "XXX TODO XXX": "len(set(sorted(self.vocabulary).values())) == len(sorted(self.vocabulary))"
                            },
                        ]
                    },
                    {
                        "anyOf": [
                            {"XXX TODO XXX": "isinstance(self.vocabulary, set)"},
                            {"XXX TODO XXX": "isinstance(self.vocabulary, Mapping)"},
                            {
                                "XXX TODO XXX": "len(set(self.vocabulary.values())) == len(self.vocabulary)"
                            },
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": "From /feature_extraction/text.py:_VectorizerMixin:_validate_vocabulary, Exception: raise ValueError(msg) ",
        "anyOf": [
            {"type": "object", "properties": {"vocabulary": {"enum": [None]}}},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {"XXX TODO XXX": "isinstance(self.vocabulary, set)"},
                            {
                                "XXX TODO XXX": "isinstance(sorted(self.vocabulary), Mapping)"
                            },
                            {
                                "XXX TODO XXX": "i not in range(len(sorted(self.vocabulary)))"
                            },
                            {
                                "XXX TODO XXX": "i in set(sorted(self.vocabulary).values())"
                            },
                        ]
                    },
                    {
                        "anyOf": [
                            {"XXX TODO XXX": "isinstance(self.vocabulary, set)"},
                            {"XXX TODO XXX": "isinstance(self.vocabulary, Mapping)"},
                            {"XXX TODO XXX": "i not in range(len(self.vocabulary))"},
                            {"XXX TODO XXX": "i in set(self.vocabulary.values())"},
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": "From /feature_extraction/text.py:_VectorizerMixin:_validate_vocabulary, Exception: raise ValueError('empty vocabulary passed to fit') ",
        "anyOf": [
            {"type": "object", "properties": {"vocabulary": {"enum": [None]}}},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {"XXX TODO XXX": "isinstance(self.vocabulary, set)"},
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "isinstance(sorted(self.vocabulary), Mapping)"
                                            },
                                            {},
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "isinstance(sorted(self.vocabulary), Mapping)"
                                            },
                                            {"XXX TODO XXX": "sorted(self.vocabulary)"},
                                        ]
                                    },
                                ]
                            },
                        ]
                    },
                    {
                        "anyOf": [
                            {"XXX TODO XXX": "isinstance(self.vocabulary, set)"},
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "isinstance(self.vocabulary, Mapping)"
                                            },
                                            {},
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "isinstance(self.vocabulary, Mapping)"
                                            },
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "vocabulary": {"enum": [True]}
                                                },
                                            },
                                        ]
                                    },
                                ]
                            },
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": "From /feature_extraction/text.py:_VectorizerMixin:build_preprocessor, Exception: raise ValueError('Invalid value for \"strip_accents\": %s' % self.strip_accents) ",
        "anyOf": [
            {
                "type": "object",
                "properties": {"preprocessor": {"not": {"enum": [None]}}},
            },
            {"type": "object", "properties": {"strip_accents": {"enum": [False]}}},
            {"XXX TODO XXX": "callable(self.strip_accents)"},
            {"type": "object", "properties": {"strip_accents": {"enum": ["ascii"]}}},
            {"type": "object", "properties": {"strip_accents": {"enum": ["unicode"]}}},
        ],
    },
    {
        "description": "From /feature_extraction/text.py:None:_check_stop_list, Exception: raise ValueError('not a built-in stop list: %s' % stop) ",
        "anyOf": [
            {"type": "object", "properties": {"analyzer": {"enum": ["char"]}}},
            {"type": "object", "properties": {"analyzer": {"enum": ["char_wb"]}}},
            {"type": "object", "properties": {"analyzer": {"not": {"enum": ["word"]}}}},
            {"type": "object", "properties": {"stop_words": {"enum": ["english"]}}},
            {
                "type": "object",
                "properties": {"stop_words": {"not": {"type": "string"}}},
            },
        ],
    },
    {
        "description": "From /feature_extraction/text.py:_VectorizerMixin:build_tokenizer, Exception: raise ValueError(     'More than 1 capturing group in token pattern. Only a single group should be captured.'     ) ",
        "anyOf": [
            {"type": "object", "properties": {"analyzer": {"enum": ["char"]}}},
            {"type": "object", "properties": {"analyzer": {"enum": ["char_wb"]}}},
            {"type": "object", "properties": {"analyzer": {"not": {"enum": ["word"]}}}},
            {"type": "object", "properties": {"tokenizer": {"not": {"enum": [None]}}}},
            {"XXX TODO XXX": "re.compile(self.token_pattern).groups <= 1"},
        ],
    },
    {
        "description": "From /feature_extraction/text.py:_VectorizerMixin:build_analyzer, Exception: raise ValueError('%s is not a valid tokenization scheme/analyzer' % self.     analyzer) ",
        "anyOf": [
            {"type": "object", "properties": {"analyzer": {"enum": ["char"]}}},
            {"type": "object", "properties": {"analyzer": {"enum": ["char_wb"]}}},
            {"type": "object", "properties": {"analyzer": {"enum": ["word"]}}},
        ],
    },
    {
        "description": "From /feature_extraction/text.py:CountVectorizer:_count_vocab, Exception: raise ValueError(     'empty vocabulary; perhaps the documents only contain stop words') ",
        "anyOf": [
            {"type": "object", "properties": {"fixed_vocabulary_": {"enum": [True]}}},
            {},
        ],
    },
    {
        "description": "From /feature_extraction/text.py:CountVectorizer:_count_vocab, Exception: raise ValueError(     'sparse CSR array has {} non-zero elements and requires 64 bit indexing, which is unsupported with 32 bit Python.'     .format(indptr[-1])) ",
        "anyOf": [
            {"XXX TODO XXX": "indptr[-1] <= np.iinfo(np.int32).max"},
            {"type": "object", "properties": {"_IS_32BIT": {"enum": [False]}}},
        ],
    },
    {
        "description": "From /feature_extraction/text.py:CountVectorizer:_limit_features, Exception: raise ValueError(     'After pruning, no terms remain. Try a lower min_df or a higher max_df.') ",
        "anyOf": [
            {"type": "object", "properties": {"fixed_vocabulary_": {"enum": [True]}}},
            {
                "allOf": [
                    {
                        "XXX TODO XXX": "(self.max_df if isinstance(self.max_df, numbers.Integral) else self.max_df * X.shape[0]) is None"
                    },
                    {
                        "XXX TODO XXX": "(self.min_df if isinstance(self.min_df, numbers.Integral) else self.min_df * X.shape[0]) is None"
                    },
                    {
                        "type": "object",
                        "properties": {"max_features": {"enum": [None]}},
                    },
                ]
            },
            {"XXX TODO XXX": "len(np.where(mask)[0]) != 0"},
        ],
    },
    {
        "description": "From /feature_extraction/text.py:CountVectorizer:fit_transform, Exception: raise ValueError(     'Iterable over raw text documents expected, string object received.') ",
        "type": "object",
        "properties": {"raw_documents": {"not": {"type": "string"}}},
    },
    {
        "description": "From /feature_extraction/text.py:CountVectorizer:fit_transform, Exception: raise ValueError('max_df corresponds to < documents than min_df') ",
        "anyOf": [
            {"type": "object", "properties": {"fixed_vocabulary_": {"enum": [True]}}},
            {
                "XXX TODO XXX": "(self.max_df if isinstance(self.max_df, numbers.Integral) else self.max_df * X.shape[0]) >= (self.min_df if isinstance(self.min_df, numbers.Integral) else self.min_df * X.shape[0])"
            },
        ],
    },
]
