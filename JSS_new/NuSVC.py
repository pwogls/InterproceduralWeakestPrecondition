[
    {
        "description": "From /utils/validation.py:None:check_random_state, Exception: raise ValueError(     '%r cannot be used to seed a numpy.random.RandomState instance' % seed) ",
        "anyOf": [
            {"type": "object", "properties": {"random_state": {"enum": [None]}}},
            {"XXX TODO XXX": "self.random_state is np.random"},
            {"XXX TODO XXX": "isinstance(self.random_state, np.random.RandomState)"},
        ],
    },
    {
        "description": "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) ",
        "anyOf": [
            {"XXX TODO XXX": "not callable(self.kernel)"},
            {"XXX TODO XXX": "not hasattr(X, 'fit')"},
            {"XXX TODO XXX": "not callable(X.fit)"},
        ],
    },
    {
        "description": "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) ",
        "anyOf": [
            {"XXX TODO XXX": "not callable(self.kernel)"},
            {"XXX TODO XXX": "hasattr(X, '__len__')"},
            {"XXX TODO XXX": "hasattr(X, 'shape')"},
            {"XXX TODO XXX": "hasattr(X, '__array__')"},
        ],
    },
    {
        "description": "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(     'Singleton array %r cannot be considered a valid collection.' % x) ",
        "anyOf": [
            {"XXX TODO XXX": "not callable(self.kernel)"},
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
            {"XXX TODO XXX": "not callable(self.kernel)"},
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
        "description": "From /utils/validation.py:None:check_consistent_length, Exception: raise ValueError(     'Found input variables with inconsistent numbers of samples: %r' % [int     (l) for l in lengths]) ",
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "not sp.isspmatrix(X)"},
                    {
                        "type": "object",
                        "properties": {"kernel": {"not": {"enum": ["precomputed"]}}},
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "not hasattr(self, 'decision_function_shape')"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "decision_function_shape": {
                                                                "enum": ["ovr", "ovo"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(self.kernel)"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "decision_function_shape": {
                                                                "not": {
                                                                    "enum": [
                                                                        "ovr",
                                                                        "ovo",
                                                                    ]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(self.kernel)"
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
                                        "XXX TODO XXX": "hasattr(self, 'decision_function_shape')"
                                    },
                                    {"XXX TODO XXX": "not callable(self.kernel)"},
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
                        "allOf": [
                            {"XXX TODO XXX": "sp.isspmatrix(X)"},
                            {
                                "type": "object",
                                "properties": {"kernel": {"enum": ["precomputed"]}},
                            },
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "not hasattr(self, 'decision_function_shape')"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "decision_function_shape": {
                                                                "enum": ["ovr", "ovo"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(self.kernel)"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "decision_function_shape": {
                                                                "not": {
                                                                    "enum": [
                                                                        "ovr",
                                                                        "ovo",
                                                                    ]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(self.kernel)"
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
                                        "XXX TODO XXX": "hasattr(self, 'decision_function_shape')"
                                    },
                                    {"XXX TODO XXX": "not callable(self.kernel)"},
                                    {
                                        "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
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
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"not": {"enum": [None]}}}},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "X.ndim <= 1"},
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "type": "object",
                                                                "laleNot": "X/isSparse",
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, False), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, False).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).fit)"
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
                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "X.ndim > 1"},
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(X, order='C', dtype=np.float64).fit)"
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
                                "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "X.ndim <= 1"},
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "type": "object",
                                                                "laleNot": "X/isSparse",
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, False), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, False).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).fit)"
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
                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "X.ndim > 1"},
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(X, order='C', dtype=np.float64).fit)"
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
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"not": {"enum": [None]}}}},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {"XXX TODO XXX": "not hasattr(X, 'sparse')"},
                            {"XXX TODO XXX": "X.ndim <= 1"},
                            {"type": "object", "laleNot": "X/isSparse"},
                            {"XXX TODO XXX": "not hasattr(X.sparse.to_coo(), 'dtype')"},
                            {"XXX TODO XXX": "X.sparse.to_coo().dtype is None"},
                            {
                                "XXX TODO XXX": "not hasattr(X.sparse.to_coo().dtype, 'kind')"
                            },
                            {"XXX TODO XXX": "X.sparse.to_coo().dtype.kind != 'c'"},
                        ]
                    },
                    {
                        "anyOf": [
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'sparse')"},
                                    {"XXX TODO XXX": "X.ndim > 1"},
                                ]
                            },
                            {"type": "object", "laleNot": "X/isSparse"},
                            {"XXX TODO XXX": "not hasattr(X, 'dtype')"},
                            {"XXX TODO XXX": "X.dtype is None"},
                            {"XXX TODO XXX": "not hasattr(X.dtype, 'kind')"},
                            {"XXX TODO XXX": "X.dtype.kind != 'c'"},
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": 'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) ',
        "anyOf": [
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"not": {"enum": [None]}}}},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'dtypes')"
                                            },
                                            {
                                                "XXX TODO XXX": "not hasattr(X.dtypes, '__array__')"
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "not all((False for np.float64 in list(X.dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "X.ndim <= 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype.kind != 'c'"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "all((False for np.float64 in list(X.dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "X.ndim <= 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype.kind != 'c'"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype.kind != 'c'"
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
                                                        "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                    },
                                                ]
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "X.ndim <= 1"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype.kind != 'c'"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype.kind != 'c'"
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
                                "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'dtypes')"
                                            },
                                            {
                                                "XXX TODO XXX": "not hasattr(X.dtypes, '__array__')"
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "not all((False for np.float64 in list(X.dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "X.ndim <= 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype.kind != 'c'"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "all((False for np.float64 in list(X.dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "X.ndim <= 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype.kind != 'c'"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype.kind != 'c'"
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
                                                        "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                    },
                                                ]
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "X.ndim <= 1"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype.kind != 'c'"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype.kind != 'c'"
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
        "description": "From /utils/validation.py:None:_check_large_sparse, Exception: raise ValueError(     'Only sparse matrices with 32-bit integer indices are accepted. Got %s indices.'      % indices_datatype) ",
        "anyOf": [
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"not": {"enum": [None]}}}},
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                    {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                ]
            },
            {
                "allOf": [
                    {
                        "anyOf": [
                            {"XXX TODO XXX": "not hasattr(X, 'sparse')"},
                            {"XXX TODO XXX": "X.ndim <= 1"},
                            {"type": "object", "laleNot": "X/isSparse"},
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "X.sparse.to_coo().getformat() != 'coo'"
                                            },
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "key": {
                                                        "not": {"enum": ["col", "row"]}
                                                    }
                                                },
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(X.sparse.to_coo(), key).dtype in ['int32']"
                                            },
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "X.sparse.to_coo().getformat() == 'coo'"
                                            },
                                            {
                                                "XXX TODO XXX": "X.sparse.to_coo().getformat() not in ['csr', 'csc', 'bsr']"
                                            },
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "key": {
                                                        "not": {
                                                            "enum": [
                                                                "indices",
                                                                "indptr",
                                                            ]
                                                        }
                                                    }
                                                },
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(X.sparse.to_coo(), key).dtype in ['int32']"
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
                                    {"XXX TODO XXX": "hasattr(X, 'sparse')"},
                                    {"XXX TODO XXX": "X.ndim > 1"},
                                ]
                            },
                            {"type": "object", "laleNot": "X/isSparse"},
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {"XXX TODO XXX": "X.getformat() != 'coo'"},
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "key": {
                                                        "not": {"enum": ["col", "row"]}
                                                    }
                                                },
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(X, key).dtype in ['int32']"
                                            },
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {"XXX TODO XXX": "X.getformat() == 'coo'"},
                                            {
                                                "XXX TODO XXX": "X.getformat() not in ['csr', 'csc', 'bsr']"
                                            },
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "key": {
                                                        "not": {
                                                            "enum": [
                                                                "indices",
                                                                "indptr",
                                                            ]
                                                        }
                                                    }
                                                },
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(X, key).dtype in ['int32']"
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
        "description": "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Pandas DataFrame with mixed sparse extension arrays generated a sparse matrix with object dtype which can not be converted to a scipy sparse matrix.Sparse extension arrays should all have the same numeric type.'     ) ",
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "not sp.isspmatrix(X)"},
                    {
                        "type": "object",
                        "properties": {"kernel": {"not": {"enum": ["precomputed"]}}},
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "not hasattr(self, 'decision_function_shape')"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "decision_function_shape": {
                                                                "enum": ["ovr", "ovo"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "callable(self.kernel)"
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "y": {
                                                                "not": {"enum": [None]}
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "not self._get_tags()['requires_y']"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "anyOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                                    },
                                                                                    {
                                                                                        "allOf": [
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "anyOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                                    },
                                                                                    {
                                                                                        "allOf": [
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
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
                                                                        "XXX TODO XXX": "self._get_tags()['requires_y']"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "anyOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                                    },
                                                                                    {
                                                                                        "allOf": [
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "anyOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                                    },
                                                                                    {
                                                                                        "allOf": [
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
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
                                                            "decision_function_shape": {
                                                                "not": {
                                                                    "enum": [
                                                                        "ovr",
                                                                        "ovo",
                                                                    ]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "callable(self.kernel)"
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "y": {
                                                                "not": {"enum": [None]}
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "not self._get_tags()['requires_y']"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "anyOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                                    },
                                                                                    {
                                                                                        "allOf": [
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "anyOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                                    },
                                                                                    {
                                                                                        "allOf": [
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
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
                                                                        "XXX TODO XXX": "self._get_tags()['requires_y']"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "anyOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                                    },
                                                                                    {
                                                                                        "allOf": [
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "anyOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                                    },
                                                                                    {
                                                                                        "allOf": [
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
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
                                        "XXX TODO XXX": "hasattr(self, 'decision_function_shape')"
                                    },
                                    {"XXX TODO XXX": "callable(self.kernel)"},
                                    {
                                        "type": "object",
                                        "properties": {"y": {"not": {"enum": [None]}}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "not self._get_tags()['requires_y']"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
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
                                                        "XXX TODO XXX": "self._get_tags()['requires_y']"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
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
                        "allOf": [
                            {"XXX TODO XXX": "sp.isspmatrix(X)"},
                            {
                                "type": "object",
                                "properties": {"kernel": {"enum": ["precomputed"]}},
                            },
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "not hasattr(self, 'decision_function_shape')"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "decision_function_shape": {
                                                                "enum": ["ovr", "ovo"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "callable(self.kernel)"
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "y": {
                                                                "not": {"enum": [None]}
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "not self._get_tags()['requires_y']"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "anyOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                                    },
                                                                                    {
                                                                                        "allOf": [
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "anyOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                                    },
                                                                                    {
                                                                                        "allOf": [
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
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
                                                                        "XXX TODO XXX": "self._get_tags()['requires_y']"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "anyOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                                    },
                                                                                    {
                                                                                        "allOf": [
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "anyOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                                    },
                                                                                    {
                                                                                        "allOf": [
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
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
                                                            "decision_function_shape": {
                                                                "not": {
                                                                    "enum": [
                                                                        "ovr",
                                                                        "ovo",
                                                                    ]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "callable(self.kernel)"
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "y": {
                                                                "not": {"enum": [None]}
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "not self._get_tags()['requires_y']"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "anyOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                                    },
                                                                                    {
                                                                                        "allOf": [
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "anyOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                                    },
                                                                                    {
                                                                                        "allOf": [
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
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
                                                                        "XXX TODO XXX": "self._get_tags()['requires_y']"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "anyOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                                    },
                                                                                    {
                                                                                        "allOf": [
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "anyOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                                    },
                                                                                    {
                                                                                        "allOf": [
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
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
                                        "XXX TODO XXX": "hasattr(self, 'decision_function_shape')"
                                    },
                                    {"XXX TODO XXX": "callable(self.kernel)"},
                                    {
                                        "type": "object",
                                        "properties": {"y": {"not": {"enum": [None]}}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "not self._get_tags()['requires_y']"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
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
                                                        "XXX TODO XXX": "self._get_tags()['requires_y']"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
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
        "description": 'From /utils/validation.py:None:check_array, Exception: raise ValueError("""Complex data not supported {} """.format(array)     ) from complex_warning ',
        "anyOf": [
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"not": {"enum": [None]}}}},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {"XXX TODO XXX": "not hasattr(X, 'sparse')"},
                            {"XXX TODO XXX": "X.ndim <= 1"},
                            {"XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"},
                        ]
                    },
                    {
                        "anyOf": [
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'sparse')"},
                                    {"XXX TODO XXX": "X.ndim > 1"},
                                ]
                            },
                            {"XXX TODO XXX": "sp.issparse(X)"},
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": "From /utils/validation.py:None:check_array, Exception: raise ValueError('Found array with dim %d. %s expected <= 2.' % (array.ndim,     estimator_name)) ",
        "anyOf": [
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"not": {"enum": [None]}}}},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "X.ndim <= 1"},
                                            {
                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                            },
                                            {
                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).ndim < 3"
                                            },
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "X.ndim > 1"},
                                                ]
                                            },
                                            {"XXX TODO XXX": "sp.issparse(X)"},
                                            {
                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).ndim < 3"
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
                                "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "X.ndim <= 1"},
                                            {
                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                            },
                                            {
                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).ndim < 3"
                                            },
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "X.ndim > 1"},
                                                ]
                                            },
                                            {"XXX TODO XXX": "sp.issparse(X)"},
                                            {
                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).ndim < 3"
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
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"not": {"enum": [None]}}}},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "X.ndim <= 1"},
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "type": "object",
                                                                "laleNot": "X/isSparse",
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, False)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64)) >= 1"
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
                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "X.ndim > 1"},
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(X, order='C', dtype=np.float64)) >= 1"
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
                                "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "X.ndim <= 1"},
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "type": "object",
                                                                "laleNot": "X/isSparse",
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, False)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64)) >= 1"
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
                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "X.ndim > 1"},
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(X, order='C', dtype=np.float64)) >= 1"
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
        "description": "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Found array with %d feature(s) (shape=%s) while a minimum of %d is required%s.'      % (n_features, array.shape, ensure_min_features, context)) ",
        "anyOf": [
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"not": {"enum": [None]}}}},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "X.ndim <= 1"},
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "type": "object",
                                                                "laleNot": "X/isSparse",
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, False).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
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
                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "X.ndim > 1"},
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
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
                                "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "X.ndim <= 1"},
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "type": "object",
                                                                "laleNot": "X/isSparse",
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, False).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
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
                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "X.ndim > 1"},
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
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
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"enum": [None]}}},
            {"type": "object", "properties": {"y": {"not": {"type": "string"}}}},
            {
                "type": "object",
                "properties": {"y": {"not": {"enum": ["no_validation"]}}},
            },
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "X.ndim <= 1"},
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "type": "object",
                                                                "laleNot": "X/isSparse",
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, False), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, False).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).fit)"
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
                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "X.ndim > 1"},
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(X, order='C', dtype=np.float64).fit)"
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
                                "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "X.ndim <= 1"},
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "type": "object",
                                                                "laleNot": "X/isSparse",
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, False), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, False).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).fit)"
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
                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "X.ndim > 1"},
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(X, order='C', dtype=np.float64).fit)"
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
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"enum": [None]}}},
            {"type": "object", "properties": {"y": {"not": {"type": "string"}}}},
            {
                "type": "object",
                "properties": {"y": {"not": {"enum": ["no_validation"]}}},
            },
            {
                "allOf": [
                    {
                        "anyOf": [
                            {"XXX TODO XXX": "not hasattr(X, 'sparse')"},
                            {"XXX TODO XXX": "X.ndim <= 1"},
                            {"type": "object", "laleNot": "X/isSparse"},
                            {"XXX TODO XXX": "not hasattr(X.sparse.to_coo(), 'dtype')"},
                            {"XXX TODO XXX": "X.sparse.to_coo().dtype is None"},
                            {
                                "XXX TODO XXX": "not hasattr(X.sparse.to_coo().dtype, 'kind')"
                            },
                            {"XXX TODO XXX": "X.sparse.to_coo().dtype.kind != 'c'"},
                        ]
                    },
                    {
                        "anyOf": [
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'sparse')"},
                                    {"XXX TODO XXX": "X.ndim > 1"},
                                ]
                            },
                            {"type": "object", "laleNot": "X/isSparse"},
                            {"XXX TODO XXX": "not hasattr(X, 'dtype')"},
                            {"XXX TODO XXX": "X.dtype is None"},
                            {"XXX TODO XXX": "not hasattr(X.dtype, 'kind')"},
                            {"XXX TODO XXX": "X.dtype.kind != 'c'"},
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": 'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) ',
        "anyOf": [
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"enum": [None]}}},
            {"type": "object", "properties": {"y": {"not": {"type": "string"}}}},
            {
                "type": "object",
                "properties": {"y": {"not": {"enum": ["no_validation"]}}},
            },
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'dtypes')"
                                            },
                                            {
                                                "XXX TODO XXX": "not hasattr(X.dtypes, '__array__')"
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "not all((False for np.float64 in list(X.dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "X.ndim <= 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype.kind != 'c'"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "all((False for np.float64 in list(X.dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "X.ndim <= 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype.kind != 'c'"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype.kind != 'c'"
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
                                                        "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                    },
                                                ]
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "X.ndim <= 1"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype.kind != 'c'"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype.kind != 'c'"
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
                                "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'dtypes')"
                                            },
                                            {
                                                "XXX TODO XXX": "not hasattr(X.dtypes, '__array__')"
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "not all((False for np.float64 in list(X.dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "X.ndim <= 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype.kind != 'c'"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "all((False for np.float64 in list(X.dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "X.ndim <= 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype.kind != 'c'"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype.kind != 'c'"
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
                                                        "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                    },
                                                ]
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "X.ndim <= 1"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype.kind != 'c'"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype.kind != 'c'"
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
        "description": "From /utils/validation.py:None:_check_large_sparse, Exception: raise ValueError(     'Only sparse matrices with 32-bit integer indices are accepted. Got %s indices.'      % indices_datatype) ",
        "anyOf": [
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"enum": [None]}}},
            {"type": "object", "properties": {"y": {"not": {"type": "string"}}}},
            {
                "type": "object",
                "properties": {"y": {"not": {"enum": ["no_validation"]}}},
            },
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                    {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                ]
            },
            {
                "allOf": [
                    {
                        "anyOf": [
                            {"XXX TODO XXX": "not hasattr(X, 'sparse')"},
                            {"XXX TODO XXX": "X.ndim <= 1"},
                            {"type": "object", "laleNot": "X/isSparse"},
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "X.sparse.to_coo().getformat() != 'coo'"
                                            },
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "key": {
                                                        "not": {"enum": ["col", "row"]}
                                                    }
                                                },
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(X.sparse.to_coo(), key).dtype in ['int32']"
                                            },
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "X.sparse.to_coo().getformat() == 'coo'"
                                            },
                                            {
                                                "XXX TODO XXX": "X.sparse.to_coo().getformat() not in ['csr', 'csc', 'bsr']"
                                            },
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "key": {
                                                        "not": {
                                                            "enum": [
                                                                "indices",
                                                                "indptr",
                                                            ]
                                                        }
                                                    }
                                                },
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(X.sparse.to_coo(), key).dtype in ['int32']"
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
                                    {"XXX TODO XXX": "hasattr(X, 'sparse')"},
                                    {"XXX TODO XXX": "X.ndim > 1"},
                                ]
                            },
                            {"type": "object", "laleNot": "X/isSparse"},
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {"XXX TODO XXX": "X.getformat() != 'coo'"},
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "key": {
                                                        "not": {"enum": ["col", "row"]}
                                                    }
                                                },
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(X, key).dtype in ['int32']"
                                            },
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {"XXX TODO XXX": "X.getformat() == 'coo'"},
                                            {
                                                "XXX TODO XXX": "X.getformat() not in ['csr', 'csc', 'bsr']"
                                            },
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "key": {
                                                        "not": {
                                                            "enum": [
                                                                "indices",
                                                                "indptr",
                                                            ]
                                                        }
                                                    }
                                                },
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(X, key).dtype in ['int32']"
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
        "description": "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Pandas DataFrame with mixed sparse extension arrays generated a sparse matrix with object dtype which can not be converted to a scipy sparse matrix.Sparse extension arrays should all have the same numeric type.'     ) ",
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "not sp.isspmatrix(X)"},
                    {
                        "type": "object",
                        "properties": {"kernel": {"not": {"enum": ["precomputed"]}}},
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "not hasattr(self, 'decision_function_shape')"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "decision_function_shape": {
                                                                "enum": ["ovr", "ovo"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "callable(self.kernel)"
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "y": {"enum": [None]}
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "y": {
                                                                "not": {
                                                                    "type": "string"
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "y": {
                                                                "not": {
                                                                    "enum": [
                                                                        "no_validation"
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
                                                                        "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
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
                                                            "decision_function_shape": {
                                                                "not": {
                                                                    "enum": [
                                                                        "ovr",
                                                                        "ovo",
                                                                    ]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "callable(self.kernel)"
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "y": {"enum": [None]}
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "y": {
                                                                "not": {
                                                                    "type": "string"
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "y": {
                                                                "not": {
                                                                    "enum": [
                                                                        "no_validation"
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
                                                                        "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
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
                                        "XXX TODO XXX": "hasattr(self, 'decision_function_shape')"
                                    },
                                    {"XXX TODO XXX": "callable(self.kernel)"},
                                    {
                                        "type": "object",
                                        "properties": {"y": {"enum": [None]}},
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "y": {"not": {"type": "string"}}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "y": {"not": {"enum": ["no_validation"]}}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "X.ndim <= 1"},
                                                    {
                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "X.ndim <= 1"},
                                                    {
                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
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
                            {"XXX TODO XXX": "sp.isspmatrix(X)"},
                            {
                                "type": "object",
                                "properties": {"kernel": {"enum": ["precomputed"]}},
                            },
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "not hasattr(self, 'decision_function_shape')"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "decision_function_shape": {
                                                                "enum": ["ovr", "ovo"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "callable(self.kernel)"
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "y": {"enum": [None]}
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "y": {
                                                                "not": {
                                                                    "type": "string"
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "y": {
                                                                "not": {
                                                                    "enum": [
                                                                        "no_validation"
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
                                                                        "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
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
                                                            "decision_function_shape": {
                                                                "not": {
                                                                    "enum": [
                                                                        "ovr",
                                                                        "ovo",
                                                                    ]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "callable(self.kernel)"
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "y": {"enum": [None]}
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "y": {
                                                                "not": {
                                                                    "type": "string"
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "y": {
                                                                "not": {
                                                                    "enum": [
                                                                        "no_validation"
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
                                                                        "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim <= 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
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
                                        "XXX TODO XXX": "hasattr(self, 'decision_function_shape')"
                                    },
                                    {"XXX TODO XXX": "callable(self.kernel)"},
                                    {
                                        "type": "object",
                                        "properties": {"y": {"enum": [None]}},
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "y": {"not": {"type": "string"}}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "y": {"not": {"enum": ["no_validation"]}}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "X.ndim <= 1"},
                                                    {
                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "X.ndim <= 1"},
                                                    {
                                                        "XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
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
        "description": 'From /utils/validation.py:None:check_array, Exception: raise ValueError("""Complex data not supported {} """.format(array)     ) from complex_warning ',
        "anyOf": [
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"enum": [None]}}},
            {"type": "object", "properties": {"y": {"not": {"type": "string"}}}},
            {
                "type": "object",
                "properties": {"y": {"not": {"enum": ["no_validation"]}}},
            },
            {
                "allOf": [
                    {
                        "anyOf": [
                            {"XXX TODO XXX": "not hasattr(X, 'sparse')"},
                            {"XXX TODO XXX": "X.ndim <= 1"},
                            {"XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"},
                        ]
                    },
                    {
                        "anyOf": [
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'sparse')"},
                                    {"XXX TODO XXX": "X.ndim > 1"},
                                ]
                            },
                            {"XXX TODO XXX": "sp.issparse(X)"},
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": "From /utils/validation.py:None:check_array, Exception: raise ValueError('Found array with dim %d. %s expected <= 2.' % (array.ndim,     estimator_name)) ",
        "anyOf": [
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"enum": [None]}}},
            {"type": "object", "properties": {"y": {"not": {"type": "string"}}}},
            {
                "type": "object",
                "properties": {"y": {"not": {"enum": ["no_validation"]}}},
            },
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "X.ndim <= 1"},
                                            {
                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                            },
                                            {
                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).ndim < 3"
                                            },
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "X.ndim > 1"},
                                                ]
                                            },
                                            {"XXX TODO XXX": "sp.issparse(X)"},
                                            {
                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).ndim < 3"
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
                                "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "X.ndim <= 1"},
                                            {
                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                            },
                                            {
                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).ndim < 3"
                                            },
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "X.ndim > 1"},
                                                ]
                                            },
                                            {"XXX TODO XXX": "sp.issparse(X)"},
                                            {
                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).ndim < 3"
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
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"enum": [None]}}},
            {"type": "object", "properties": {"y": {"not": {"type": "string"}}}},
            {
                "type": "object",
                "properties": {"y": {"not": {"enum": ["no_validation"]}}},
            },
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "X.ndim <= 1"},
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "type": "object",
                                                                "laleNot": "X/isSparse",
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, False)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64)) >= 1"
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
                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "X.ndim > 1"},
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(X, order='C', dtype=np.float64)) >= 1"
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
                                "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "X.ndim <= 1"},
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "type": "object",
                                                                "laleNot": "X/isSparse",
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, False)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64)) >= 1"
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
                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "X.ndim > 1"},
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(X, order='C', dtype=np.float64)) >= 1"
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
        "description": "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Found array with %d feature(s) (shape=%s) while a minimum of %d is required%s.'      % (n_features, array.shape, ensure_min_features, context)) ",
        "anyOf": [
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"enum": [None]}}},
            {"type": "object", "properties": {"y": {"not": {"type": "string"}}}},
            {
                "type": "object",
                "properties": {"y": {"not": {"enum": ["no_validation"]}}},
            },
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "X.ndim <= 1"},
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "type": "object",
                                                                "laleNot": "X/isSparse",
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, False).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
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
                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "X.ndim > 1"},
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
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
                                "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "X.ndim <= 1"},
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "type": "object",
                                                                "laleNot": "X/isSparse",
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, False).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
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
                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "X.ndim > 1"},
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
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
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"enum": [None]}}},
            {
                "allOf": [
                    {"type": "object", "properties": {"y": {"type": "string"}}},
                    {
                        "type": "object",
                        "properties": {"y": {"enum": ["no_validation"]}},
                    },
                ]
            },
            {"XXX TODO XXX": "not hasattr(X, 'fit')"},
            {"XXX TODO XXX": "not callable(X.fit)"},
        ],
    },
    {
        "description": "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) ",
        "anyOf": [
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"enum": [None]}}},
            {
                "allOf": [
                    {"type": "object", "properties": {"y": {"type": "string"}}},
                    {
                        "type": "object",
                        "properties": {"y": {"enum": ["no_validation"]}},
                    },
                ]
            },
            {"XXX TODO XXX": "hasattr(X, '__len__')"},
            {"XXX TODO XXX": "hasattr(X, 'shape')"},
            {"XXX TODO XXX": "hasattr(X, '__array__')"},
        ],
    },
    {
        "description": "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(     'Singleton array %r cannot be considered a valid collection.' % x) ",
        "anyOf": [
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"enum": [None]}}},
            {
                "allOf": [
                    {"type": "object", "properties": {"y": {"type": "string"}}},
                    {
                        "type": "object",
                        "properties": {"y": {"enum": ["no_validation"]}},
                    },
                ]
            },
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
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"enum": [None]}}},
            {
                "allOf": [
                    {"type": "object", "properties": {"y": {"type": "string"}}},
                    {
                        "type": "object",
                        "properties": {"y": {"enum": ["no_validation"]}},
                    },
                ]
            },
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
        "description": "From /utils/validation.py:None:check_consistent_length, Exception: raise ValueError(     'Found input variables with inconsistent numbers of samples: %r' % [int     (l) for l in lengths]) ",
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "not sp.isspmatrix(X)"},
                    {
                        "type": "object",
                        "properties": {"kernel": {"not": {"enum": ["precomputed"]}}},
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "not hasattr(self, 'decision_function_shape')"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "decision_function_shape": {
                                                                "enum": ["ovr", "ovo"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "callable(self.kernel)"
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "y": {"enum": [None]}
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "y": {
                                                                        "type": "string"
                                                                    }
                                                                },
                                                            },
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "y": {
                                                                        "enum": [
                                                                            "no_validation"
                                                                        ]
                                                                    }
                                                                },
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "type": "object",
                                                                        "properties": {
                                                                            "y": {
                                                                                "not": {
                                                                                    "enum": [
                                                                                        None
                                                                                    ]
                                                                                }
                                                                            }
                                                                        },
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "type": "object",
                                                                        "properties": {
                                                                            "y": {
                                                                                "enum": [
                                                                                    None
                                                                                ]
                                                                            }
                                                                        },
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
                                                        "properties": {
                                                            "decision_function_shape": {
                                                                "not": {
                                                                    "enum": [
                                                                        "ovr",
                                                                        "ovo",
                                                                    ]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "callable(self.kernel)"
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "y": {"enum": [None]}
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "y": {
                                                                        "type": "string"
                                                                    }
                                                                },
                                                            },
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "y": {
                                                                        "enum": [
                                                                            "no_validation"
                                                                        ]
                                                                    }
                                                                },
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "type": "object",
                                                                        "properties": {
                                                                            "y": {
                                                                                "not": {
                                                                                    "enum": [
                                                                                        None
                                                                                    ]
                                                                                }
                                                                            }
                                                                        },
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "type": "object",
                                                                        "properties": {
                                                                            "y": {
                                                                                "enum": [
                                                                                    None
                                                                                ]
                                                                            }
                                                                        },
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
                                        "XXX TODO XXX": "hasattr(self, 'decision_function_shape')"
                                    },
                                    {"XXX TODO XXX": "callable(self.kernel)"},
                                    {
                                        "type": "object",
                                        "properties": {"y": {"enum": [None]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "type": "object",
                                                "properties": {"y": {"type": "string"}},
                                            },
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "y": {"enum": ["no_validation"]}
                                                },
                                            },
                                        ]
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "y": {
                                                                "not": {"enum": [None]}
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "y": {"enum": [None]}
                                                        },
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
                            {"XXX TODO XXX": "sp.isspmatrix(X)"},
                            {
                                "type": "object",
                                "properties": {"kernel": {"enum": ["precomputed"]}},
                            },
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "not hasattr(self, 'decision_function_shape')"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "decision_function_shape": {
                                                                "enum": ["ovr", "ovo"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "callable(self.kernel)"
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "y": {"enum": [None]}
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "y": {
                                                                        "type": "string"
                                                                    }
                                                                },
                                                            },
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "y": {
                                                                        "enum": [
                                                                            "no_validation"
                                                                        ]
                                                                    }
                                                                },
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "type": "object",
                                                                        "properties": {
                                                                            "y": {
                                                                                "not": {
                                                                                    "enum": [
                                                                                        None
                                                                                    ]
                                                                                }
                                                                            }
                                                                        },
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "type": "object",
                                                                        "properties": {
                                                                            "y": {
                                                                                "enum": [
                                                                                    None
                                                                                ]
                                                                            }
                                                                        },
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
                                                        "properties": {
                                                            "decision_function_shape": {
                                                                "not": {
                                                                    "enum": [
                                                                        "ovr",
                                                                        "ovo",
                                                                    ]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "callable(self.kernel)"
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "y": {"enum": [None]}
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "y": {
                                                                        "type": "string"
                                                                    }
                                                                },
                                                            },
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "y": {
                                                                        "enum": [
                                                                            "no_validation"
                                                                        ]
                                                                    }
                                                                },
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "type": "object",
                                                                        "properties": {
                                                                            "y": {
                                                                                "not": {
                                                                                    "enum": [
                                                                                        None
                                                                                    ]
                                                                                }
                                                                            }
                                                                        },
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "type": "object",
                                                                        "properties": {
                                                                            "y": {
                                                                                "enum": [
                                                                                    None
                                                                                ]
                                                                            }
                                                                        },
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
                                        "XXX TODO XXX": "hasattr(self, 'decision_function_shape')"
                                    },
                                    {"XXX TODO XXX": "callable(self.kernel)"},
                                    {
                                        "type": "object",
                                        "properties": {"y": {"enum": [None]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "type": "object",
                                                "properties": {"y": {"type": "string"}},
                                            },
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "y": {"enum": ["no_validation"]}
                                                },
                                            },
                                        ]
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "y": {
                                                                "not": {"enum": [None]}
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "y": {"enum": [None]}
                                                        },
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
        ],
    },
    {
        "description": "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) ",
        "anyOf": [
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"enum": [None]}}},
            {
                "allOf": [
                    {"type": "object", "properties": {"y": {"type": "string"}}},
                    {
                        "type": "object",
                        "properties": {"y": {"enum": ["no_validation"]}},
                    },
                ]
            },
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "X.ndim <= 1"},
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "type": "object",
                                                                "laleNot": "X/isSparse",
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, False), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, False).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).fit)"
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
                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "X.ndim > 1"},
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(X, order='C', dtype=np.float64).fit)"
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
                                "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "X.ndim <= 1"},
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "type": "object",
                                                                "laleNot": "X/isSparse",
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, False), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, False).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).fit)"
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
                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "X.ndim > 1"},
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(X, order='C', dtype=np.float64).fit)"
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
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"enum": [None]}}},
            {
                "allOf": [
                    {"type": "object", "properties": {"y": {"type": "string"}}},
                    {
                        "type": "object",
                        "properties": {"y": {"enum": ["no_validation"]}},
                    },
                ]
            },
            {
                "allOf": [
                    {
                        "anyOf": [
                            {"XXX TODO XXX": "not hasattr(X, 'sparse')"},
                            {"XXX TODO XXX": "X.ndim <= 1"},
                            {"type": "object", "laleNot": "X/isSparse"},
                            {"XXX TODO XXX": "not hasattr(X.sparse.to_coo(), 'dtype')"},
                            {"XXX TODO XXX": "X.sparse.to_coo().dtype is None"},
                            {
                                "XXX TODO XXX": "not hasattr(X.sparse.to_coo().dtype, 'kind')"
                            },
                            {"XXX TODO XXX": "X.sparse.to_coo().dtype.kind != 'c'"},
                        ]
                    },
                    {
                        "anyOf": [
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'sparse')"},
                                    {"XXX TODO XXX": "X.ndim > 1"},
                                ]
                            },
                            {"type": "object", "laleNot": "X/isSparse"},
                            {"XXX TODO XXX": "not hasattr(X, 'dtype')"},
                            {"XXX TODO XXX": "X.dtype is None"},
                            {"XXX TODO XXX": "not hasattr(X.dtype, 'kind')"},
                            {"XXX TODO XXX": "X.dtype.kind != 'c'"},
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": 'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) ',
        "anyOf": [
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"enum": [None]}}},
            {
                "allOf": [
                    {"type": "object", "properties": {"y": {"type": "string"}}},
                    {
                        "type": "object",
                        "properties": {"y": {"enum": ["no_validation"]}},
                    },
                ]
            },
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'dtypes')"
                                            },
                                            {
                                                "XXX TODO XXX": "not hasattr(X.dtypes, '__array__')"
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "not all((False for np.float64 in list(X.dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "X.ndim <= 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype.kind != 'c'"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "all((False for np.float64 in list(X.dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "X.ndim <= 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype.kind != 'c'"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype.kind != 'c'"
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
                                                        "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                    },
                                                ]
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "X.ndim <= 1"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype.kind != 'c'"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype.kind != 'c'"
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
                                "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'dtypes')"
                                            },
                                            {
                                                "XXX TODO XXX": "not hasattr(X.dtypes, '__array__')"
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "not all((False for np.float64 in list(X.dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "X.ndim <= 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype.kind != 'c'"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "all((False for np.float64 in list(X.dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "X.ndim <= 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype.kind != 'c'"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype.kind != 'c'"
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
                                                        "XXX TODO XXX": "hasattr(X, 'dtypes')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
                                                    },
                                                ]
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "X.ndim <= 1"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).dtype.kind != 'c'"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, order='C', dtype=np.float64).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).dtype.kind != 'c'"
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
        "description": "From /utils/validation.py:None:_check_large_sparse, Exception: raise ValueError(     'Only sparse matrices with 32-bit integer indices are accepted. Got %s indices.'      % indices_datatype) ",
        "anyOf": [
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"enum": [None]}}},
            {
                "allOf": [
                    {"type": "object", "properties": {"y": {"type": "string"}}},
                    {
                        "type": "object",
                        "properties": {"y": {"enum": ["no_validation"]}},
                    },
                ]
            },
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                    {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                ]
            },
            {
                "allOf": [
                    {
                        "anyOf": [
                            {"XXX TODO XXX": "not hasattr(X, 'sparse')"},
                            {"XXX TODO XXX": "X.ndim <= 1"},
                            {"type": "object", "laleNot": "X/isSparse"},
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "X.sparse.to_coo().getformat() != 'coo'"
                                            },
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "key": {
                                                        "not": {"enum": ["col", "row"]}
                                                    }
                                                },
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(X.sparse.to_coo(), key).dtype in ['int32']"
                                            },
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "X.sparse.to_coo().getformat() == 'coo'"
                                            },
                                            {
                                                "XXX TODO XXX": "X.sparse.to_coo().getformat() not in ['csr', 'csc', 'bsr']"
                                            },
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "key": {
                                                        "not": {
                                                            "enum": [
                                                                "indices",
                                                                "indptr",
                                                            ]
                                                        }
                                                    }
                                                },
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(X.sparse.to_coo(), key).dtype in ['int32']"
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
                                    {"XXX TODO XXX": "hasattr(X, 'sparse')"},
                                    {"XXX TODO XXX": "X.ndim > 1"},
                                ]
                            },
                            {"type": "object", "laleNot": "X/isSparse"},
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {"XXX TODO XXX": "X.getformat() != 'coo'"},
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "key": {
                                                        "not": {"enum": ["col", "row"]}
                                                    }
                                                },
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(X, key).dtype in ['int32']"
                                            },
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {"XXX TODO XXX": "X.getformat() == 'coo'"},
                                            {
                                                "XXX TODO XXX": "X.getformat() not in ['csr', 'csc', 'bsr']"
                                            },
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "key": {
                                                        "not": {
                                                            "enum": [
                                                                "indices",
                                                                "indptr",
                                                            ]
                                                        }
                                                    }
                                                },
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(X, key).dtype in ['int32']"
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
        "description": 'From /utils/validation.py:None:check_array, Exception: raise ValueError("""Complex data not supported {} """.format(array)     ) from complex_warning ',
        "anyOf": [
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"enum": [None]}}},
            {
                "allOf": [
                    {"type": "object", "properties": {"y": {"type": "string"}}},
                    {
                        "type": "object",
                        "properties": {"y": {"enum": ["no_validation"]}},
                    },
                ]
            },
            {
                "allOf": [
                    {
                        "anyOf": [
                            {"XXX TODO XXX": "not hasattr(X, 'sparse')"},
                            {"XXX TODO XXX": "X.ndim <= 1"},
                            {"XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"},
                        ]
                    },
                    {
                        "anyOf": [
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'sparse')"},
                                    {"XXX TODO XXX": "X.ndim > 1"},
                                ]
                            },
                            {"XXX TODO XXX": "sp.issparse(X)"},
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": "From /utils/validation.py:None:check_array, Exception: raise ValueError('Found array with dim %d. %s expected <= 2.' % (array.ndim,     estimator_name)) ",
        "anyOf": [
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"enum": [None]}}},
            {
                "allOf": [
                    {"type": "object", "properties": {"y": {"type": "string"}}},
                    {
                        "type": "object",
                        "properties": {"y": {"enum": ["no_validation"]}},
                    },
                ]
            },
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "X.ndim <= 1"},
                                            {
                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                            },
                                            {
                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).ndim < 3"
                                            },
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "X.ndim > 1"},
                                                ]
                                            },
                                            {"XXX TODO XXX": "sp.issparse(X)"},
                                            {
                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).ndim < 3"
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
                                "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "X.ndim <= 1"},
                                            {
                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                            },
                                            {
                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).ndim < 3"
                                            },
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "X.ndim > 1"},
                                                ]
                                            },
                                            {"XXX TODO XXX": "sp.issparse(X)"},
                                            {
                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).ndim < 3"
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
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"enum": [None]}}},
            {
                "allOf": [
                    {"type": "object", "properties": {"y": {"type": "string"}}},
                    {
                        "type": "object",
                        "properties": {"y": {"enum": ["no_validation"]}},
                    },
                ]
            },
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "X.ndim <= 1"},
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "type": "object",
                                                                "laleNot": "X/isSparse",
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, False)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64)) >= 1"
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
                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "X.ndim > 1"},
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(X, order='C', dtype=np.float64)) >= 1"
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
                                "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "X.ndim <= 1"},
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "type": "object",
                                                                "laleNot": "X/isSparse",
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, False)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64)) >= 1"
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
                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "X.ndim > 1"},
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(X, order='C', dtype=np.float64)) >= 1"
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
        "description": "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Found array with %d feature(s) (shape=%s) while a minimum of %d is required%s.'      % (n_features, array.shape, ensure_min_features, context)) ",
        "anyOf": [
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"enum": [None]}}},
            {
                "allOf": [
                    {"type": "object", "properties": {"y": {"type": "string"}}},
                    {
                        "type": "object",
                        "properties": {"y": {"enum": ["no_validation"]}},
                    },
                ]
            },
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "X.ndim <= 1"},
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "type": "object",
                                                                "laleNot": "X/isSparse",
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, False).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
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
                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "X.ndim > 1"},
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
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
                                "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(X, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "X.ndim <= 1"},
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "type": "object",
                                                                "laleNot": "X/isSparse",
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, False).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
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
                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "X.ndim > 1"},
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
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
        "description": "From /utils/validation.py:None:column_or_1d, Exception: raise ValueError('y should be a 1d array, got an array of shape {} instead.'     .format(shape)) ",
        "anyOf": [
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"enum": [None]}}},
            {
                "allOf": [
                    {"type": "object", "properties": {"y": {"type": "string"}}},
                    {
                        "type": "object",
                        "properties": {"y": {"enum": ["no_validation"]}},
                    },
                ]
            },
        ],
    },
    {
        "description": "From /utils/validation.py:None:_assert_all_finite, Exception: raise ValueError(msg_err.format(type_err, msg_dtype if msg_dtype is not     None else X.dtype)) ",
        "anyOf": [
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"enum": [None]}}},
            {
                "allOf": [
                    {"type": "object", "properties": {"y": {"type": "string"}}},
                    {
                        "type": "object",
                        "properties": {"y": {"enum": ["no_validation"]}},
                    },
                ]
            },
            {"XXX TODO XXX": "_get_config()['assume_finite']"},
            {
                "allOf": [
                    {"XXX TODO XXX": "y.dtype.kind in 'fc'"},
                    {"XXX TODO XXX": "np.isfinite(_safe_accumulator_op(np.sum, y))"},
                ]
            },
            {"XXX TODO XXX": "y.dtype.kind not in 'fc'"},
            {"XXX TODO XXX": "np.isfinite(y).all()"},
        ],
    },
    {
        "description": "From /utils/validation.py:None:_assert_all_finite, Exception: raise ValueError('Input contains NaN') ",
        "anyOf": [
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"enum": [None]}}},
            {
                "allOf": [
                    {"type": "object", "properties": {"y": {"type": "string"}}},
                    {
                        "type": "object",
                        "properties": {"y": {"enum": ["no_validation"]}},
                    },
                ]
            },
            {"XXX TODO XXX": "_get_config()['assume_finite']"},
            {
                "allOf": [
                    {"XXX TODO XXX": "y.dtype.kind in 'fc'"},
                    {"XXX TODO XXX": "np.isfinite(_safe_accumulator_op(np.sum, y))"},
                ]
            },
            {"XXX TODO XXX": "y.dtype.kind in 'fc'"},
            {"XXX TODO XXX": "y.dtype != np.dtype('object')"},
            {"XXX TODO XXX": "not _object_dtype_isnan(y).any()"},
        ],
    },
    {
        "description": "From /utils/validation.py:None:check_X_y, Exception: raise ValueError('y cannot be None') ",
        "anyOf": [
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"enum": [None]}}},
            {
                "allOf": [
                    {"type": "object", "properties": {"y": {"type": "string"}}},
                    {
                        "type": "object",
                        "properties": {"y": {"enum": ["no_validation"]}},
                    },
                ]
            },
            {"type": "object", "properties": {"y": {"not": {"enum": [None]}}}},
        ],
    },
    {
        "description": "From /base.py:BaseEstimator:_validate_data, Exception: raise ValueError(     f'This {self.__class__.__name__} estimator requires y to be passed, but the target y is None.'     ) ",
        "anyOf": [
            {"XXX TODO XXX": "callable(self.kernel)"},
            {"type": "object", "properties": {"y": {"not": {"enum": [None]}}}},
            {"XXX TODO XXX": "not self._get_tags()['requires_y']"},
        ],
    },
    {
        "description": "From /utils/validation.py:None:_assert_all_finite, Exception: raise ValueError(msg_err.format(type_err, msg_dtype if msg_dtype is not     None else X.dtype)) ",
        "anyOf": [
            {"XXX TODO XXX": "is_multilabel(y)"},
            {"XXX TODO XXX": "y.ndim > 2"},
            {
                "allOf": [
                    {"XXX TODO XXX": "y.dtype == object"},
                    {"XXX TODO XXX": "len(y)"},
                    {"XXX TODO XXX": "isinstance(y.flat[0], str)"},
                ]
            },
            {
                "allOf": [
                    {"XXX TODO XXX": "y.ndim == 2"},
                    {"XXX TODO XXX": "y.shape[1] == 0"},
                ]
            },
            {"XXX TODO XXX": "y.dtype.kind != 'f'"},
            {"XXX TODO XXX": "not np.any(y != y.astype(int))"},
            {"XXX TODO XXX": "_get_config()['assume_finite']"},
            {
                "allOf": [
                    {"XXX TODO XXX": "y.dtype.kind in 'fc'"},
                    {"XXX TODO XXX": "np.isfinite(_safe_accumulator_op(np.sum, y))"},
                ]
            },
            {"XXX TODO XXX": "y.dtype.kind not in 'fc'"},
            {"XXX TODO XXX": "np.isfinite(y).all()"},
        ],
    },
    {
        "description": "From /utils/validation.py:None:_assert_all_finite, Exception: raise ValueError('Input contains NaN') ",
        "anyOf": [
            {"XXX TODO XXX": "is_multilabel(y)"},
            {"XXX TODO XXX": "y.ndim > 2"},
            {
                "allOf": [
                    {"XXX TODO XXX": "y.dtype == object"},
                    {"XXX TODO XXX": "len(y)"},
                    {"XXX TODO XXX": "isinstance(y.flat[0], str)"},
                ]
            },
            {
                "allOf": [
                    {"XXX TODO XXX": "y.ndim == 2"},
                    {"XXX TODO XXX": "y.shape[1] == 0"},
                ]
            },
            {"XXX TODO XXX": "y.dtype.kind != 'f'"},
            {"XXX TODO XXX": "not np.any(y != y.astype(int))"},
            {"XXX TODO XXX": "_get_config()['assume_finite']"},
            {
                "allOf": [
                    {"XXX TODO XXX": "y.dtype.kind in 'fc'"},
                    {"XXX TODO XXX": "np.isfinite(_safe_accumulator_op(np.sum, y))"},
                ]
            },
            {"XXX TODO XXX": "y.dtype.kind in 'fc'"},
            {"XXX TODO XXX": "y.dtype != np.dtype('object')"},
            {"XXX TODO XXX": "not _object_dtype_isnan(y).any()"},
        ],
    },
    {
        "description": "From /utils/multiclass.py:None:type_of_target, Exception: raise ValueError(     'Expected array-like (array or non-string sequence), got %r' % y) ",
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "isinstance(y, [Sequence, spmatrix])"},
                    {"XXX TODO XXX": "hasattr(y, '__array__')"},
                ]
            },
            {"type": "object", "properties": {"y": {"not": {"type": "string"}}}},
        ],
    },
    {
        "description": "From /utils/multiclass.py:None:type_of_target, Exception: raise ValueError(\"y cannot be class 'SparseSeries' or 'SparseArray'\") ",
        "XXX TODO XXX": "y.__class__.__name__ not in ['SparseSeries', 'SparseArray']",
    },
    {
        "description": "From /utils/multiclass.py:None:type_of_target, Exception: raise ValueError(     'You appear to be using a legacy multi-label data representation. Sequence of sequences are no longer supported; use a binary array or sparse matrix instead - the MultiLabelBinarizer transformer can convert to this format.'     ) ",
        "anyOf": [
            {"XXX TODO XXX": "is_multilabel(y)"},
            {"XXX TODO XXX": "hasattr(y[0], '__array__')"},
            {"XXX TODO XXX": "isinstance(y[0], Sequence)"},
            {"XXX TODO XXX": "isinstance(y[0], str)"},
        ],
    },
    {
        "description": "From /utils/multiclass.py:None:check_classification_targets, Exception: raise ValueError('Unknown label type: %r' % y_type) ",
        "XXX TODO XXX": "type_of_target(y) in ['binary', 'multiclass', 'multiclass-multioutput', 'multilabel-indicator', 'multilabel-sequences']",
    },
    {
        "description": "From /utils/class_weight.py:None:compute_class_weight, Exception: raise ValueError('classes should include all valid labels that can be in y') ",
        "XXX TODO XXX": "not set(column_or_1d(y, True)) - set(np.unique(y_, return_inverse=True)[0])",
    },
    {
        "description": "From /utils/class_weight.py:None:compute_class_weight, Exception: raise ValueError('classes should have valid labels that are in y') ",
        "anyOf": [
            {"type": "object", "properties": {"class_weight": {"enum": [None]}}},
            {"XXX TODO XXX": "len(self.class_weight) == 0"},
            {
                "type": "object",
                "properties": {"class_weight": {"not": {"enum": ["balanced"]}}},
            },
            {
                "XXX TODO XXX": "all(np.in1d(np.unique(y_, return_inverse=True)[0], LabelEncoder().classes_))"
            },
        ],
    },
    {
        "description": "From /utils/class_weight.py:None:compute_class_weight, Exception: raise ValueError(\"class_weight must be dict, 'balanced', or None, got: %r\" %     class_weight) ",
        "anyOf": [
            {"type": "object", "properties": {"class_weight": {"enum": [None]}}},
            {"XXX TODO XXX": "len(self.class_weight) == 0"},
            {"type": "object", "properties": {"class_weight": {"enum": ["balanced"]}}},
            {"XXX TODO XXX": "isinstance(self.class_weight, dict)"},
        ],
    },
    {
        "description": "From /utils/class_weight.py:None:compute_class_weight, Exception: raise ValueError('Class label {} not present.'.format(c)) ",
        "anyOf": [
            {"type": "object", "properties": {"class_weight": {"enum": [None]}}},
            {"XXX TODO XXX": "len(self.class_weight) == 0"},
            {"type": "object", "properties": {"class_weight": {"enum": ["balanced"]}}},
            {"XXX TODO XXX": "c not in self.class_weight"},
            {
                "allOf": [
                    {
                        "XXX TODO XXX": "np.searchsorted(np.unique(y_, return_inverse=True)[0], c) < len(np.unique(y_, return_inverse=True)[0])"
                    },
                    {"XXX TODO XXX": "classes[i] == c"},
                ]
            },
        ],
    },
    {
        "description": "From /svm/_base.py:BaseSVC:_validate_targets, Exception: raise ValueError(     'The number of classes has to be greater than one; got %d class' % len(cls)     ) ",
        "XXX TODO XXX": "len(np.unique(y_, return_inverse=True)[0]) >= 2",
    },
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
        "description": "From /svm/_base.py:BaseLibSVM:_dense_fit, Exception: raise ValueError('X.shape[0] should be equal to X.shape[1]') ",
        "anyOf": [
            {"XXX TODO XXX": "not callable(self.kernel)"},
            {"XXX TODO XXX": "X.shape[0] == X.shape[1]"},
        ],
    },
    {
        "description": "From /svm/_base.py:BaseLibSVM:fit, Exception: raise TypeError('Sparse precomputed kernels are not supported.') ",
        "anyOf": [
            {"XXX TODO XXX": "not sp.isspmatrix(X)"},
            {
                "type": "object",
                "properties": {"kernel": {"not": {"enum": ["precomputed"]}}},
            },
        ],
    },
    {
        "description": "From /svm/_base.py:BaseLibSVM:fit, Exception: raise ValueError(     f\"decision_function_shape must be either 'ovr' or 'ovo', got {self.decision_function_shape}.\"     ) ",
        "anyOf": [
            {"XXX TODO XXX": "not hasattr(self, 'decision_function_shape')"},
            {
                "type": "object",
                "properties": {"decision_function_shape": {"enum": ["ovr", "ovo"]}},
            },
        ],
    },
    {
        "description": "From /svm/_base.py:BaseLibSVM:fit, Exception: raise ValueError('X and y have incompatible shapes.\\n' +      'X has %s samples, but y has %s.' % (n_samples, y.shape[0])) ",
        "anyOf": [
            {"XXX TODO XXX": "LIBSVM_IMPL.index(self._impl) == 2"},
            {"XXX TODO XXX": "_num_samples(X) == y.shape[0]"},
        ],
    },
    {
        "description": "From /svm/_base.py:BaseLibSVM:fit, Exception: raise ValueError(     'Precomputed matrix must be a square matrix. Input is a {}x{} matrix.'.     format(X.shape[0], X.shape[1])) ",
        "anyOf": [
            {
                "type": "object",
                "properties": {"kernel": {"not": {"enum": ["precomputed"]}}},
            },
            {"XXX TODO XXX": "_num_samples(X) == X.shape[1]"},
        ],
    },
    {
        "description": 'From /svm/_base.py:BaseLibSVM:fit, Exception: raise ValueError(     """sample_weight and X have incompatible shapes: %r vs %r Note: Sparse matrices cannot be indexed w/boolean masks (use `indices=True` in CV)."""      % (sample_weight.shape, X.shape)) ',
        "anyOf": [
            {"XXX TODO XXX": "sample_weight.shape[0] <= 0"},
            {"XXX TODO XXX": "sample_weight.shape[0] == _num_samples(X)"},
        ],
    },
    {
        "description": "From /svm/_base.py:BaseLibSVM:fit, Exception: raise ValueError(     \"When 'gamma' is a string, it should be either 'scale' or 'auto'. Got '{}' instead.\"     .format(self.gamma)) ",
        "anyOf": [
            {
                "XXX TODO XXX": "('precomputed' if callable(self.kernel) else self.kernel) == 'precomputed'"
            },
            {"type": "object", "properties": {"gamma": {"not": {"type": "string"}}}},
            {"type": "object", "properties": {"gamma": {"enum": ["scale"]}}},
            {"type": "object", "properties": {"gamma": {"enum": ["auto"]}}},
        ],
    },
]
