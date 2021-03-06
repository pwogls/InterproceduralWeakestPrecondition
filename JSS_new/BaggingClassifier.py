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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), None, None).fit)"
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(X, None, None).fit)"
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), None, None).fit)"
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(X, None, None).fit)"
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
                                                                "XXX TODO XXX": "not all((False for None in list(X.dtypes)))"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype.kind != 'c'"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "all((False for None in list(X.dtypes)))"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype.kind != 'c'"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "not all((False for None in list(X.dtypes)))"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype.kind != 'c'"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "all((False for None in list(X.dtypes)))"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype.kind != 'c'"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype.kind != 'c'"
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
        "description": "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Pandas DataFrame with mixed sparse extension arrays generated a sparse matrix with object dtype which can not be converted to a scipy sparse matrix.Sparse extension arrays should all have the same numeric type.'     ) ",
        "anyOf": [
            {"type": "object", "properties": {"y": {"not": {"enum": [None]}}}},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {"XXX TODO XXX": "not self._get_tags()['requires_y']"},
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
                    {
                        "anyOf": [
                            {"XXX TODO XXX": "self._get_tags()['requires_y']"},
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
        ],
    },
    {
        "description": 'From /utils/validation.py:None:check_array, Exception: raise ValueError("""Complex data not supported {} """.format(array)     ) from complex_warning ',
        "anyOf": [
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
                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).ndim < 3"
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
                                                "XXX TODO XXX": "np.asarray(X, None, None).ndim < 3"
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
                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).ndim < 3"
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
                                                "XXX TODO XXX": "np.asarray(X, None, None).ndim < 3"
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), None, None)) >= 1"
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(X, None, None)) >= 1"
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), None, None)) >= 1"
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(X, None, None)) >= 1"
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True).ndim != 2"
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
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).ndim != 2"
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True).ndim != 2"
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
                                                                "XXX TODO XXX": "np.asarray(X, None, None).ndim != 2"
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True).ndim != 2"
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
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).ndim != 2"
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True).ndim != 2"
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
                                                                "XXX TODO XXX": "np.asarray(X, None, None).ndim != 2"
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), None, None).fit)"
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(X, None, None).fit)"
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), None, None).fit)"
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(X, None, None).fit)"
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
                                                                "XXX TODO XXX": "not all((False for None in list(X.dtypes)))"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype.kind != 'c'"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "all((False for None in list(X.dtypes)))"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype.kind != 'c'"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "not all((False for None in list(X.dtypes)))"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype.kind != 'c'"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "all((False for None in list(X.dtypes)))"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype.kind != 'c'"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype.kind != 'c'"
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
        "description": "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Pandas DataFrame with mixed sparse extension arrays generated a sparse matrix with object dtype which can not be converted to a scipy sparse matrix.Sparse extension arrays should all have the same numeric type.'     ) ",
        "anyOf": [
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
                            {"XXX TODO XXX": "not hasattr(X, 'sparse')"},
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
                                    {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                                ]
                            },
                            {"XXX TODO XXX": "not hasattr(X, 'sparse')"},
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
        ],
    },
    {
        "description": 'From /utils/validation.py:None:check_array, Exception: raise ValueError("""Complex data not supported {} """.format(array)     ) from complex_warning ',
        "anyOf": [
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
                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).ndim < 3"
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
                                                "XXX TODO XXX": "np.asarray(X, None, None).ndim < 3"
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
                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).ndim < 3"
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
                                                "XXX TODO XXX": "np.asarray(X, None, None).ndim < 3"
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), None, None)) >= 1"
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(X, None, None)) >= 1"
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), None, None)) >= 1"
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(X, None, None)) >= 1"
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True).ndim != 2"
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
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).ndim != 2"
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True).ndim != 2"
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
                                                                "XXX TODO XXX": "np.asarray(X, None, None).ndim != 2"
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True).ndim != 2"
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
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).ndim != 2"
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True).ndim != 2"
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
                                                                "XXX TODO XXX": "np.asarray(X, None, None).ndim != 2"
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), None, None).fit)"
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(X, None, None).fit)"
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), None, None).fit)"
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(X, None, None).fit)"
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
                                                                "XXX TODO XXX": "not all((False for None in list(X.dtypes)))"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype.kind != 'c'"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "all((False for None in list(X.dtypes)))"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype.kind != 'c'"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "not all((False for None in list(X.dtypes)))"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype.kind != 'c'"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "all((False for None in list(X.dtypes)))"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype.kind != 'c'"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, None).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, None).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, None, None).dtype.kind != 'c'"
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
                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).ndim < 3"
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
                                                "XXX TODO XXX": "np.asarray(X, None, None).ndim < 3"
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
                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).ndim < 3"
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
                                                "XXX TODO XXX": "np.asarray(X, None, None).ndim < 3"
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), None, None)) >= 1"
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(X, None, None)) >= 1"
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), None, None)) >= 1"
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(X, None, None)) >= 1"
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True).ndim != 2"
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
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).ndim != 2"
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True).ndim != 2"
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
                                                                "XXX TODO XXX": "np.asarray(X, None, None).ndim != 2"
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True).ndim != 2"
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
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).ndim != 2"
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True).ndim != 2"
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
                                                                "XXX TODO XXX": "np.asarray(X, None, None).ndim != 2"
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
                                "XXX TODO XXX": "hasattr(getattr(y, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(y, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(y.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(y, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "y.ndim <= 1"},
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "type": "object",
                                                                "laleNot": "X/isSparse",
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(y.sparse.to_coo(), accept_sparse='csr', None, False, True, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(y.sparse.to_coo(), accept_sparse='csr', None, False, True, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(y.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, None), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(y.sparse.to_coo(), None, None).fit)"
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
                                                        "XXX TODO XXX": "hasattr(y, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "y.ndim > 1"},
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(y, accept_sparse='csr', None, False, True, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(y, accept_sparse='csr', None, False, True, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(y)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(y, None, None), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(y, None, None).fit)"
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
                                "XXX TODO XXX": "not hasattr(getattr(y, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(y, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(y.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(y, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "y.ndim <= 1"},
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "type": "object",
                                                                "laleNot": "X/isSparse",
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(y.sparse.to_coo(), accept_sparse='csr', None, False, True, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(y.sparse.to_coo(), accept_sparse='csr', None, False, True, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(y.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, None), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(y.sparse.to_coo(), None, None).fit)"
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
                                                        "XXX TODO XXX": "hasattr(y, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "y.ndim > 1"},
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(y, accept_sparse='csr', None, False, True, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(y, accept_sparse='csr', None, False, True, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(y)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(y, None, None), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(y, None, None).fit)"
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
                            {"XXX TODO XXX": "not hasattr(y, 'sparse')"},
                            {"XXX TODO XXX": "y.ndim <= 1"},
                            {"type": "object", "laleNot": "X/isSparse"},
                            {"XXX TODO XXX": "not hasattr(y.sparse.to_coo(), 'dtype')"},
                            {"XXX TODO XXX": "y.sparse.to_coo().dtype is None"},
                            {
                                "XXX TODO XXX": "not hasattr(y.sparse.to_coo().dtype, 'kind')"
                            },
                            {"XXX TODO XXX": "y.sparse.to_coo().dtype.kind != 'c'"},
                        ]
                    },
                    {
                        "anyOf": [
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(y, 'sparse')"},
                                    {"XXX TODO XXX": "y.ndim > 1"},
                                ]
                            },
                            {"type": "object", "laleNot": "X/isSparse"},
                            {"XXX TODO XXX": "not hasattr(y, 'dtype')"},
                            {"XXX TODO XXX": "y.dtype is None"},
                            {"XXX TODO XXX": "not hasattr(y.dtype, 'kind')"},
                            {"XXX TODO XXX": "y.dtype.kind != 'c'"},
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": 'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) ',
        "anyOf": [
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
                                "XXX TODO XXX": "hasattr(getattr(y, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(y, 'dtypes')"
                                            },
                                            {
                                                "XXX TODO XXX": "not hasattr(y.dtypes, '__array__')"
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "not all((False for None in list(y.dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(y, 'sparse')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "y.ndim <= 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(y.sparse.to_coo())"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, None).dtype.kind != 'c'"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "hasattr(y, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "y.ndim > 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(y)"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(y, None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(y, None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(y, None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(y, None, None).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "all((False for None in list(y.dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(y, 'sparse')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "y.ndim <= 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(y.sparse.to_coo())"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, None).dtype.kind != 'c'"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "hasattr(y, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "y.ndim > 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(y)"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(y, None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(y, None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(y, None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(y, None, None).dtype.kind != 'c'"
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
                                                        "XXX TODO XXX": "hasattr(y, 'dtypes')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(y.dtypes, '__array__')"
                                                    },
                                                ]
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "not hasattr(y, 'sparse')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "y.ndim <= 1"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(y.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, None), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, None).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, None).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, None).dtype.kind != 'c'"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(y, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "y.ndim > 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(y)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(y, None, None), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(y, None, None).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(y, None, None).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(y, None, None).dtype.kind != 'c'"
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
                                "XXX TODO XXX": "not hasattr(getattr(y, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(y, 'dtypes')"
                                            },
                                            {
                                                "XXX TODO XXX": "not hasattr(y.dtypes, '__array__')"
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "not all((False for None in list(y.dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(y, 'sparse')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "y.ndim <= 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(y.sparse.to_coo())"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, None).dtype.kind != 'c'"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "hasattr(y, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "y.ndim > 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(y)"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(y, None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(y, None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(y, None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(y, None, None).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "all((False for None in list(y.dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(y, 'sparse')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "y.ndim <= 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(y.sparse.to_coo())"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, None).dtype.kind != 'c'"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "hasattr(y, 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "y.ndim > 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(y)"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(y, None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(y, None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(y, None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(y, None, None).dtype.kind != 'c'"
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
                                                        "XXX TODO XXX": "hasattr(y, 'dtypes')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(y.dtypes, '__array__')"
                                                    },
                                                ]
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "not hasattr(y, 'sparse')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "y.ndim <= 1"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(y.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, None), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, None).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, None).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, None).dtype.kind != 'c'"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(y, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "y.ndim > 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(y)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(y, None, None), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(y, None, None).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(y, None, None).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(y, None, None).dtype.kind != 'c'"
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
        "description": "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Pandas DataFrame with mixed sparse extension arrays generated a sparse matrix with object dtype which can not be converted to a scipy sparse matrix.Sparse extension arrays should all have the same numeric type.'     ) ",
        "anyOf": [
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
                                "type": "object",
                                "properties": {"y": {"not": {"enum": [None]}}},
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "hasattr(getattr(y, 'dtype', None), 'kind')"
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(y, 'dtypes')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(y.dtypes, '__array__')"
                                                    },
                                                ]
                                            },
                                            {
                                                "XXX TODO XXX": "not hasattr(y, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "y.ndim <= 1"},
                                            {
                                                "XXX TODO XXX": "y.sparse.to_coo().dtype != np.dtype('object')"
                                            },
                                            {
                                                "XXX TODO XXX": "len(set([dt.subtype.name for dt in y.dtypes])) <= 1"
                                            },
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(getattr(y, 'dtype', None), 'kind')"
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(y, 'dtypes')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(y.dtypes, '__array__')"
                                                    },
                                                ]
                                            },
                                            {
                                                "XXX TODO XXX": "not hasattr(y, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "y.ndim <= 1"},
                                            {
                                                "XXX TODO XXX": "y.sparse.to_coo().dtype != np.dtype('object')"
                                            },
                                            {
                                                "XXX TODO XXX": "len(set([dt.subtype.name for dt in y.dtypes])) <= 1"
                                            },
                                        ]
                                    },
                                ]
                            },
                        ]
                    },
                    {
                        "anyOf": [
                            {"type": "object", "properties": {"y": {"enum": [None]}}},
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "hasattr(getattr(y, 'dtype', None), 'kind')"
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(y, 'dtypes')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(y.dtypes, '__array__')"
                                                    },
                                                ]
                                            },
                                            {
                                                "XXX TODO XXX": "not hasattr(y, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "y.ndim <= 1"},
                                            {
                                                "XXX TODO XXX": "y.sparse.to_coo().dtype != np.dtype('object')"
                                            },
                                            {
                                                "XXX TODO XXX": "len(set([dt.subtype.name for dt in y.dtypes])) <= 1"
                                            },
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(getattr(y, 'dtype', None), 'kind')"
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(y, 'dtypes')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(y.dtypes, '__array__')"
                                                    },
                                                ]
                                            },
                                            {
                                                "XXX TODO XXX": "not hasattr(y, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "y.ndim <= 1"},
                                            {
                                                "XXX TODO XXX": "y.sparse.to_coo().dtype != np.dtype('object')"
                                            },
                                            {
                                                "XXX TODO XXX": "len(set([dt.subtype.name for dt in y.dtypes])) <= 1"
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
                            {"XXX TODO XXX": "not hasattr(y, 'sparse')"},
                            {"XXX TODO XXX": "y.ndim <= 1"},
                            {"XXX TODO XXX": "sp.issparse(y.sparse.to_coo())"},
                        ]
                    },
                    {
                        "anyOf": [
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(y, 'sparse')"},
                                    {"XXX TODO XXX": "y.ndim > 1"},
                                ]
                            },
                            {"XXX TODO XXX": "sp.issparse(y)"},
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": "From /utils/validation.py:None:check_array, Exception: raise ValueError('Found array with dim %d. %s expected <= 2.' % (array.ndim,     estimator_name)) ",
        "anyOf": [
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
                                "XXX TODO XXX": "hasattr(getattr(y, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(y, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(y.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(y, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "y.ndim <= 1"},
                                            {
                                                "XXX TODO XXX": "sp.issparse(y.sparse.to_coo())"
                                            },
                                            {
                                                "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, None).ndim < 3"
                                            },
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(y, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "y.ndim > 1"},
                                                ]
                                            },
                                            {"XXX TODO XXX": "sp.issparse(y)"},
                                            {
                                                "XXX TODO XXX": "np.asarray(y, None, None).ndim < 3"
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
                                "XXX TODO XXX": "not hasattr(getattr(y, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(y, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(y.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(y, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "y.ndim <= 1"},
                                            {
                                                "XXX TODO XXX": "sp.issparse(y.sparse.to_coo())"
                                            },
                                            {
                                                "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, None).ndim < 3"
                                            },
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(y, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "y.ndim > 1"},
                                                ]
                                            },
                                            {"XXX TODO XXX": "sp.issparse(y)"},
                                            {
                                                "XXX TODO XXX": "np.asarray(y, None, None).ndim < 3"
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
                                "XXX TODO XXX": "hasattr(getattr(y, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(y, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(y.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(y, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "y.ndim <= 1"},
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "type": "object",
                                                                "laleNot": "X/isSparse",
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(y.sparse.to_coo(), accept_sparse='csr', None, False, True, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(y.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(y.sparse.to_coo(), None, None)) >= 1"
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
                                                        "XXX TODO XXX": "hasattr(y, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "y.ndim > 1"},
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(y, accept_sparse='csr', None, False, True, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(y)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(y, None, None)) >= 1"
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
                                "XXX TODO XXX": "not hasattr(getattr(y, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(y, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(y.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(y, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "y.ndim <= 1"},
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "type": "object",
                                                                "laleNot": "X/isSparse",
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(y.sparse.to_coo(), accept_sparse='csr', None, False, True, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(y.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(y.sparse.to_coo(), None, None)) >= 1"
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
                                                        "XXX TODO XXX": "hasattr(y, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "y.ndim > 1"},
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(y, accept_sparse='csr', None, False, True, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(y)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(y, None, None)) >= 1"
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
                                "XXX TODO XXX": "hasattr(getattr(y, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(y, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(y.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(y, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "y.ndim <= 1"},
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "type": "object",
                                                                "laleNot": "X/isSparse",
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_ensure_sparse_format(y.sparse.to_coo(), accept_sparse='csr', None, False, True, True).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(y.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, None).ndim != 2"
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
                                                        "XXX TODO XXX": "hasattr(y, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "y.ndim > 1"},
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(y, accept_sparse='csr', None, False, True, True).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(y)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(y, None, None).ndim != 2"
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
                                "XXX TODO XXX": "not hasattr(getattr(y, 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {"XXX TODO XXX": "hasattr(y, 'dtypes')"},
                                    {"XXX TODO XXX": "hasattr(y.dtypes, '__array__')"},
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(y, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "y.ndim <= 1"},
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "type": "object",
                                                                "laleNot": "X/isSparse",
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_ensure_sparse_format(y.sparse.to_coo(), accept_sparse='csr', None, False, True, True).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(y.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, None).ndim != 2"
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
                                                        "XXX TODO XXX": "hasattr(y, 'sparse')"
                                                    },
                                                    {"XXX TODO XXX": "y.ndim > 1"},
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(y, accept_sparse='csr', None, False, True, True).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(y)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(y, None, None).ndim != 2"
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
        "anyOf": [
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
                                "type": "object",
                                "properties": {"y": {"not": {"enum": [None]}}},
                            },
                            {
                                "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
                            },
                        ]
                    },
                    {
                        "anyOf": [
                            {"type": "object", "properties": {"y": {"enum": [None]}}},
                            {
                                "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
                            },
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": "From /utils/validation.py:None:check_X_y, Exception: raise ValueError('y cannot be None') ",
        "anyOf": [
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
            {"type": "object", "properties": {"y": {"not": {"enum": [None]}}}},
            {"XXX TODO XXX": "not self._get_tags()['requires_y']"},
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
        "description": "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Pandas DataFrame with mixed sparse extension arrays generated a sparse matrix with object dtype which can not be converted to a scipy sparse matrix.Sparse extension arrays should all have the same numeric type.'     ) ",
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
                            {"XXX TODO XXX": "not hasattr(sample_weight, 'sparse')"},
                            {"XXX TODO XXX": "sample_weight.ndim <= 1"},
                            {
                                "XXX TODO XXX": "sample_weight.sparse.to_coo().dtype != np.dtype('object')"
                            },
                            {
                                "XXX TODO XXX": "len(set([dt.subtype.name for dt in sample_weight.dtypes])) <= 1"
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
                                                "XXX TODO XXX": "not hasattr(sample_weight, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "sample_weight.ndim <= 1"},
                                            {
                                                "XXX TODO XXX": "sample_weight.sparse.to_coo().dtype != np.dtype('object')"
                                            },
                                            {
                                                "XXX TODO XXX": "len(set([dt.subtype.name for dt in sample_weight.dtypes])) <= 1"
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
                                                "XXX TODO XXX": "not hasattr(sample_weight, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "sample_weight.ndim <= 1"},
                                            {
                                                "XXX TODO XXX": "sample_weight.sparse.to_coo().dtype != np.dtype('object')"
                                            },
                                            {
                                                "XXX TODO XXX": "len(set([dt.subtype.name for dt in sample_weight.dtypes])) <= 1"
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
        "description": "From /ensemble/_base.py:BaseEnsemble:_validate_estimator, Exception: raise ValueError('n_estimators must be an integer, got {0}.'.format(type(     self.n_estimators))) ",
        "type": "object",
        "properties": {"n_estimators": {"type": "integer"}},
    },
    {
        "description": "From /ensemble/_base.py:BaseEnsemble:_validate_estimator, Exception: raise ValueError('n_estimators must be greater than zero, got {0}.'.format(     self.n_estimators)) ",
        "type": "object",
        "properties": {
            "n_estimators": {"type": "number", "minimum": 0, "exclusiveMinimum": True}
        },
    },
    {
        "description": "From /ensemble/_base.py:BaseEnsemble:_validate_estimator, Exception: raise ValueError('base_estimator cannot be None') ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "type": "object",
                        "properties": {"base_estimator": {"enum": [None]}},
                    },
                    {
                        "type": "object",
                        "properties": {"base_estimator": {"not": {"enum": [None]}}},
                    },
                ]
            },
            {
                "anyOf": [
                    {
                        "type": "object",
                        "properties": {"base_estimator": {"not": {"enum": [None]}}},
                    },
                    {"XXX TODO XXX": "DecisionTreeClassifier() is not None"},
                ]
            },
        ],
    },
    {
        "description": "From /utils/__init__.py:None:indices_to_mask, Exception: raise ValueError('mask_length must be greater than max(indices)') ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "type": "object",
                        "properties": {"sample_weight": {"enum": [None]}},
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "allOf": [
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "warm_start": {"enum": [True]}
                                                },
                                            },
                                            {
                                                "XXX TODO XXX": "hasattr(self, 'estimators_')"
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
                                                            "n_estimators": {
                                                                "type": "number",
                                                                "minimum": 0,
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "oob_score": {
                                                                "enum": [False]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "[estimator, samples, features] not in zip([] + list(itertools.chain.from_iterable((t[0] for t in Parallel(n_jobs=_partition_estimators(n_more_estimators, self.n_jobs)[0], verbose=self.verbose, **self._parallel_args())((delayed(_parallel_build_estimators)(n_estimators[i], self, X, y, _check_sample_weight(sample_weight, X, None), seeds[starts[i]:starts[i + 1]], sum(_partition_estimators(n_more_estimators, self.n_jobs)[1]), verbose=self.verbose) for i in range(_partition_estimators(n_more_estimators, self.n_jobs)[0])))))), self.estimators_samples_, [] + list(itertools.chain.from_iterable((t[1] for t in Parallel(n_jobs=_partition_estimators(n_more_estimators, self.n_jobs)[0], verbose=self.verbose, **self._parallel_args())((delayed(_parallel_build_estimators)(n_estimators[i], self, X, y, _check_sample_weight(sample_weight, X, None), seeds[starts[i]:starts[i + 1]], sum(_partition_estimators(n_more_estimators, self.n_jobs)[1]), verbose=self.verbose) for i in range(_partition_estimators(n_more_estimators, self.n_jobs)[0])))))))"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "y.shape[0] > np.max(samples)"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "n_estimators": {
                                                                "type": "number",
                                                                "maximum": 0,
                                                                "exclusiveMaximum": True,
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "n_estimators": {
                                                                "enum": [0]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "oob_score": {
                                                                "enum": [False]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "[estimator, samples, features] not in zip([] + list(itertools.chain.from_iterable((t[0] for t in Parallel(n_jobs=_partition_estimators(n_more_estimators, self.n_jobs)[0], verbose=self.verbose, **self._parallel_args())((delayed(_parallel_build_estimators)(n_estimators[i], self, X, y, _check_sample_weight(sample_weight, X, None), seeds[starts[i]:starts[i + 1]], sum(_partition_estimators(n_more_estimators, self.n_jobs)[1]), verbose=self.verbose) for i in range(_partition_estimators(n_more_estimators, self.n_jobs)[0])))))), self.estimators_samples_, [] + list(itertools.chain.from_iterable((t[1] for t in Parallel(n_jobs=_partition_estimators(n_more_estimators, self.n_jobs)[0], verbose=self.verbose, **self._parallel_args())((delayed(_parallel_build_estimators)(n_estimators[i], self, X, y, _check_sample_weight(sample_weight, X, None), seeds[starts[i]:starts[i + 1]], sum(_partition_estimators(n_more_estimators, self.n_jobs)[1]), verbose=self.verbose) for i in range(_partition_estimators(n_more_estimators, self.n_jobs)[0])))))))"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "y.shape[0] > np.max(samples)"
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
                                        "properties": {"warm_start": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "not hasattr(self, 'estimators_')"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) >= 0"
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "oob_score": {
                                                                "enum": [False]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "[estimator, samples, features] not in zip(self.estimators_ + list(itertools.chain.from_iterable((t[0] for t in Parallel(n_jobs=_partition_estimators(n_more_estimators, self.n_jobs)[0], verbose=self.verbose, **self._parallel_args())((delayed(_parallel_build_estimators)(n_estimators[i], self, X, y, _check_sample_weight(sample_weight, X, None), seeds[starts[i]:starts[i + 1]], sum(_partition_estimators(n_more_estimators, self.n_jobs)[1]), verbose=self.verbose) for i in range(_partition_estimators(n_more_estimators, self.n_jobs)[0])))))), self.estimators_samples_, self.estimators_features_ + list(itertools.chain.from_iterable((t[1] for t in Parallel(n_jobs=_partition_estimators(n_more_estimators, self.n_jobs)[0], verbose=self.verbose, **self._parallel_args())((delayed(_parallel_build_estimators)(n_estimators[i], self, X, y, _check_sample_weight(sample_weight, X, None), seeds[starts[i]:starts[i + 1]], sum(_partition_estimators(n_more_estimators, self.n_jobs)[1]), verbose=self.verbose) for i in range(_partition_estimators(n_more_estimators, self.n_jobs)[0])))))))"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "y.shape[0] > np.max(samples)"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) < 0"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) == 0"
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "oob_score": {
                                                                "enum": [False]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "[estimator, samples, features] not in zip(self.estimators_ + list(itertools.chain.from_iterable((t[0] for t in Parallel(n_jobs=_partition_estimators(n_more_estimators, self.n_jobs)[0], verbose=self.verbose, **self._parallel_args())((delayed(_parallel_build_estimators)(n_estimators[i], self, X, y, _check_sample_weight(sample_weight, X, None), seeds[starts[i]:starts[i + 1]], sum(_partition_estimators(n_more_estimators, self.n_jobs)[1]), verbose=self.verbose) for i in range(_partition_estimators(n_more_estimators, self.n_jobs)[0])))))), self.estimators_samples_, self.estimators_features_ + list(itertools.chain.from_iterable((t[1] for t in Parallel(n_jobs=_partition_estimators(n_more_estimators, self.n_jobs)[0], verbose=self.verbose, **self._parallel_args())((delayed(_parallel_build_estimators)(n_estimators[i], self, X, y, _check_sample_weight(sample_weight, X, None), seeds[starts[i]:starts[i + 1]], sum(_partition_estimators(n_more_estimators, self.n_jobs)[1]), verbose=self.verbose) for i in range(_partition_estimators(n_more_estimators, self.n_jobs)[0])))))))"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "y.shape[0] > np.max(samples)"
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
                        "properties": {"sample_weight": {"not": {"enum": [None]}}},
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "allOf": [
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "warm_start": {"enum": [True]}
                                                },
                                            },
                                            {
                                                "XXX TODO XXX": "hasattr(self, 'estimators_')"
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
                                                            "n_estimators": {
                                                                "type": "number",
                                                                "minimum": 0,
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "oob_score": {
                                                                "enum": [False]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "[estimator, samples, features] not in zip([] + list(itertools.chain.from_iterable((t[0] for t in Parallel(n_jobs=_partition_estimators(n_more_estimators, self.n_jobs)[0], verbose=self.verbose, **self._parallel_args())((delayed(_parallel_build_estimators)(n_estimators[i], self, X, y, sample_weight, seeds[starts[i]:starts[i + 1]], sum(_partition_estimators(n_more_estimators, self.n_jobs)[1]), verbose=self.verbose) for i in range(_partition_estimators(n_more_estimators, self.n_jobs)[0])))))), self.estimators_samples_, [] + list(itertools.chain.from_iterable((t[1] for t in Parallel(n_jobs=_partition_estimators(n_more_estimators, self.n_jobs)[0], verbose=self.verbose, **self._parallel_args())((delayed(_parallel_build_estimators)(n_estimators[i], self, X, y, sample_weight, seeds[starts[i]:starts[i + 1]], sum(_partition_estimators(n_more_estimators, self.n_jobs)[1]), verbose=self.verbose) for i in range(_partition_estimators(n_more_estimators, self.n_jobs)[0])))))))"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "y.shape[0] > np.max(samples)"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "n_estimators": {
                                                                "type": "number",
                                                                "maximum": 0,
                                                                "exclusiveMaximum": True,
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "n_estimators": {
                                                                "enum": [0]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "oob_score": {
                                                                "enum": [False]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "[estimator, samples, features] not in zip([] + list(itertools.chain.from_iterable((t[0] for t in Parallel(n_jobs=_partition_estimators(n_more_estimators, self.n_jobs)[0], verbose=self.verbose, **self._parallel_args())((delayed(_parallel_build_estimators)(n_estimators[i], self, X, y, sample_weight, seeds[starts[i]:starts[i + 1]], sum(_partition_estimators(n_more_estimators, self.n_jobs)[1]), verbose=self.verbose) for i in range(_partition_estimators(n_more_estimators, self.n_jobs)[0])))))), self.estimators_samples_, [] + list(itertools.chain.from_iterable((t[1] for t in Parallel(n_jobs=_partition_estimators(n_more_estimators, self.n_jobs)[0], verbose=self.verbose, **self._parallel_args())((delayed(_parallel_build_estimators)(n_estimators[i], self, X, y, sample_weight, seeds[starts[i]:starts[i + 1]], sum(_partition_estimators(n_more_estimators, self.n_jobs)[1]), verbose=self.verbose) for i in range(_partition_estimators(n_more_estimators, self.n_jobs)[0])))))))"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "y.shape[0] > np.max(samples)"
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
                                        "properties": {"warm_start": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "not hasattr(self, 'estimators_')"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) >= 0"
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "oob_score": {
                                                                "enum": [False]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "[estimator, samples, features] not in zip(self.estimators_ + list(itertools.chain.from_iterable((t[0] for t in Parallel(n_jobs=_partition_estimators(n_more_estimators, self.n_jobs)[0], verbose=self.verbose, **self._parallel_args())((delayed(_parallel_build_estimators)(n_estimators[i], self, X, y, sample_weight, seeds[starts[i]:starts[i + 1]], sum(_partition_estimators(n_more_estimators, self.n_jobs)[1]), verbose=self.verbose) for i in range(_partition_estimators(n_more_estimators, self.n_jobs)[0])))))), self.estimators_samples_, self.estimators_features_ + list(itertools.chain.from_iterable((t[1] for t in Parallel(n_jobs=_partition_estimators(n_more_estimators, self.n_jobs)[0], verbose=self.verbose, **self._parallel_args())((delayed(_parallel_build_estimators)(n_estimators[i], self, X, y, sample_weight, seeds[starts[i]:starts[i + 1]], sum(_partition_estimators(n_more_estimators, self.n_jobs)[1]), verbose=self.verbose) for i in range(_partition_estimators(n_more_estimators, self.n_jobs)[0])))))))"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "y.shape[0] > np.max(samples)"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) < 0"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) == 0"
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "oob_score": {
                                                                "enum": [False]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "[estimator, samples, features] not in zip(self.estimators_ + list(itertools.chain.from_iterable((t[0] for t in Parallel(n_jobs=_partition_estimators(n_more_estimators, self.n_jobs)[0], verbose=self.verbose, **self._parallel_args())((delayed(_parallel_build_estimators)(n_estimators[i], self, X, y, sample_weight, seeds[starts[i]:starts[i + 1]], sum(_partition_estimators(n_more_estimators, self.n_jobs)[1]), verbose=self.verbose) for i in range(_partition_estimators(n_more_estimators, self.n_jobs)[0])))))), self.estimators_samples_, self.estimators_features_ + list(itertools.chain.from_iterable((t[1] for t in Parallel(n_jobs=_partition_estimators(n_more_estimators, self.n_jobs)[0], verbose=self.verbose, **self._parallel_args())((delayed(_parallel_build_estimators)(n_estimators[i], self, X, y, sample_weight, seeds[starts[i]:starts[i + 1]], sum(_partition_estimators(n_more_estimators, self.n_jobs)[1]), verbose=self.verbose) for i in range(_partition_estimators(n_more_estimators, self.n_jobs)[0])))))))"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "y.shape[0] > np.max(samples)"
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
        "allOf": [
            {
                "anyOf": [
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'estimators_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "minimum": 0,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "not hasattr(X, 'fit')"},
                                    {"XXX TODO XXX": "not callable(X.fit)"},
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "maximum": 0,
                                                "exclusiveMaximum": True,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"n_estimators": {"enum": [0]}},
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "not hasattr(X, 'fit')"},
                                    {"XXX TODO XXX": "not callable(X.fit)"},
                                ]
                            },
                        ]
                    },
                ]
            },
            {
                "anyOf": [
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'estimators_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) >= 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "not hasattr(X, 'fit')"},
                                    {"XXX TODO XXX": "not callable(X.fit)"},
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) < 0"
                                    },
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) == 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "not hasattr(X, 'fit')"},
                                    {"XXX TODO XXX": "not callable(X.fit)"},
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
        "allOf": [
            {
                "anyOf": [
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'estimators_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "minimum": 0,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "hasattr(X, '__len__')"},
                                    {"XXX TODO XXX": "hasattr(X, 'shape')"},
                                    {"XXX TODO XXX": "hasattr(X, '__array__')"},
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "maximum": 0,
                                                "exclusiveMaximum": True,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"n_estimators": {"enum": [0]}},
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "hasattr(X, '__len__')"},
                                    {"XXX TODO XXX": "hasattr(X, 'shape')"},
                                    {"XXX TODO XXX": "hasattr(X, '__array__')"},
                                ]
                            },
                        ]
                    },
                ]
            },
            {
                "anyOf": [
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'estimators_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) >= 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "hasattr(X, '__len__')"},
                                    {"XXX TODO XXX": "hasattr(X, 'shape')"},
                                    {"XXX TODO XXX": "hasattr(X, '__array__')"},
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) < 0"
                                    },
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) == 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "hasattr(X, '__len__')"},
                                    {"XXX TODO XXX": "hasattr(X, 'shape')"},
                                    {"XXX TODO XXX": "hasattr(X, '__array__')"},
                                ]
                            },
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(     'Singleton array %r cannot be considered a valid collection.' % x) ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'estimators_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "minimum": 0,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, '__len__')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, 'shape')"
                                                    },
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
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, '__array__')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.shape is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(X.shape) != 0"
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
                                                                "XXX TODO XXX": "not hasattr(X, '__len__')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                    },
                                                    {"XXX TODO XXX": "X.shape is None"},
                                                    {
                                                        "XXX TODO XXX": "len(X.shape) != 0"
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
                                            "n_estimators": {
                                                "type": "number",
                                                "maximum": 0,
                                                "exclusiveMaximum": True,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"n_estimators": {"enum": [0]}},
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, '__len__')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, 'shape')"
                                                    },
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
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, '__array__')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.shape is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(X.shape) != 0"
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
                                                                "XXX TODO XXX": "not hasattr(X, '__len__')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                    },
                                                    {"XXX TODO XXX": "X.shape is None"},
                                                    {
                                                        "XXX TODO XXX": "len(X.shape) != 0"
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
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'estimators_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) >= 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, '__len__')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, 'shape')"
                                                    },
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
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, '__array__')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.shape is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(X.shape) != 0"
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
                                                                "XXX TODO XXX": "not hasattr(X, '__len__')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                    },
                                                    {"XXX TODO XXX": "X.shape is None"},
                                                    {
                                                        "XXX TODO XXX": "len(X.shape) != 0"
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
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) < 0"
                                    },
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) == 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, '__len__')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, 'shape')"
                                                    },
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
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, '__array__')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.shape is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(X.shape) != 0"
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
                                                                "XXX TODO XXX": "not hasattr(X, '__len__')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                    },
                                                    {"XXX TODO XXX": "X.shape is None"},
                                                    {
                                                        "XXX TODO XXX": "len(X.shape) != 0"
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
        "description": "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) from type_error ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'estimators_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "minimum": 0,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, '__len__')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, 'shape')"
                                                    },
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
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, '__array__')"
                                                                    },
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
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, '__len__')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                            },
                                                        ]
                                                    },
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
                                            {
                                                "XXX TODO XXX": "isinstance(x.shape[0], numbers.Integral)"
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
                                            "n_estimators": {
                                                "type": "number",
                                                "maximum": 0,
                                                "exclusiveMaximum": True,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"n_estimators": {"enum": [0]}},
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, '__len__')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, 'shape')"
                                                    },
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
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, '__array__')"
                                                                    },
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
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, '__len__')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                            },
                                                        ]
                                                    },
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
                                            {
                                                "XXX TODO XXX": "isinstance(x.shape[0], numbers.Integral)"
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
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'estimators_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) >= 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, '__len__')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, 'shape')"
                                                    },
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
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, '__array__')"
                                                                    },
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
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, '__len__')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                            },
                                                        ]
                                                    },
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
                                            {
                                                "XXX TODO XXX": "isinstance(x.shape[0], numbers.Integral)"
                                            },
                                        ]
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) < 0"
                                    },
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) == 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, '__len__')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, 'shape')"
                                                    },
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
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, '__array__')"
                                                                    },
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
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, '__len__')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                            },
                                                        ]
                                                    },
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
                                            {
                                                "XXX TODO XXX": "isinstance(x.shape[0], numbers.Integral)"
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
        "allOf": [
            {
                "anyOf": [
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'estimators_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "minimum": 0,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))} != {'binary', 'multiclass'}"
                                            },
                                            {
                                                "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))}.pop() not in ['binary', 'multiclass']"
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
                                            "n_estimators": {
                                                "type": "number",
                                                "maximum": 0,
                                                "exclusiveMaximum": True,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"n_estimators": {"enum": [0]}},
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))} != {'binary', 'multiclass'}"
                                            },
                                            {
                                                "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))}.pop() not in ['binary', 'multiclass']"
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
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'estimators_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) >= 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))} != {'binary', 'multiclass'}"
                                            },
                                            {
                                                "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))}.pop() not in ['binary', 'multiclass']"
                                            },
                                        ]
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) < 0"
                                    },
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) == 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))} != {'binary', 'multiclass'}"
                                            },
                                            {
                                                "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))}.pop() not in ['binary', 'multiclass']"
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
        "allOf": [
            {
                "anyOf": [
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'estimators_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "minimum": 0,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))} != {'binary', 'multiclass'}"
                                            },
                                            {
                                                "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))}.pop() not in ['binary', 'multiclass']"
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
                                            "n_estimators": {
                                                "type": "number",
                                                "maximum": 0,
                                                "exclusiveMaximum": True,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"n_estimators": {"enum": [0]}},
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))} != {'binary', 'multiclass'}"
                                            },
                                            {
                                                "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))}.pop() not in ['binary', 'multiclass']"
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
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'estimators_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) >= 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))} != {'binary', 'multiclass'}"
                                            },
                                            {
                                                "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))}.pop() not in ['binary', 'multiclass']"
                                            },
                                        ]
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) < 0"
                                    },
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) == 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))} != {'binary', 'multiclass'}"
                                            },
                                            {
                                                "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))}.pop() not in ['binary', 'multiclass']"
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
        "allOf": [
            {
                "anyOf": [
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'estimators_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "minimum": 0,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "not hasattr(X, 'fit')"},
                                    {"XXX TODO XXX": "not callable(X.fit)"},
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "maximum": 0,
                                                "exclusiveMaximum": True,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"n_estimators": {"enum": [0]}},
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "not hasattr(X, 'fit')"},
                                    {"XXX TODO XXX": "not callable(X.fit)"},
                                ]
                            },
                        ]
                    },
                ]
            },
            {
                "anyOf": [
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'estimators_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) >= 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "not hasattr(X, 'fit')"},
                                    {"XXX TODO XXX": "not callable(X.fit)"},
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) < 0"
                                    },
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) == 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "not hasattr(X, 'fit')"},
                                    {"XXX TODO XXX": "not callable(X.fit)"},
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
        "allOf": [
            {
                "anyOf": [
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'estimators_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "minimum": 0,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "hasattr(X, '__len__')"},
                                    {"XXX TODO XXX": "hasattr(X, 'shape')"},
                                    {"XXX TODO XXX": "hasattr(X, '__array__')"},
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "maximum": 0,
                                                "exclusiveMaximum": True,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"n_estimators": {"enum": [0]}},
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "hasattr(X, '__len__')"},
                                    {"XXX TODO XXX": "hasattr(X, 'shape')"},
                                    {"XXX TODO XXX": "hasattr(X, '__array__')"},
                                ]
                            },
                        ]
                    },
                ]
            },
            {
                "anyOf": [
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'estimators_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) >= 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "hasattr(X, '__len__')"},
                                    {"XXX TODO XXX": "hasattr(X, 'shape')"},
                                    {"XXX TODO XXX": "hasattr(X, '__array__')"},
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) < 0"
                                    },
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) == 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "hasattr(X, '__len__')"},
                                    {"XXX TODO XXX": "hasattr(X, 'shape')"},
                                    {"XXX TODO XXX": "hasattr(X, '__array__')"},
                                ]
                            },
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(     'Singleton array %r cannot be considered a valid collection.' % x) ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'estimators_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "minimum": 0,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, '__len__')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, 'shape')"
                                                    },
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
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, '__array__')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.shape is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(X.shape) != 0"
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
                                                                "XXX TODO XXX": "not hasattr(X, '__len__')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                    },
                                                    {"XXX TODO XXX": "X.shape is None"},
                                                    {
                                                        "XXX TODO XXX": "len(X.shape) != 0"
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
                                            "n_estimators": {
                                                "type": "number",
                                                "maximum": 0,
                                                "exclusiveMaximum": True,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"n_estimators": {"enum": [0]}},
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, '__len__')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, 'shape')"
                                                    },
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
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, '__array__')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.shape is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(X.shape) != 0"
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
                                                                "XXX TODO XXX": "not hasattr(X, '__len__')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                    },
                                                    {"XXX TODO XXX": "X.shape is None"},
                                                    {
                                                        "XXX TODO XXX": "len(X.shape) != 0"
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
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'estimators_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) >= 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, '__len__')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, 'shape')"
                                                    },
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
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, '__array__')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.shape is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(X.shape) != 0"
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
                                                                "XXX TODO XXX": "not hasattr(X, '__len__')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                    },
                                                    {"XXX TODO XXX": "X.shape is None"},
                                                    {
                                                        "XXX TODO XXX": "len(X.shape) != 0"
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
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) < 0"
                                    },
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) == 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, '__len__')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, 'shape')"
                                                    },
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
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, '__array__')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.shape is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "len(X.shape) != 0"
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
                                                                "XXX TODO XXX": "not hasattr(X, '__len__')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                    },
                                                    {"XXX TODO XXX": "X.shape is None"},
                                                    {
                                                        "XXX TODO XXX": "len(X.shape) != 0"
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
        "description": "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) from type_error ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'estimators_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "minimum": 0,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, '__len__')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, 'shape')"
                                                    },
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
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, '__array__')"
                                                                    },
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
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, '__len__')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                            },
                                                        ]
                                                    },
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
                                            {
                                                "XXX TODO XXX": "isinstance(x.shape[0], numbers.Integral)"
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
                                            "n_estimators": {
                                                "type": "number",
                                                "maximum": 0,
                                                "exclusiveMaximum": True,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"n_estimators": {"enum": [0]}},
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, '__len__')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, 'shape')"
                                                    },
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
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, '__array__')"
                                                                    },
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
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, '__len__')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                            },
                                                        ]
                                                    },
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
                                            {
                                                "XXX TODO XXX": "isinstance(x.shape[0], numbers.Integral)"
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
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'estimators_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) >= 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, '__len__')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, 'shape')"
                                                    },
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
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, '__array__')"
                                                                    },
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
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, '__len__')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                            },
                                                        ]
                                                    },
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
                                            {
                                                "XXX TODO XXX": "isinstance(x.shape[0], numbers.Integral)"
                                            },
                                        ]
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) < 0"
                                    },
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) == 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, '__len__')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, 'shape')"
                                                    },
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
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, '__array__')"
                                                                    },
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
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, '__len__')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(X, 'shape')"
                                                            },
                                                        ]
                                                    },
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
                                            {
                                                "XXX TODO XXX": "isinstance(x.shape[0], numbers.Integral)"
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
        "description": "From /utils/validation.py:None:_assert_all_finite, Exception: raise ValueError(msg_err.format(type_err, msg_dtype if msg_dtype is not     None else X.dtype)) ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'estimators_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "minimum": 0,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "is_multilabel(y)"},
                                    {"XXX TODO XXX": "y.ndim > 2"},
                                    {
                                        "allOf": [
                                            {"XXX TODO XXX": "y.dtype == object"},
                                            {"XXX TODO XXX": "len(y)"},
                                            {
                                                "XXX TODO XXX": "isinstance(y.flat[0], str)"
                                            },
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
                                            {
                                                "XXX TODO XXX": "np.isfinite(_safe_accumulator_op(np.sum, y))"
                                            },
                                        ]
                                    },
                                    {"XXX TODO XXX": "y.dtype.kind not in 'fc'"},
                                    {"XXX TODO XXX": "np.isfinite(y).all()"},
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "maximum": 0,
                                                "exclusiveMaximum": True,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"n_estimators": {"enum": [0]}},
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "is_multilabel(y)"},
                                    {"XXX TODO XXX": "y.ndim > 2"},
                                    {
                                        "allOf": [
                                            {"XXX TODO XXX": "y.dtype == object"},
                                            {"XXX TODO XXX": "len(y)"},
                                            {
                                                "XXX TODO XXX": "isinstance(y.flat[0], str)"
                                            },
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
                                            {
                                                "XXX TODO XXX": "np.isfinite(_safe_accumulator_op(np.sum, y))"
                                            },
                                        ]
                                    },
                                    {"XXX TODO XXX": "y.dtype.kind not in 'fc'"},
                                    {"XXX TODO XXX": "np.isfinite(y).all()"},
                                ]
                            },
                        ]
                    },
                ]
            },
            {
                "anyOf": [
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'estimators_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) >= 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "is_multilabel(y)"},
                                    {"XXX TODO XXX": "y.ndim > 2"},
                                    {
                                        "allOf": [
                                            {"XXX TODO XXX": "y.dtype == object"},
                                            {"XXX TODO XXX": "len(y)"},
                                            {
                                                "XXX TODO XXX": "isinstance(y.flat[0], str)"
                                            },
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
                                            {
                                                "XXX TODO XXX": "np.isfinite(_safe_accumulator_op(np.sum, y))"
                                            },
                                        ]
                                    },
                                    {"XXX TODO XXX": "y.dtype.kind not in 'fc'"},
                                    {"XXX TODO XXX": "np.isfinite(y).all()"},
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) < 0"
                                    },
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) == 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "is_multilabel(y)"},
                                    {"XXX TODO XXX": "y.ndim > 2"},
                                    {
                                        "allOf": [
                                            {"XXX TODO XXX": "y.dtype == object"},
                                            {"XXX TODO XXX": "len(y)"},
                                            {
                                                "XXX TODO XXX": "isinstance(y.flat[0], str)"
                                            },
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
                                            {
                                                "XXX TODO XXX": "np.isfinite(_safe_accumulator_op(np.sum, y))"
                                            },
                                        ]
                                    },
                                    {"XXX TODO XXX": "y.dtype.kind not in 'fc'"},
                                    {"XXX TODO XXX": "np.isfinite(y).all()"},
                                ]
                            },
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": "From /utils/validation.py:None:_assert_all_finite, Exception: raise ValueError('Input contains NaN') ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'estimators_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "minimum": 0,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "is_multilabel(y)"},
                                    {"XXX TODO XXX": "y.ndim > 2"},
                                    {
                                        "allOf": [
                                            {"XXX TODO XXX": "y.dtype == object"},
                                            {"XXX TODO XXX": "len(y)"},
                                            {
                                                "XXX TODO XXX": "isinstance(y.flat[0], str)"
                                            },
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
                                            {
                                                "XXX TODO XXX": "np.isfinite(_safe_accumulator_op(np.sum, y))"
                                            },
                                        ]
                                    },
                                    {"XXX TODO XXX": "y.dtype.kind in 'fc'"},
                                    {"XXX TODO XXX": "y.dtype != np.dtype('object')"},
                                    {
                                        "XXX TODO XXX": "not _object_dtype_isnan(y).any()"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "maximum": 0,
                                                "exclusiveMaximum": True,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"n_estimators": {"enum": [0]}},
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "is_multilabel(y)"},
                                    {"XXX TODO XXX": "y.ndim > 2"},
                                    {
                                        "allOf": [
                                            {"XXX TODO XXX": "y.dtype == object"},
                                            {"XXX TODO XXX": "len(y)"},
                                            {
                                                "XXX TODO XXX": "isinstance(y.flat[0], str)"
                                            },
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
                                            {
                                                "XXX TODO XXX": "np.isfinite(_safe_accumulator_op(np.sum, y))"
                                            },
                                        ]
                                    },
                                    {"XXX TODO XXX": "y.dtype.kind in 'fc'"},
                                    {"XXX TODO XXX": "y.dtype != np.dtype('object')"},
                                    {
                                        "XXX TODO XXX": "not _object_dtype_isnan(y).any()"
                                    },
                                ]
                            },
                        ]
                    },
                ]
            },
            {
                "anyOf": [
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'estimators_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) >= 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "is_multilabel(y)"},
                                    {"XXX TODO XXX": "y.ndim > 2"},
                                    {
                                        "allOf": [
                                            {"XXX TODO XXX": "y.dtype == object"},
                                            {"XXX TODO XXX": "len(y)"},
                                            {
                                                "XXX TODO XXX": "isinstance(y.flat[0], str)"
                                            },
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
                                            {
                                                "XXX TODO XXX": "np.isfinite(_safe_accumulator_op(np.sum, y))"
                                            },
                                        ]
                                    },
                                    {"XXX TODO XXX": "y.dtype.kind in 'fc'"},
                                    {"XXX TODO XXX": "y.dtype != np.dtype('object')"},
                                    {
                                        "XXX TODO XXX": "not _object_dtype_isnan(y).any()"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) < 0"
                                    },
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) == 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "is_multilabel(y)"},
                                    {"XXX TODO XXX": "y.ndim > 2"},
                                    {
                                        "allOf": [
                                            {"XXX TODO XXX": "y.dtype == object"},
                                            {"XXX TODO XXX": "len(y)"},
                                            {
                                                "XXX TODO XXX": "isinstance(y.flat[0], str)"
                                            },
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
                                            {
                                                "XXX TODO XXX": "np.isfinite(_safe_accumulator_op(np.sum, y))"
                                            },
                                        ]
                                    },
                                    {"XXX TODO XXX": "y.dtype.kind in 'fc'"},
                                    {"XXX TODO XXX": "y.dtype != np.dtype('object')"},
                                    {
                                        "XXX TODO XXX": "not _object_dtype_isnan(y).any()"
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
        "description": "From /utils/multiclass.py:None:type_of_target, Exception: raise ValueError(     'Expected array-like (array or non-string sequence), got %r' % y) ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'estimators_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "minimum": 0,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "isinstance(y, [Sequence, spmatrix])"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(y, '__array__')"
                                                    },
                                                ]
                                            },
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "y": {"not": {"type": "string"}}
                                                },
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
                                            "n_estimators": {
                                                "type": "number",
                                                "maximum": 0,
                                                "exclusiveMaximum": True,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"n_estimators": {"enum": [0]}},
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "isinstance(y, [Sequence, spmatrix])"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(y, '__array__')"
                                                    },
                                                ]
                                            },
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "y": {"not": {"type": "string"}}
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
            {
                "anyOf": [
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'estimators_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) >= 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "isinstance(y, [Sequence, spmatrix])"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(y, '__array__')"
                                                    },
                                                ]
                                            },
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "y": {"not": {"type": "string"}}
                                                },
                                            },
                                        ]
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) < 0"
                                    },
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) == 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "isinstance(y, [Sequence, spmatrix])"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(y, '__array__')"
                                                    },
                                                ]
                                            },
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "y": {"not": {"type": "string"}}
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
        "description": "From /utils/multiclass.py:None:type_of_target, Exception: raise ValueError(\"y cannot be class 'SparseSeries' or 'SparseArray'\") ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'estimators_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "minimum": 0,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "y.__class__.__name__ not in ['SparseSeries', 'SparseArray']"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "maximum": 0,
                                                "exclusiveMaximum": True,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"n_estimators": {"enum": [0]}},
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "y.__class__.__name__ not in ['SparseSeries', 'SparseArray']"
                                    },
                                ]
                            },
                        ]
                    },
                ]
            },
            {
                "anyOf": [
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'estimators_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) >= 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "y.__class__.__name__ not in ['SparseSeries', 'SparseArray']"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) < 0"
                                    },
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) == 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "y.__class__.__name__ not in ['SparseSeries', 'SparseArray']"
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
        "description": "From /utils/multiclass.py:None:type_of_target, Exception: raise ValueError(     'You appear to be using a legacy multi-label data representation. Sequence of sequences are no longer supported; use a binary array or sparse matrix instead - the MultiLabelBinarizer transformer can convert to this format.'     ) ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'estimators_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "minimum": 0,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "is_multilabel(y)"},
                                    {"XXX TODO XXX": "hasattr(y[0], '__array__')"},
                                    {"XXX TODO XXX": "isinstance(y[0], Sequence)"},
                                    {"XXX TODO XXX": "isinstance(y[0], str)"},
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "maximum": 0,
                                                "exclusiveMaximum": True,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"n_estimators": {"enum": [0]}},
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "is_multilabel(y)"},
                                    {"XXX TODO XXX": "hasattr(y[0], '__array__')"},
                                    {"XXX TODO XXX": "isinstance(y[0], Sequence)"},
                                    {"XXX TODO XXX": "isinstance(y[0], str)"},
                                ]
                            },
                        ]
                    },
                ]
            },
            {
                "anyOf": [
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'estimators_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) >= 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "is_multilabel(y)"},
                                    {"XXX TODO XXX": "hasattr(y[0], '__array__')"},
                                    {"XXX TODO XXX": "isinstance(y[0], Sequence)"},
                                    {"XXX TODO XXX": "isinstance(y[0], str)"},
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) < 0"
                                    },
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) == 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "is_multilabel(y)"},
                                    {"XXX TODO XXX": "hasattr(y[0], '__array__')"},
                                    {"XXX TODO XXX": "isinstance(y[0], Sequence)"},
                                    {"XXX TODO XXX": "isinstance(y[0], str)"},
                                ]
                            },
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": "From /utils/validation.py:None:_assert_all_finite, Exception: raise ValueError(msg_err.format(type_err, msg_dtype if msg_dtype is not     None else X.dtype)) ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'estimators_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "minimum": 0,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "is_multilabel(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))"
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).ndim > 2"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype == object"
                                            },
                                            {
                                                "XXX TODO XXX": "len(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))"
                                            },
                                            {
                                                "XXX TODO XXX": "isinstance(y.flat[0], str)"
                                            },
                                        ]
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).ndim == 2"
                                            },
                                            {"XXX TODO XXX": "y.shape[1] == 0"},
                                        ]
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype.kind != 'f'"
                                    },
                                    {
                                        "XXX TODO XXX": "not np.any(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1) != np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).astype(int))"
                                    },
                                    {"XXX TODO XXX": "_get_config()['assume_finite']"},
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype.kind in 'fc'"
                                            },
                                            {
                                                "XXX TODO XXX": "np.isfinite(_safe_accumulator_op(np.sum, np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1)))"
                                            },
                                        ]
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype.kind not in 'fc'"
                                    },
                                    {
                                        "XXX TODO XXX": "np.isfinite(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1)).all()"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "maximum": 0,
                                                "exclusiveMaximum": True,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"n_estimators": {"enum": [0]}},
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "is_multilabel(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))"
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).ndim > 2"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype == object"
                                            },
                                            {
                                                "XXX TODO XXX": "len(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))"
                                            },
                                            {
                                                "XXX TODO XXX": "isinstance(y.flat[0], str)"
                                            },
                                        ]
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).ndim == 2"
                                            },
                                            {"XXX TODO XXX": "y.shape[1] == 0"},
                                        ]
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype.kind != 'f'"
                                    },
                                    {
                                        "XXX TODO XXX": "not np.any(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1) != np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).astype(int))"
                                    },
                                    {"XXX TODO XXX": "_get_config()['assume_finite']"},
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype.kind in 'fc'"
                                            },
                                            {
                                                "XXX TODO XXX": "np.isfinite(_safe_accumulator_op(np.sum, np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1)))"
                                            },
                                        ]
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype.kind not in 'fc'"
                                    },
                                    {
                                        "XXX TODO XXX": "np.isfinite(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1)).all()"
                                    },
                                ]
                            },
                        ]
                    },
                ]
            },
            {
                "anyOf": [
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'estimators_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) >= 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "is_multilabel(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))"
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).ndim > 2"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype == object"
                                            },
                                            {
                                                "XXX TODO XXX": "len(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))"
                                            },
                                            {
                                                "XXX TODO XXX": "isinstance(y.flat[0], str)"
                                            },
                                        ]
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).ndim == 2"
                                            },
                                            {"XXX TODO XXX": "y.shape[1] == 0"},
                                        ]
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype.kind != 'f'"
                                    },
                                    {
                                        "XXX TODO XXX": "not np.any(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1) != np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).astype(int))"
                                    },
                                    {"XXX TODO XXX": "_get_config()['assume_finite']"},
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype.kind in 'fc'"
                                            },
                                            {
                                                "XXX TODO XXX": "np.isfinite(_safe_accumulator_op(np.sum, np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1)))"
                                            },
                                        ]
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype.kind not in 'fc'"
                                    },
                                    {
                                        "XXX TODO XXX": "np.isfinite(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1)).all()"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) < 0"
                                    },
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) == 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "is_multilabel(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))"
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).ndim > 2"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype == object"
                                            },
                                            {
                                                "XXX TODO XXX": "len(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))"
                                            },
                                            {
                                                "XXX TODO XXX": "isinstance(y.flat[0], str)"
                                            },
                                        ]
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).ndim == 2"
                                            },
                                            {"XXX TODO XXX": "y.shape[1] == 0"},
                                        ]
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype.kind != 'f'"
                                    },
                                    {
                                        "XXX TODO XXX": "not np.any(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1) != np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).astype(int))"
                                    },
                                    {"XXX TODO XXX": "_get_config()['assume_finite']"},
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype.kind in 'fc'"
                                            },
                                            {
                                                "XXX TODO XXX": "np.isfinite(_safe_accumulator_op(np.sum, np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1)))"
                                            },
                                        ]
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype.kind not in 'fc'"
                                    },
                                    {
                                        "XXX TODO XXX": "np.isfinite(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1)).all()"
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
        "description": "From /utils/validation.py:None:_assert_all_finite, Exception: raise ValueError('Input contains NaN') ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'estimators_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "minimum": 0,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "is_multilabel(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))"
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).ndim > 2"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype == object"
                                            },
                                            {
                                                "XXX TODO XXX": "len(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))"
                                            },
                                            {
                                                "XXX TODO XXX": "isinstance(y.flat[0], str)"
                                            },
                                        ]
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).ndim == 2"
                                            },
                                            {"XXX TODO XXX": "y.shape[1] == 0"},
                                        ]
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype.kind != 'f'"
                                    },
                                    {
                                        "XXX TODO XXX": "not np.any(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1) != np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).astype(int))"
                                    },
                                    {"XXX TODO XXX": "_get_config()['assume_finite']"},
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype.kind in 'fc'"
                                            },
                                            {
                                                "XXX TODO XXX": "np.isfinite(_safe_accumulator_op(np.sum, np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1)))"
                                            },
                                        ]
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype.kind in 'fc'"
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype != np.dtype('object')"
                                    },
                                    {
                                        "XXX TODO XXX": "not _object_dtype_isnan(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1)).any()"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "maximum": 0,
                                                "exclusiveMaximum": True,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"n_estimators": {"enum": [0]}},
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "is_multilabel(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))"
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).ndim > 2"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype == object"
                                            },
                                            {
                                                "XXX TODO XXX": "len(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))"
                                            },
                                            {
                                                "XXX TODO XXX": "isinstance(y.flat[0], str)"
                                            },
                                        ]
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).ndim == 2"
                                            },
                                            {"XXX TODO XXX": "y.shape[1] == 0"},
                                        ]
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype.kind != 'f'"
                                    },
                                    {
                                        "XXX TODO XXX": "not np.any(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1) != np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).astype(int))"
                                    },
                                    {"XXX TODO XXX": "_get_config()['assume_finite']"},
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype.kind in 'fc'"
                                            },
                                            {
                                                "XXX TODO XXX": "np.isfinite(_safe_accumulator_op(np.sum, np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1)))"
                                            },
                                        ]
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype.kind in 'fc'"
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype != np.dtype('object')"
                                    },
                                    {
                                        "XXX TODO XXX": "not _object_dtype_isnan(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1)).any()"
                                    },
                                ]
                            },
                        ]
                    },
                ]
            },
            {
                "anyOf": [
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'estimators_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) >= 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "is_multilabel(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))"
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).ndim > 2"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype == object"
                                            },
                                            {
                                                "XXX TODO XXX": "len(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))"
                                            },
                                            {
                                                "XXX TODO XXX": "isinstance(y.flat[0], str)"
                                            },
                                        ]
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).ndim == 2"
                                            },
                                            {"XXX TODO XXX": "y.shape[1] == 0"},
                                        ]
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype.kind != 'f'"
                                    },
                                    {
                                        "XXX TODO XXX": "not np.any(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1) != np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).astype(int))"
                                    },
                                    {"XXX TODO XXX": "_get_config()['assume_finite']"},
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype.kind in 'fc'"
                                            },
                                            {
                                                "XXX TODO XXX": "np.isfinite(_safe_accumulator_op(np.sum, np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1)))"
                                            },
                                        ]
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype.kind in 'fc'"
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype != np.dtype('object')"
                                    },
                                    {
                                        "XXX TODO XXX": "not _object_dtype_isnan(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1)).any()"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) < 0"
                                    },
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) == 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "is_multilabel(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))"
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).ndim > 2"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype == object"
                                            },
                                            {
                                                "XXX TODO XXX": "len(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))"
                                            },
                                            {
                                                "XXX TODO XXX": "isinstance(y.flat[0], str)"
                                            },
                                        ]
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).ndim == 2"
                                            },
                                            {"XXX TODO XXX": "y.shape[1] == 0"},
                                        ]
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype.kind != 'f'"
                                    },
                                    {
                                        "XXX TODO XXX": "not np.any(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1) != np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).astype(int))"
                                    },
                                    {"XXX TODO XXX": "_get_config()['assume_finite']"},
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype.kind in 'fc'"
                                            },
                                            {
                                                "XXX TODO XXX": "np.isfinite(_safe_accumulator_op(np.sum, np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1)))"
                                            },
                                        ]
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype.kind in 'fc'"
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).dtype != np.dtype('object')"
                                    },
                                    {
                                        "XXX TODO XXX": "not _object_dtype_isnan(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1)).any()"
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
        "description": "From /utils/multiclass.py:None:type_of_target, Exception: raise ValueError(     'Expected array-like (array or non-string sequence), got %r' % y) ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'estimators_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "minimum": 0,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "isinstance(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1), [Sequence, spmatrix])"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1), '__array__')"
                                                    },
                                                ]
                                            },
                                            {
                                                "XXX TODO XXX": "isinstance(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1), str)"
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
                                            "n_estimators": {
                                                "type": "number",
                                                "maximum": 0,
                                                "exclusiveMaximum": True,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"n_estimators": {"enum": [0]}},
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "isinstance(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1), [Sequence, spmatrix])"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1), '__array__')"
                                                    },
                                                ]
                                            },
                                            {
                                                "XXX TODO XXX": "isinstance(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1), str)"
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
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'estimators_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) >= 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "isinstance(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1), [Sequence, spmatrix])"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1), '__array__')"
                                                    },
                                                ]
                                            },
                                            {
                                                "XXX TODO XXX": "isinstance(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1), str)"
                                            },
                                        ]
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) < 0"
                                    },
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) == 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "isinstance(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1), [Sequence, spmatrix])"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1), '__array__')"
                                                    },
                                                ]
                                            },
                                            {
                                                "XXX TODO XXX": "isinstance(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1), str)"
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
        "description": "From /utils/multiclass.py:None:type_of_target, Exception: raise ValueError(\"y cannot be class 'SparseSeries' or 'SparseArray'\") ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'estimators_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "minimum": 0,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).__class__.__name__ not in ['SparseSeries', 'SparseArray']"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "maximum": 0,
                                                "exclusiveMaximum": True,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"n_estimators": {"enum": [0]}},
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).__class__.__name__ not in ['SparseSeries', 'SparseArray']"
                                    },
                                ]
                            },
                        ]
                    },
                ]
            },
            {
                "anyOf": [
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'estimators_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) >= 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).__class__.__name__ not in ['SparseSeries', 'SparseArray']"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) < 0"
                                    },
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) == 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1).__class__.__name__ not in ['SparseSeries', 'SparseArray']"
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
        "description": "From /utils/multiclass.py:None:type_of_target, Exception: raise ValueError(     'You appear to be using a legacy multi-label data representation. Sequence of sequences are no longer supported; use a binary array or sparse matrix instead - the MultiLabelBinarizer transformer can convert to this format.'     ) ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'estimators_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "minimum": 0,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "is_multilabel(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))"
                                    },
                                    {"XXX TODO XXX": "hasattr(y[0], '__array__')"},
                                    {"XXX TODO XXX": "isinstance(y[0], Sequence)"},
                                    {"XXX TODO XXX": "isinstance(y[0], str)"},
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "maximum": 0,
                                                "exclusiveMaximum": True,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"n_estimators": {"enum": [0]}},
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "is_multilabel(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))"
                                    },
                                    {"XXX TODO XXX": "hasattr(y[0], '__array__')"},
                                    {"XXX TODO XXX": "isinstance(y[0], Sequence)"},
                                    {"XXX TODO XXX": "isinstance(y[0], str)"},
                                ]
                            },
                        ]
                    },
                ]
            },
            {
                "anyOf": [
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'estimators_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) >= 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "is_multilabel(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))"
                                    },
                                    {"XXX TODO XXX": "hasattr(y[0], '__array__')"},
                                    {"XXX TODO XXX": "isinstance(y[0], Sequence)"},
                                    {"XXX TODO XXX": "isinstance(y[0], str)"},
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) < 0"
                                    },
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) == 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "is_multilabel(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))"
                                    },
                                    {"XXX TODO XXX": "hasattr(y[0], '__array__')"},
                                    {"XXX TODO XXX": "isinstance(y[0], Sequence)"},
                                    {"XXX TODO XXX": "isinstance(y[0], str)"},
                                ]
                            },
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": 'From /metrics/_classification.py:None:_check_targets, Exception: raise ValueError(     "Classification metrics can\'t handle a mix of {0} and {1} targets".     format(type_true, type_pred)) ',
        "allOf": [
            {
                "anyOf": [
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'estimators_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "minimum": 0,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))} == {'binary', 'multiclass'}"
                                    },
                                    {
                                        "XXX TODO XXX": "len({type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))}) <= 1"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "maximum": 0,
                                                "exclusiveMaximum": True,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"n_estimators": {"enum": [0]}},
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))} == {'binary', 'multiclass'}"
                                    },
                                    {
                                        "XXX TODO XXX": "len({type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))}) <= 1"
                                    },
                                ]
                            },
                        ]
                    },
                ]
            },
            {
                "anyOf": [
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'estimators_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) >= 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))} == {'binary', 'multiclass'}"
                                    },
                                    {
                                        "XXX TODO XXX": "len({type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))}) <= 1"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) < 0"
                                    },
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) == 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))} == {'binary', 'multiclass'}"
                                    },
                                    {
                                        "XXX TODO XXX": "len({type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))}) <= 1"
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
        "description": "From /metrics/_classification.py:None:_check_targets, Exception: raise ValueError('{0} is not supported'.format(y_type)) ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'estimators_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "minimum": 0,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))} == {'binary', 'multiclass'}"
                                    },
                                    {
                                        "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))}.pop() in ['binary', 'multiclass', 'multilabel-indicator']"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "maximum": 0,
                                                "exclusiveMaximum": True,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"n_estimators": {"enum": [0]}},
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))} == {'binary', 'multiclass'}"
                                    },
                                    {
                                        "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))}.pop() in ['binary', 'multiclass', 'multilabel-indicator']"
                                    },
                                ]
                            },
                        ]
                    },
                ]
            },
            {
                "anyOf": [
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'estimators_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) >= 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))} == {'binary', 'multiclass'}"
                                    },
                                    {
                                        "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))}.pop() in ['binary', 'multiclass', 'multilabel-indicator']"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) < 0"
                                    },
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) == 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))} == {'binary', 'multiclass'}"
                                    },
                                    {
                                        "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))}.pop() in ['binary', 'multiclass', 'multilabel-indicator']"
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
        "description": "From /metrics/_classification.py:None:_check_targets, Exception: raise TypeError(     f'Labels in y_true and y_pred should be of the same type. Got y_true={np.unique(y_true)} and y_pred={np.unique(y_pred)}. Make sure that the predictions provided by the classifier coincides with the true labels.'     ) from e ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'estimators_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "minimum": 0,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))} == {'binary', 'multiclass'}"
                                    },
                                    {
                                        "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))}.pop() not in ['binary', 'multiclass']"
                                    },
                                    {
                                        "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))}.pop() != 'binary'"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "maximum": 0,
                                                "exclusiveMaximum": True,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"n_estimators": {"enum": [0]}},
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))} == {'binary', 'multiclass'}"
                                    },
                                    {
                                        "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))}.pop() not in ['binary', 'multiclass']"
                                    },
                                    {
                                        "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))}.pop() != 'binary'"
                                    },
                                ]
                            },
                        ]
                    },
                ]
            },
            {
                "anyOf": [
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'estimators_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) >= 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))} == {'binary', 'multiclass'}"
                                    },
                                    {
                                        "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))}.pop() not in ['binary', 'multiclass']"
                                    },
                                    {
                                        "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))}.pop() != 'binary'"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) < 0"
                                    },
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) == 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))} == {'binary', 'multiclass'}"
                                    },
                                    {
                                        "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))}.pop() not in ['binary', 'multiclass']"
                                    },
                                    {
                                        "XXX TODO XXX": "{type_of_target(y), type_of_target(np.argmax(np.zeros([y.shape[0], self.n_classes_]), 1))}.pop() != 'binary'"
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
        "description": "From /utils/sparsefuncs.py:None:count_nonzero, Exception: raise TypeError('Expected CSR sparse format, got {0}'.format(X.format)) ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'estimators_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "minimum": 0,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "not _check_targets(y_true, y_pred)[0].startswith('multilabel')"
                                    },
                                    {
                                        "XXX TODO XXX": "(_check_targets(y_true, y_pred)[1] - _check_targets(y_true, y_pred)[2]).format == 'csr'"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_estimators": {
                                                "type": "number",
                                                "maximum": 0,
                                                "exclusiveMaximum": True,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"n_estimators": {"enum": [0]}},
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "not _check_targets(y_true, y_pred)[0].startswith('multilabel')"
                                    },
                                    {
                                        "XXX TODO XXX": "(_check_targets(y_true, y_pred)[1] - _check_targets(y_true, y_pred)[2]).format == 'csr'"
                                    },
                                ]
                            },
                        ]
                    },
                ]
            },
            {
                "anyOf": [
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'estimators_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) >= 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "not _check_targets(y_true, y_pred)[0].startswith('multilabel')"
                                    },
                                    {
                                        "XXX TODO XXX": "(_check_targets(y_true, y_pred)[1] - _check_targets(y_true, y_pred)[2]).format == 'csr'"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) < 0"
                                    },
                                    {
                                        "XXX TODO XXX": "self.n_estimators - len(self.estimators_) == 0"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {"oob_score": {"enum": [False]}},
                                    },
                                    {
                                        "XXX TODO XXX": "not _check_targets(y_true, y_pred)[0].startswith('multilabel')"
                                    },
                                    {
                                        "XXX TODO XXX": "(_check_targets(y_true, y_pred)[1] - _check_targets(y_true, y_pred)[2]).format == 'csr'"
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
        "description": "From /ensemble/_bagging.py:BaseBagging:_fit, Exception: raise ValueError('max_samples must be in (0, n_samples]') ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "type": "object",
                        "properties": {"max_samples": {"not": {"enum": [None]}}},
                    },
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {
                                    "max_samples": {
                                        "type": "number",
                                        "minimum": 0,
                                        "exclusiveMinimum": True,
                                    }
                                },
                            },
                            {
                                "type": "object",
                                "properties": {
                                    "max_samples": {"laleMaximum": "X/maxItems"}
                                },
                            },
                        ]
                    },
                ]
            },
            {
                "anyOf": [
                    {"type": "object", "properties": {"max_samples": {"enum": [None]}}},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "max_samples": {"type": "integer"}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "0 < int(self.max_samples * X.shape[0])"
                                            },
                                            {
                                                "XXX TODO XXX": "int(self.max_samples * X.shape[0]) <= X.shape[0]"
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
                                            "max_samples": {"not": {"type": "integer"}}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "max_samples": {
                                                        "type": "number",
                                                        "minimum": 0,
                                                        "exclusiveMinimum": True,
                                                    }
                                                },
                                            },
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "max_samples": {
                                                        "laleMaximum": "X/maxItems"
                                                    }
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
        "description": "From /ensemble/_bagging.py:BaseBagging:_fit, Exception: raise ValueError('max_features must be int or float') ",
        "anyOf": [
            {"type": "object", "properties": {"max_features": {"type": "integer"}}},
            {"type": "object", "properties": {"max_features": {"type": "number"}}},
        ],
    },
    {
        "description": "From /ensemble/_bagging.py:BaseBagging:_fit, Exception: raise ValueError('max_features must be in (0, n_features]') ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "type": "object",
                        "properties": {"max_features": {"not": {"type": "integer"}}},
                    },
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {
                                    "max_features": {
                                        "type": "number",
                                        "minimum": 0,
                                        "exclusiveMinimum": True,
                                    }
                                },
                            },
                            {
                                "type": "object",
                                "properties": {
                                    "max_features": {"laleMaximum": "X/items/maxItems"}
                                },
                            },
                        ]
                    },
                ]
            },
            {
                "anyOf": [
                    {
                        "type": "object",
                        "properties": {"max_features": {"type": "integer"}},
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "max_features": {"not": {"type": "number"}}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "0 < self.max_features * X.shape[1]"
                                            },
                                            {
                                                "XXX TODO XXX": "self.max_features * X.shape[1] <= X.shape[1]"
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
                                            "max_features": {"type": "number"}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "max_features": {
                                                        "type": "number",
                                                        "minimum": 0,
                                                        "exclusiveMinimum": True,
                                                    }
                                                },
                                            },
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "max_features": {
                                                        "laleMaximum": "X/items/maxItems"
                                                    }
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
        "description": "From /ensemble/_bagging.py:BaseBagging:_fit, Exception: raise ValueError('Out of bag estimation only available if bootstrap=True') ",
        "anyOf": [
            {"type": "object", "properties": {"bootstrap": {"enum": [True]}}},
            {"type": "object", "properties": {"oob_score": {"enum": [False]}}},
        ],
    },
    {
        "description": "From /ensemble/_bagging.py:BaseBagging:_fit, Exception: raise ValueError('Out of bag estimate only available if warm_start=False') ",
        "anyOf": [
            {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
            {"type": "object", "properties": {"oob_score": {"enum": [False]}}},
        ],
    },
    {
        "description": "From /ensemble/_bagging.py:BaseBagging:_fit, Exception: raise ValueError(     'n_estimators=%d must be larger or equal to len(estimators_)=%d when warm_start==True'      % (self.n_estimators, len(self.estimators_))) ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'estimators_')"},
                        ]
                    },
                    {
                        "type": "object",
                        "properties": {
                            "n_estimators": {"type": "number", "minimum": 0}
                        },
                    },
                ]
            },
            {
                "anyOf": [
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'estimators_')"},
                    {"XXX TODO XXX": "self.n_estimators - len(self.estimators_) >= 0"},
                ]
            },
        ],
    },
]
