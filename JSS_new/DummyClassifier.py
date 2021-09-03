[
    {
        "description": "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) ",
        "anyOf": [
            {"XXX TODO XXX": "not hasattr(X, 'fit')"},
            {"XXX TODO XXX": "not callable(X.fit)"},
        ],
    },
    {
        "description": "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) ",
        "anyOf": [
            {"XXX TODO XXX": "hasattr(X, '__len__')"},
            {"XXX TODO XXX": "hasattr(X, 'shape')"},
            {"XXX TODO XXX": "hasattr(X, '__array__')"},
        ],
    },
    {
        "description": "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(     'Singleton array %r cannot be considered a valid collection.' % x) ",
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "hasattr(X, '__len__')"},
                    {"XXX TODO XXX": "hasattr(X, 'shape')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {"XXX TODO XXX": "not hasattr(X, '__array__')"},
                                    {
                                        "XXX TODO XXX": "not hasattr(np.asarray(X), 'shape')"
                                    },
                                    {"XXX TODO XXX": "np.asarray(X).shape is None"},
                                    {"XXX TODO XXX": "len(np.asarray(X).shape) != 0"},
                                ]
                            },
                            {
                                "anyOf": [
                                    {"XXX TODO XXX": "hasattr(X, '__array__')"},
                                    {"XXX TODO XXX": "not hasattr(X, 'shape')"},
                                    {"XXX TODO XXX": "X.shape is None"},
                                    {"XXX TODO XXX": "len(X.shape) != 0"},
                                ]
                            },
                        ]
                    },
                ]
            },
            {
                "anyOf": [
                    {
                        "allOf": [
                            {"XXX TODO XXX": "not hasattr(X, '__len__')"},
                            {"XXX TODO XXX": "not hasattr(X, 'shape')"},
                        ]
                    },
                    {"XXX TODO XXX": "not hasattr(X, 'shape')"},
                    {"XXX TODO XXX": "X.shape is None"},
                    {"XXX TODO XXX": "len(X.shape) != 0"},
                ]
            },
        ],
    },
    {
        "description": "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) from type_error ",
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "hasattr(X, '__len__')"},
                    {"XXX TODO XXX": "hasattr(X, 'shape')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {"XXX TODO XXX": "not hasattr(X, '__array__')"},
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "hasattr(np.asarray(X), 'shape')"
                                            },
                                            {
                                                "XXX TODO XXX": "np.asarray(X).shape is not None"
                                            },
                                        ]
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {"XXX TODO XXX": "hasattr(X, '__array__')"},
                                    {
                                        "allOf": [
                                            {"XXX TODO XXX": "hasattr(X, 'shape')"},
                                            {"XXX TODO XXX": "X.shape is not None"},
                                        ]
                                    },
                                ]
                            },
                        ]
                    },
                ]
            },
            {
                "anyOf": [
                    {
                        "allOf": [
                            {"XXX TODO XXX": "not hasattr(X, '__len__')"},
                            {"XXX TODO XXX": "not hasattr(X, 'shape')"},
                        ]
                    },
                    {
                        "allOf": [
                            {"XXX TODO XXX": "hasattr(X, 'shape')"},
                            {"XXX TODO XXX": "X.shape is not None"},
                        ]
                    },
                ]
            },
            {"XXX TODO XXX": "isinstance(x.shape[0], numbers.Integral)"},
        ],
    },
    {
        "description": "From /utils/validation.py:None:check_consistent_length, Exception: raise ValueError(     'Found input variables with inconsistent numbers of samples: %r' % [int     (l) for l in lengths]) ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "type": "object",
                        "properties": {
                            "strategy": {
                                "enum": [
                                    "most_frequent",
                                    "stratified",
                                    "uniform",
                                    "constant",
                                    "prior",
                                ]
                            }
                        },
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "strategy": {"not": {"enum": ["uniform"]}}
                                        },
                                    },
                                    {"type": "object", "laleNot": "X/isSparse"},
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {"XXX TODO XXX": "sp.issparse(y)"},
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "y.ndim != 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "y.ndim == 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "laleNot": "X/isSparse",
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "y.ndim != 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "y.ndim == 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                        ]
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "allOf": [
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "strategy": {"enum": ["uniform"]}
                                                },
                                            },
                                            {"XXX TODO XXX": "sp.issparse(y)"},
                                        ]
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {"XXX TODO XXX": "sp.issparse(y)"},
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "y.ndim != 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "y.ndim == 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "laleNot": "X/isSparse",
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "y.ndim != 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "y.ndim == 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                        ]
                                    },
                                ]
                            },
                        ]
                    },
                ]
            },
            {
                "anyOf": [
                    {
                        "type": "object",
                        "properties": {
                            "strategy": {
                                "not": {
                                    "enum": [
                                        "most_frequent",
                                        "stratified",
                                        "uniform",
                                        "constant",
                                        "prior",
                                    ]
                                }
                            }
                        },
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "strategy": {"not": {"enum": ["uniform"]}}
                                        },
                                    },
                                    {"type": "object", "laleNot": "X/isSparse"},
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {"XXX TODO XXX": "sp.issparse(y)"},
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "y.ndim != 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "y.ndim == 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "laleNot": "X/isSparse",
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "y.ndim != 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "y.ndim == 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                        ]
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "allOf": [
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "strategy": {"enum": ["uniform"]}
                                                },
                                            },
                                            {"XXX TODO XXX": "sp.issparse(y)"},
                                        ]
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {"XXX TODO XXX": "sp.issparse(y)"},
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "y.ndim != 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "y.ndim == 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "laleNot": "X/isSparse",
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "y.ndim != 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "y.ndim == 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
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
        "description": "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) ",
        "anyOf": [
            {"type": "object", "properties": {"sample_weight": {"enum": [None]}}},
            {"XXX TODO XXX": "not hasattr(X, 'fit')"},
            {"XXX TODO XXX": "not callable(X.fit)"},
        ],
    },
    {
        "description": "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) ",
        "anyOf": [
            {"type": "object", "properties": {"sample_weight": {"enum": [None]}}},
            {"XXX TODO XXX": "hasattr(X, '__len__')"},
            {"XXX TODO XXX": "hasattr(X, 'shape')"},
            {"XXX TODO XXX": "hasattr(X, '__array__')"},
        ],
    },
    {
        "description": "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(     'Singleton array %r cannot be considered a valid collection.' % x) ",
        "anyOf": [
            {"type": "object", "properties": {"sample_weight": {"enum": [None]}}},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {"XXX TODO XXX": "hasattr(X, '__len__')"},
                            {"XXX TODO XXX": "hasattr(X, 'shape')"},
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, '__array__')"
                                            },
                                            {
                                                "XXX TODO XXX": "not hasattr(np.asarray(X), 'shape')"
                                            },
                                            {
                                                "XXX TODO XXX": "np.asarray(X).shape is None"
                                            },
                                            {
                                                "XXX TODO XXX": "len(np.asarray(X).shape) != 0"
                                            },
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {"XXX TODO XXX": "hasattr(X, '__array__')"},
                                            {"XXX TODO XXX": "not hasattr(X, 'shape')"},
                                            {"XXX TODO XXX": "X.shape is None"},
                                            {"XXX TODO XXX": "len(X.shape) != 0"},
                                        ]
                                    },
                                ]
                            },
                        ]
                    },
                    {
                        "anyOf": [
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "not hasattr(X, '__len__')"},
                                    {"XXX TODO XXX": "not hasattr(X, 'shape')"},
                                ]
                            },
                            {"XXX TODO XXX": "not hasattr(X, 'shape')"},
                            {"XXX TODO XXX": "X.shape is None"},
                            {"XXX TODO XXX": "len(X.shape) != 0"},
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) from type_error ",
        "anyOf": [
            {"type": "object", "properties": {"sample_weight": {"enum": [None]}}},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {"XXX TODO XXX": "hasattr(X, '__len__')"},
                            {"XXX TODO XXX": "hasattr(X, 'shape')"},
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, '__array__')"
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(np.asarray(X), 'shape')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X).shape is not None"
                                                    },
                                                ]
                                            },
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {"XXX TODO XXX": "hasattr(X, '__array__')"},
                                            {
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, 'shape')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "X.shape is not None"
                                                    },
                                                ]
                                            },
                                        ]
                                    },
                                ]
                            },
                        ]
                    },
                    {
                        "anyOf": [
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "not hasattr(X, '__len__')"},
                                    {"XXX TODO XXX": "not hasattr(X, 'shape')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'shape')"},
                                    {"XXX TODO XXX": "X.shape is not None"},
                                ]
                            },
                        ]
                    },
                    {"XXX TODO XXX": "isinstance(x.shape[0], numbers.Integral)"},
                ]
            },
        ],
    },
    {
        "description": "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) ",
        "anyOf": [
            {"type": "object", "properties": {"sample_weight": {"enum": [None]}}},
            {"type": "object", "properties": {"sample_weight": {"enum": [None]}}},
            {"type": "object", "properties": {"sample_weight": {"type": "number"}}},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "hasattr(getattr(sample_weight, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {
                                        "XXX TODO XXX": "hasattr(sample_weight, 'dtypes')"
                                    },
                                    {
                                        "XXX TODO XXX": "hasattr(sample_weight.dtypes, '__array__')"
                                    },
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(sample_weight, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "sample_weight.ndim <= 1"},
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "type": "object",
                                                                "laleNot": "X/isSparse",
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(sample_weight.sparse.to_coo(), False, dtype=dtype[0], False, True, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(sample_weight.sparse.to_coo(), False, dtype=dtype[0], False, True, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(sample_weight.sparse.to_coo())"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "dtype[0] is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(sample_weight.sparse.to_coo(), order='C').astype(dtype[0], casting='unsafe', False), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(np.asarray(sample_weight.sparse.to_coo(), order='C').astype(dtype[0], casting='unsafe', False).fit)"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "dtype[0] is not None"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "np.dtype(dtype[0]).kind in 'iu'"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(sample_weight.sparse.to_coo(), order='C', dtype=dtype[0]), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(np.asarray(sample_weight.sparse.to_coo(), order='C', dtype=dtype[0]).fit)"
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(sample_weight, 'sparse')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "sample_weight.ndim > 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "type": "object",
                                                                "laleNot": "X/isSparse",
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(sample_weight, False, dtype=dtype[0], False, True, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(sample_weight, False, dtype=dtype[0], False, True, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(sample_weight)"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "dtype[0] is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(sample_weight, order='C').astype(dtype[0], casting='unsafe', False), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(np.asarray(sample_weight, order='C').astype(dtype[0], casting='unsafe', False).fit)"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "dtype[0] is not None"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "np.dtype(dtype[0]).kind in 'iu'"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(sample_weight, order='C', dtype=dtype[0]), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(np.asarray(sample_weight, order='C', dtype=dtype[0]).fit)"
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                        ]
                                    },
                                ]
                            },
                        ]
                    },
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "not hasattr(getattr(sample_weight, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {
                                        "XXX TODO XXX": "hasattr(sample_weight, 'dtypes')"
                                    },
                                    {
                                        "XXX TODO XXX": "hasattr(sample_weight.dtypes, '__array__')"
                                    },
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "getattr(sample_weight, 'dtype', None) is None"
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(sample_weight, 'dtype', None) not in [np.float64, np.float32]"
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "not hasattr(sample_weight, 'sparse')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sample_weight.ndim <= 1"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "laleNot": "X/isSparse",
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(sample_weight.sparse.to_coo(), False, None, False, True, True), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(sample_weight.sparse.to_coo(), False, None, False, True, True).fit)"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(sample_weight.sparse.to_coo())"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(sample_weight.sparse.to_coo(), order='C', None), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(np.asarray(sample_weight.sparse.to_coo(), order='C', None).fit)"
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(sample_weight, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "sample_weight.ndim > 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "laleNot": "X/isSparse",
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(sample_weight, False, None, False, True, True), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(sample_weight, False, None, False, True, True).fit)"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(sample_weight)"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(sample_weight, order='C', None), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(np.asarray(sample_weight, order='C', None).fit)"
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "getattr(sample_weight, 'dtype', None) is not None"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "getattr(sample_weight, 'dtype', None) in [np.float64, np.float32]"
                                                    },
                                                ]
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "not hasattr(sample_weight, 'sparse')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sample_weight.ndim <= 1"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "laleNot": "X/isSparse",
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(sample_weight.sparse.to_coo(), False, dtype=dtype[0], False, True, True), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(sample_weight.sparse.to_coo(), False, dtype=dtype[0], False, True, True).fit)"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(sample_weight.sparse.to_coo())"
                                                                            },
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "anyOf": [
                                                                                            {
                                                                                                "XXX TODO XXX": "dtype[0] is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(sample_weight.sparse.to_coo(), order='C').astype(dtype[0], casting='unsafe', False), 'fit')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not callable(np.asarray(sample_weight.sparse.to_coo(), order='C').astype(dtype[0], casting='unsafe', False).fit)"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                    {
                                                                                        "anyOf": [
                                                                                            {
                                                                                                "allOf": [
                                                                                                    {
                                                                                                        "XXX TODO XXX": "dtype[0] is not None"
                                                                                                    },
                                                                                                    {
                                                                                                        "XXX TODO XXX": "np.dtype(dtype[0]).kind in 'iu'"
                                                                                                    },
                                                                                                ]
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(sample_weight.sparse.to_coo(), order='C', dtype=dtype[0]), 'fit')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not callable(np.asarray(sample_weight.sparse.to_coo(), order='C', dtype=dtype[0]).fit)"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                ]
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(sample_weight, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "sample_weight.ndim > 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "laleNot": "X/isSparse",
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(sample_weight, False, dtype=dtype[0], False, True, True), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(sample_weight, False, dtype=dtype[0], False, True, True).fit)"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(sample_weight)"
                                                                            },
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "anyOf": [
                                                                                            {
                                                                                                "XXX TODO XXX": "dtype[0] is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(sample_weight, order='C').astype(dtype[0], casting='unsafe', False), 'fit')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not callable(np.asarray(sample_weight, order='C').astype(dtype[0], casting='unsafe', False).fit)"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                    {
                                                                                        "anyOf": [
                                                                                            {
                                                                                                "allOf": [
                                                                                                    {
                                                                                                        "XXX TODO XXX": "dtype[0] is not None"
                                                                                                    },
                                                                                                    {
                                                                                                        "XXX TODO XXX": "np.dtype(dtype[0]).kind in 'iu'"
                                                                                                    },
                                                                                                ]
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(sample_weight, order='C', dtype=dtype[0]), 'fit')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not callable(np.asarray(sample_weight, order='C', dtype=dtype[0]).fit)"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                ]
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
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
        "description": 'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) ',
        "anyOf": [
            {"type": "object", "properties": {"sample_weight": {"enum": [None]}}},
            {"type": "object", "properties": {"sample_weight": {"enum": [None]}}},
            {"type": "object", "properties": {"sample_weight": {"type": "number"}}},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {"XXX TODO XXX": "not hasattr(sample_weight, 'sparse')"},
                            {"XXX TODO XXX": "sample_weight.ndim <= 1"},
                            {"type": "object", "laleNot": "X/isSparse"},
                            {
                                "XXX TODO XXX": "not hasattr(sample_weight.sparse.to_coo(), 'dtype')"
                            },
                            {
                                "XXX TODO XXX": "sample_weight.sparse.to_coo().dtype is None"
                            },
                            {
                                "XXX TODO XXX": "not hasattr(sample_weight.sparse.to_coo().dtype, 'kind')"
                            },
                            {
                                "XXX TODO XXX": "sample_weight.sparse.to_coo().dtype.kind != 'c'"
                            },
                        ]
                    },
                    {
                        "anyOf": [
                            {
                                "allOf": [
                                    {
                                        "XXX TODO XXX": "hasattr(sample_weight, 'sparse')"
                                    },
                                    {"XXX TODO XXX": "sample_weight.ndim > 1"},
                                ]
                            },
                            {"type": "object", "laleNot": "X/isSparse"},
                            {"XXX TODO XXX": "not hasattr(sample_weight, 'dtype')"},
                            {"XXX TODO XXX": "sample_weight.dtype is None"},
                            {
                                "XXX TODO XXX": "not hasattr(sample_weight.dtype, 'kind')"
                            },
                            {"XXX TODO XXX": "sample_weight.dtype.kind != 'c'"},
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": "From /utils/validation.py:None:_ensure_sparse_format, Exception: raise TypeError(     'A sparse matrix was passed, but dense data is required. Use X.toarray() to convert to a dense numpy array.'     ) ",
        "anyOf": [
            {"type": "object", "properties": {"sample_weight": {"enum": [None]}}},
            {"type": "object", "properties": {"sample_weight": {"enum": [None]}}},
            {"type": "object", "properties": {"sample_weight": {"type": "number"}}},
            {"type": "object", "laleNot": "X/isSparse"},
        ],
    },
    {
        "description": 'From /utils/validation.py:None:check_array, Exception: raise ValueError("""Complex data not supported {} """.format(array)     ) from complex_warning ',
        "anyOf": [
            {"type": "object", "properties": {"sample_weight": {"enum": [None]}}},
            {"type": "object", "properties": {"sample_weight": {"enum": [None]}}},
            {"type": "object", "properties": {"sample_weight": {"type": "number"}}},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {"XXX TODO XXX": "not hasattr(sample_weight, 'sparse')"},
                            {"XXX TODO XXX": "sample_weight.ndim <= 1"},
                            {
                                "XXX TODO XXX": "sp.issparse(sample_weight.sparse.to_coo())"
                            },
                        ]
                    },
                    {
                        "anyOf": [
                            {
                                "allOf": [
                                    {
                                        "XXX TODO XXX": "hasattr(sample_weight, 'sparse')"
                                    },
                                    {"XXX TODO XXX": "sample_weight.ndim > 1"},
                                ]
                            },
                            {"XXX TODO XXX": "sp.issparse(sample_weight)"},
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": "From /utils/validation.py:None:check_array, Exception: raise ValueError('Found array with dim %d. %s expected <= 2.' % (array.ndim,     estimator_name)) ",
        "anyOf": [
            {"type": "object", "properties": {"sample_weight": {"enum": [None]}}},
            {"type": "object", "properties": {"sample_weight": {"enum": [None]}}},
            {"type": "object", "properties": {"sample_weight": {"type": "number"}}},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "hasattr(getattr(sample_weight, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {
                                        "XXX TODO XXX": "hasattr(sample_weight, 'dtypes')"
                                    },
                                    {
                                        "XXX TODO XXX": "hasattr(sample_weight.dtypes, '__array__')"
                                    },
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(sample_weight, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "sample_weight.ndim <= 1"},
                                            {
                                                "XXX TODO XXX": "sp.issparse(sample_weight.sparse.to_coo())"
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "dtype[0] is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(sample_weight.sparse.to_coo(), order='C').astype(dtype[0], casting='unsafe', False).ndim < 3"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "XXX TODO XXX": "dtype[0] is not None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.dtype(dtype[0]).kind in 'iu'"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(sample_weight.sparse.to_coo(), order='C', dtype=dtype[0]).ndim < 3"
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(sample_weight, 'sparse')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "sample_weight.ndim > 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "XXX TODO XXX": "sp.issparse(sample_weight)"
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "dtype[0] is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(sample_weight, order='C').astype(dtype[0], casting='unsafe', False).ndim < 3"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "XXX TODO XXX": "dtype[0] is not None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.dtype(dtype[0]).kind in 'iu'"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(sample_weight, order='C', dtype=dtype[0]).ndim < 3"
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                        ]
                                    },
                                ]
                            },
                        ]
                    },
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "not hasattr(getattr(sample_weight, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {
                                        "XXX TODO XXX": "hasattr(sample_weight, 'dtypes')"
                                    },
                                    {
                                        "XXX TODO XXX": "hasattr(sample_weight.dtypes, '__array__')"
                                    },
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "getattr(sample_weight, 'dtype', None) is None"
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(sample_weight, 'dtype', None) not in [np.float64, np.float32]"
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "not hasattr(sample_weight, 'sparse')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sample_weight.ndim <= 1"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(sample_weight.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(sample_weight.sparse.to_coo(), order='C', None).ndim < 3"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(sample_weight, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "sample_weight.ndim > 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(sample_weight)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(sample_weight, order='C', None).ndim < 3"
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "getattr(sample_weight, 'dtype', None) is not None"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "getattr(sample_weight, 'dtype', None) in [np.float64, np.float32]"
                                                    },
                                                ]
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "not hasattr(sample_weight, 'sparse')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sample_weight.ndim <= 1"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(sample_weight.sparse.to_coo())"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "dtype[0] is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(sample_weight.sparse.to_coo(), order='C').astype(dtype[0], casting='unsafe', False).ndim < 3"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "dtype[0] is not None"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "np.dtype(dtype[0]).kind in 'iu'"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(sample_weight.sparse.to_coo(), order='C', dtype=dtype[0]).ndim < 3"
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(sample_weight, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "sample_weight.ndim > 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(sample_weight)"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "dtype[0] is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(sample_weight, order='C').astype(dtype[0], casting='unsafe', False).ndim < 3"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "dtype[0] is not None"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "np.dtype(dtype[0]).kind in 'iu'"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(sample_weight, order='C', dtype=dtype[0]).ndim < 3"
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
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
        "description": "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Found array with %d sample(s) (shape=%s) while a minimum of %d is required%s.'      % (n_samples, array.shape, ensure_min_samples, context)) ",
        "anyOf": [
            {"type": "object", "properties": {"sample_weight": {"enum": [None]}}},
            {"type": "object", "properties": {"sample_weight": {"enum": [None]}}},
            {"type": "object", "properties": {"sample_weight": {"type": "number"}}},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "hasattr(getattr(sample_weight, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {
                                        "XXX TODO XXX": "hasattr(sample_weight, 'dtypes')"
                                    },
                                    {
                                        "XXX TODO XXX": "hasattr(sample_weight.dtypes, '__array__')"
                                    },
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(sample_weight, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "sample_weight.ndim <= 1"},
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "type": "object",
                                                                "laleNot": "X/isSparse",
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(sample_weight.sparse.to_coo(), False, dtype=dtype[0], False, True, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(sample_weight.sparse.to_coo())"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "dtype[0] is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "_num_samples(np.asarray(sample_weight.sparse.to_coo(), order='C').astype(dtype[0], casting='unsafe', False)) >= 1"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "dtype[0] is not None"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "np.dtype(dtype[0]).kind in 'iu'"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "_num_samples(np.asarray(sample_weight.sparse.to_coo(), order='C', dtype=dtype[0])) >= 1"
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(sample_weight, 'sparse')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "sample_weight.ndim > 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "type": "object",
                                                                "laleNot": "X/isSparse",
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(sample_weight, False, dtype=dtype[0], False, True, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(sample_weight)"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "dtype[0] is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "_num_samples(np.asarray(sample_weight, order='C').astype(dtype[0], casting='unsafe', False)) >= 1"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "dtype[0] is not None"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "np.dtype(dtype[0]).kind in 'iu'"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "_num_samples(np.asarray(sample_weight, order='C', dtype=dtype[0])) >= 1"
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                        ]
                                    },
                                ]
                            },
                        ]
                    },
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "not hasattr(getattr(sample_weight, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {
                                        "XXX TODO XXX": "hasattr(sample_weight, 'dtypes')"
                                    },
                                    {
                                        "XXX TODO XXX": "hasattr(sample_weight.dtypes, '__array__')"
                                    },
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "getattr(sample_weight, 'dtype', None) is None"
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(sample_weight, 'dtype', None) not in [np.float64, np.float32]"
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "not hasattr(sample_weight, 'sparse')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sample_weight.ndim <= 1"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "laleNot": "X/isSparse",
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(sample_weight.sparse.to_coo(), False, None, False, True, True)) >= 1"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(sample_weight.sparse.to_coo())"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "_num_samples(np.asarray(sample_weight.sparse.to_coo(), order='C', None)) >= 1"
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(sample_weight, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "sample_weight.ndim > 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "laleNot": "X/isSparse",
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(sample_weight, False, None, False, True, True)) >= 1"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(sample_weight)"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "_num_samples(np.asarray(sample_weight, order='C', None)) >= 1"
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "getattr(sample_weight, 'dtype', None) is not None"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "getattr(sample_weight, 'dtype', None) in [np.float64, np.float32]"
                                                    },
                                                ]
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "not hasattr(sample_weight, 'sparse')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sample_weight.ndim <= 1"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "laleNot": "X/isSparse",
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(sample_weight.sparse.to_coo(), False, dtype=dtype[0], False, True, True)) >= 1"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(sample_weight.sparse.to_coo())"
                                                                            },
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "anyOf": [
                                                                                            {
                                                                                                "XXX TODO XXX": "dtype[0] is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "_num_samples(np.asarray(sample_weight.sparse.to_coo(), order='C').astype(dtype[0], casting='unsafe', False)) >= 1"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                    {
                                                                                        "anyOf": [
                                                                                            {
                                                                                                "allOf": [
                                                                                                    {
                                                                                                        "XXX TODO XXX": "dtype[0] is not None"
                                                                                                    },
                                                                                                    {
                                                                                                        "XXX TODO XXX": "np.dtype(dtype[0]).kind in 'iu'"
                                                                                                    },
                                                                                                ]
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "_num_samples(np.asarray(sample_weight.sparse.to_coo(), order='C', dtype=dtype[0])) >= 1"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                ]
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(sample_weight, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "sample_weight.ndim > 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "laleNot": "X/isSparse",
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(sample_weight, False, dtype=dtype[0], False, True, True)) >= 1"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(sample_weight)"
                                                                            },
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "anyOf": [
                                                                                            {
                                                                                                "XXX TODO XXX": "dtype[0] is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "_num_samples(np.asarray(sample_weight, order='C').astype(dtype[0], casting='unsafe', False)) >= 1"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                    {
                                                                                        "anyOf": [
                                                                                            {
                                                                                                "allOf": [
                                                                                                    {
                                                                                                        "XXX TODO XXX": "dtype[0] is not None"
                                                                                                    },
                                                                                                    {
                                                                                                        "XXX TODO XXX": "np.dtype(dtype[0]).kind in 'iu'"
                                                                                                    },
                                                                                                ]
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "_num_samples(np.asarray(sample_weight, order='C', dtype=dtype[0])) >= 1"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                ]
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
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
        "description": "From /utils/validation.py:None:_check_sample_weight, Exception: raise ValueError('Sample weights must be 1D array or scalar') ",
        "anyOf": [
            {"type": "object", "properties": {"sample_weight": {"enum": [None]}}},
            {"type": "object", "properties": {"sample_weight": {"enum": [None]}}},
            {"type": "object", "properties": {"sample_weight": {"type": "number"}}},
            {
                "XXX TODO XXX": "check_array(sample_weight, False, False, dtype=[np.float64, np.float32], order='C', False).ndim == 1"
            },
        ],
    },
    {
        "description": "From /utils/validation.py:None:_check_sample_weight, Exception: raise ValueError('sample_weight.shape == {}, expected {}!'.format(     sample_weight.shape, (n_samples,))) ",
        "anyOf": [
            {"type": "object", "properties": {"sample_weight": {"enum": [None]}}},
            {"type": "object", "properties": {"sample_weight": {"enum": [None]}}},
            {"type": "object", "properties": {"sample_weight": {"type": "number"}}},
            {
                "XXX TODO XXX": "check_array(sample_weight, False, False, dtype=[np.float64, np.float32], order='C', False).shape == [_num_samples(X)]"
            },
        ],
    },
    {
        "description": "From /dummy.py:DummyClassifier:fit, Exception: raise ValueError('Unknown strategy type: %s, expected one of %s.' % (self.     strategy, allowed_strategies)) ",
        "type": "object",
        "properties": {
            "strategy": {
                "enum": ["most_frequent", "stratified", "uniform", "constant", "prior"]
            }
        },
    },
    {
        "description": "From /dummy.py:DummyClassifier:fit, Exception: raise ValueError(     'Constant target value has to be specified when the constant strategy is used.'     ) ",
        "anyOf": [
            {
                "type": "object",
                "properties": {"strategy": {"not": {"enum": ["constant"]}}},
            },
            {"type": "object", "properties": {"constant": {"not": {"enum": [None]}}}},
        ],
    },
    {
        "description": "From /dummy.py:DummyClassifier:fit, Exception: raise ValueError('Constant target value should have shape (%d, 1).' % self.     n_outputs_) ",
        "anyOf": [
            {
                "type": "object",
                "properties": {"strategy": {"not": {"enum": ["constant"]}}},
            },
            {"type": "object", "properties": {"constant": {"enum": [None]}}},
            {"XXX TODO XXX": "constant.shape[0] == y.shape[1]"},
        ],
    },
    {
        "description": "From /dummy.py:DummyClassifier:fit, Exception: raise ValueError(err_msg) ",
        "anyOf": [
            {
                "type": "object",
                "properties": {"strategy": {"not": {"enum": ["constant"]}}},
            },
            {"XXX TODO XXX": "k not in range(y.shape[1])"},
            {"XXX TODO XXX": "any((constant[k][0] == c for c in self.classes_[k]))"},
        ],
    },
]
