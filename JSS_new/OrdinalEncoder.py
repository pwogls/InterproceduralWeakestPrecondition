[
    {
        "description": 'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) ',
        "anyOf": [
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(X, 'iloc')"},
                    {"XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"},
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
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(X, 'iloc')"},
                    {"XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"},
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
        "description": "From /utils/validation.py:None:_ensure_sparse_format, Exception: raise TypeError(     'A sparse matrix was passed, but dense data is required. Use X.toarray() to convert to a dense numpy array.'     ) ",
        "anyOf": [
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(X, 'iloc')"},
                    {"XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"},
                ]
            },
            {"type": "object", "laleNot": "X/isSparse"},
        ],
    },
    {
        "description": "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) ",
        "anyOf": [
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(X, 'iloc')"},
                    {"XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"},
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), False, None, False, True, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), False, None, False, True, True).fit)"
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, False, None, False, True, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X, False, None, False, True, True).fit)"
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), False, None, False, True, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), False, None, False, True, True).fit)"
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, False, None, False, True, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X, False, None, False, True, True).fit)"
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
        "description": "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Pandas DataFrame with mixed sparse extension arrays generated a sparse matrix with object dtype which can not be converted to a scipy sparse matrix.Sparse extension arrays should all have the same numeric type.'     ) ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "type": "object",
                        "properties": {
                            "handle_unknown": {"enum": ["error", "use_encoded_value"]}
                        },
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "handle_unknown": {
                                                "not": {"enum": ["use_encoded_value"]}
                                            }
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "not is_scalar_nan(self.unknown_value)"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.dtype(self.dtype).kind == 'f'"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'iloc')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"
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
                                                                        "XXX TODO XXX": "np.dtype(self.dtype).kind != 'f'"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'iloc')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"
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
                                                        "XXX TODO XXX": "is_scalar_nan(self.unknown_value)"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "type": "object",
                                                                        "properties": {
                                                                            "unknown_value": {
                                                                                "type": "integer"
                                                                            }
                                                                        },
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'iloc')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"
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
                                                                            "unknown_value": {
                                                                                "not": {
                                                                                    "type": "integer"
                                                                                }
                                                                            }
                                                                        },
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'iloc')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"
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
                                        "type": "object",
                                        "properties": {
                                            "handle_unknown": {
                                                "enum": ["use_encoded_value"]
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
                                                            "unknown_value": {
                                                                "enum": [None]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "hasattr(X, 'iloc')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"
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
                                                            "unknown_value": {
                                                                "not": {"enum": [None]}
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "hasattr(X, 'iloc')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"
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
                        "type": "object",
                        "properties": {
                            "handle_unknown": {
                                "not": {"enum": ["error", "use_encoded_value"]}
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
                                            "handle_unknown": {
                                                "not": {"enum": ["use_encoded_value"]}
                                            }
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "not is_scalar_nan(self.unknown_value)"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.dtype(self.dtype).kind == 'f'"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'iloc')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"
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
                                                                        "XXX TODO XXX": "np.dtype(self.dtype).kind != 'f'"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'iloc')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"
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
                                                        "XXX TODO XXX": "is_scalar_nan(self.unknown_value)"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "type": "object",
                                                                        "properties": {
                                                                            "unknown_value": {
                                                                                "type": "integer"
                                                                            }
                                                                        },
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'iloc')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"
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
                                                                            "unknown_value": {
                                                                                "not": {
                                                                                    "type": "integer"
                                                                                }
                                                                            }
                                                                        },
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'iloc')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"
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
                                        "type": "object",
                                        "properties": {
                                            "handle_unknown": {
                                                "enum": ["use_encoded_value"]
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
                                                            "unknown_value": {
                                                                "enum": [None]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "hasattr(X, 'iloc')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"
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
                                                            "unknown_value": {
                                                                "not": {"enum": [None]}
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "hasattr(X, 'iloc')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"
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
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(X, 'iloc')"},
                    {"XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"},
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
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(X, 'iloc')"},
                    {"XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"},
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
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(X, 'iloc')"},
                    {"XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"},
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), False, None, False, True, True)) >= 1"
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, False, None, False, True, True)) >= 1"
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), False, None, False, True, True)) >= 1"
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, False, None, False, True, True)) >= 1"
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
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(X, 'iloc')"},
                    {"XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"},
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), False, None, False, True, True).ndim != 2"
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X, False, None, False, True, True).ndim != 2"
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), False, None, False, True, True).ndim != 2"
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X, False, None, False, True, True).ndim != 2"
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
        "description": 'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) ',
        "anyOf": [
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(X, 'iloc')"},
                    {"XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"},
                ]
            },
            {"XXX TODO XXX": "hasattr(X, 'dtype')"},
            {
                "XXX TODO XXX": "not np.issubdtype(check_array(X, None, True).dtype, np.str_)"
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
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(X, 'iloc')"},
                    {"XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"},
                ]
            },
            {"XXX TODO XXX": "hasattr(X, 'dtype')"},
            {
                "XXX TODO XXX": "not np.issubdtype(check_array(X, None, True).dtype, np.str_)"
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
                                                                "XXX TODO XXX": "not all((False for object in list(X.dtypes)))"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=object), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=object).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=object).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=object).dtype.kind != 'c'"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=object), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=object).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=object).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=object).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "all((False for object in list(X.dtypes)))"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=object), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=object).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=object).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=object).dtype.kind != 'c'"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=object), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=object).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=object).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=object).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=object), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=object).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=object).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=object).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=object), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=object).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=object).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=object).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "not all((False for object in list(X.dtypes)))"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=object), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=object).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=object).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=object).dtype.kind != 'c'"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=object), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=object).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=object).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=object).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "all((False for object in list(X.dtypes)))"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=object), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=object).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=object).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=object).dtype.kind != 'c'"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=object), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=object).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=object).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=object).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=object), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=object).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=object).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=object).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=object), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=object).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=object).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=object).dtype.kind != 'c'"
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
        "description": "From /utils/validation.py:None:_ensure_sparse_format, Exception: raise TypeError(     'A sparse matrix was passed, but dense data is required. Use X.toarray() to convert to a dense numpy array.'     ) ",
        "anyOf": [
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(X, 'iloc')"},
                    {"XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"},
                ]
            },
            {"XXX TODO XXX": "hasattr(X, 'dtype')"},
            {
                "XXX TODO XXX": "not np.issubdtype(check_array(X, None, True).dtype, np.str_)"
            },
            {"type": "object", "laleNot": "X/isSparse"},
        ],
    },
    {
        "description": "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) ",
        "anyOf": [
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(X, 'iloc')"},
                    {"XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"},
                ]
            },
            {"XXX TODO XXX": "hasattr(X, 'dtype')"},
            {
                "XXX TODO XXX": "not np.issubdtype(check_array(X, None, True).dtype, np.str_)"
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), False, dtype=object, False, True, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), False, dtype=object, False, True, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=object), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), None, dtype=object).fit)"
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, False, dtype=object, False, True, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X, False, dtype=object, False, True, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=object), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(X, None, dtype=object).fit)"
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), False, dtype=object, False, True, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), False, dtype=object, False, True, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=object), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), None, dtype=object).fit)"
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, False, dtype=object, False, True, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X, False, dtype=object, False, True, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=object), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(X, None, dtype=object).fit)"
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
        "allOf": [
            {
                "anyOf": [
                    {
                        "type": "object",
                        "properties": {
                            "handle_unknown": {"enum": ["error", "use_encoded_value"]}
                        },
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "handle_unknown": {
                                                "not": {"enum": ["use_encoded_value"]}
                                            }
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "not is_scalar_nan(self.unknown_value)"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.dtype(self.dtype).kind == 'f'"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'iloc')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not np.issubdtype(check_array(X, None, True).dtype, np.str_)"
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
                                                                        "XXX TODO XXX": "np.dtype(self.dtype).kind != 'f'"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'iloc')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not np.issubdtype(check_array(X, None, True).dtype, np.str_)"
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
                                                        "XXX TODO XXX": "is_scalar_nan(self.unknown_value)"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "type": "object",
                                                                        "properties": {
                                                                            "unknown_value": {
                                                                                "type": "integer"
                                                                            }
                                                                        },
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'iloc')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not np.issubdtype(check_array(X, None, True).dtype, np.str_)"
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
                                                                            "unknown_value": {
                                                                                "not": {
                                                                                    "type": "integer"
                                                                                }
                                                                            }
                                                                        },
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'iloc')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not np.issubdtype(check_array(X, None, True).dtype, np.str_)"
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
                                        "type": "object",
                                        "properties": {
                                            "handle_unknown": {
                                                "enum": ["use_encoded_value"]
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
                                                            "unknown_value": {
                                                                "enum": [None]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "hasattr(X, 'iloc')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, 'dtype')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not np.issubdtype(check_array(X, None, True).dtype, np.str_)"
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
                                                            "unknown_value": {
                                                                "not": {"enum": [None]}
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "hasattr(X, 'iloc')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, 'dtype')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not np.issubdtype(check_array(X, None, True).dtype, np.str_)"
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
                        "type": "object",
                        "properties": {
                            "handle_unknown": {
                                "not": {"enum": ["error", "use_encoded_value"]}
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
                                            "handle_unknown": {
                                                "not": {"enum": ["use_encoded_value"]}
                                            }
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "not is_scalar_nan(self.unknown_value)"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.dtype(self.dtype).kind == 'f'"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'iloc')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not np.issubdtype(check_array(X, None, True).dtype, np.str_)"
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
                                                                        "XXX TODO XXX": "np.dtype(self.dtype).kind != 'f'"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'iloc')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not np.issubdtype(check_array(X, None, True).dtype, np.str_)"
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
                                                        "XXX TODO XXX": "is_scalar_nan(self.unknown_value)"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "type": "object",
                                                                        "properties": {
                                                                            "unknown_value": {
                                                                                "type": "integer"
                                                                            }
                                                                        },
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'iloc')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not np.issubdtype(check_array(X, None, True).dtype, np.str_)"
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
                                                                            "unknown_value": {
                                                                                "not": {
                                                                                    "type": "integer"
                                                                                }
                                                                            }
                                                                        },
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(X, 'iloc')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not np.issubdtype(check_array(X, None, True).dtype, np.str_)"
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
                                        "type": "object",
                                        "properties": {
                                            "handle_unknown": {
                                                "enum": ["use_encoded_value"]
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
                                                            "unknown_value": {
                                                                "enum": [None]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "hasattr(X, 'iloc')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, 'dtype')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not np.issubdtype(check_array(X, None, True).dtype, np.str_)"
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
                                                            "unknown_value": {
                                                                "not": {"enum": [None]}
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "hasattr(X, 'iloc')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(X, 'dtype')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not np.issubdtype(check_array(X, None, True).dtype, np.str_)"
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
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(X, 'iloc')"},
                    {"XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"},
                ]
            },
            {"XXX TODO XXX": "hasattr(X, 'dtype')"},
            {
                "XXX TODO XXX": "not np.issubdtype(check_array(X, None, True).dtype, np.str_)"
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
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(X, 'iloc')"},
                    {"XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"},
                ]
            },
            {"XXX TODO XXX": "hasattr(X, 'dtype')"},
            {
                "XXX TODO XXX": "not np.issubdtype(check_array(X, None, True).dtype, np.str_)"
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
                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=object).ndim < 3"
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
                                                "XXX TODO XXX": "np.asarray(X, None, dtype=object).ndim < 3"
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
                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=object).ndim < 3"
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
                                                "XXX TODO XXX": "np.asarray(X, None, dtype=object).ndim < 3"
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
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(X, 'iloc')"},
                    {"XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"},
                ]
            },
            {"XXX TODO XXX": "hasattr(X, 'dtype')"},
            {
                "XXX TODO XXX": "not np.issubdtype(check_array(X, None, True).dtype, np.str_)"
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), False, dtype=object, False, True, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=object)) >= 1"
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, False, dtype=object, False, True, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(X, None, dtype=object)) >= 1"
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), False, dtype=object, False, True, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=object)) >= 1"
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, False, dtype=object, False, True, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(X, None, dtype=object)) >= 1"
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
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(X, 'iloc')"},
                    {"XXX TODO XXX": "getattr(X, 'ndim', 0) == 2"},
                ]
            },
            {"XXX TODO XXX": "hasattr(X, 'dtype')"},
            {
                "XXX TODO XXX": "not np.issubdtype(check_array(X, None, True).dtype, np.str_)"
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), False, dtype=object, False, True, True).ndim != 2"
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
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=object).ndim != 2"
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X, False, dtype=object, False, True, True).ndim != 2"
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
                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=object).ndim != 2"
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), False, dtype=object, False, True, True).ndim != 2"
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
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=object).ndim != 2"
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X, False, dtype=object, False, True, True).ndim != 2"
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
                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=object).ndim != 2"
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
        "description": 'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) ',
        "anyOf": [
            {"XXX TODO XXX": "i not in range(X.shape[1])"},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "not hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                            },
                            {
                                "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim <= 1"
                            },
                            {"type": "object", "laleNot": "X/isSparse"},
                            {
                                "XXX TODO XXX": "not hasattr(self._get_feature(X, feature_idx=i).sparse.to_coo(), 'dtype')"
                            },
                            {
                                "XXX TODO XXX": "self._get_feature(X, feature_idx=i).sparse.to_coo().dtype is None"
                            },
                            {
                                "XXX TODO XXX": "not hasattr(self._get_feature(X, feature_idx=i).sparse.to_coo().dtype, 'kind')"
                            },
                            {
                                "XXX TODO XXX": "self._get_feature(X, feature_idx=i).sparse.to_coo().dtype.kind != 'c'"
                            },
                        ]
                    },
                    {
                        "anyOf": [
                            {
                                "allOf": [
                                    {
                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                    },
                                    {
                                        "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim > 1"
                                    },
                                ]
                            },
                            {"type": "object", "laleNot": "X/isSparse"},
                            {
                                "XXX TODO XXX": "not hasattr(self._get_feature(X, feature_idx=i), 'dtype')"
                            },
                            {
                                "XXX TODO XXX": "self._get_feature(X, feature_idx=i).dtype is None"
                            },
                            {
                                "XXX TODO XXX": "not hasattr(self._get_feature(X, feature_idx=i).dtype, 'kind')"
                            },
                            {
                                "XXX TODO XXX": "self._get_feature(X, feature_idx=i).dtype.kind != 'c'"
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
            {"XXX TODO XXX": "i not in range(X.shape[1])"},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "hasattr(getattr(self._get_feature(X, feature_idx=i), 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(self._get_feature(X, feature_idx=i), 'dtypes')"
                                            },
                                            {
                                                "XXX TODO XXX": "not hasattr(self._get_feature(X, feature_idx=i).dtypes, '__array__')"
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "not all((False for None in list(self._get_feature(X, feature_idx=i).dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim <= 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i).sparse.to_coo())"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None).dtype.kind != 'c'"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim > 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i))"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(self._get_feature(X, feature_idx=i), None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i), None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(self._get_feature(X, feature_idx=i), None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i), None, None).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "all((False for None in list(self._get_feature(X, feature_idx=i).dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim <= 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i).sparse.to_coo())"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None).dtype.kind != 'c'"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim > 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i))"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(self._get_feature(X, feature_idx=i), None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i), None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(self._get_feature(X, feature_idx=i), None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i), None, None).dtype.kind != 'c'"
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
                                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i), 'dtypes')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i).dtypes, '__array__')"
                                                    },
                                                ]
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "not hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim <= 1"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i).sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None).dtype.kind != 'c'"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim > 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i))"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(self._get_feature(X, feature_idx=i), None, None), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i), None, None).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(self._get_feature(X, feature_idx=i), None, None).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i), None, None).dtype.kind != 'c'"
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
                                "XXX TODO XXX": "not hasattr(getattr(self._get_feature(X, feature_idx=i), 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(self._get_feature(X, feature_idx=i), 'dtypes')"
                                            },
                                            {
                                                "XXX TODO XXX": "not hasattr(self._get_feature(X, feature_idx=i).dtypes, '__array__')"
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "not all((False for None in list(self._get_feature(X, feature_idx=i).dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim <= 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i).sparse.to_coo())"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None).dtype.kind != 'c'"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim > 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i))"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(self._get_feature(X, feature_idx=i), None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i), None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(self._get_feature(X, feature_idx=i), None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i), None, None).dtype.kind != 'c'"
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
                                                                "XXX TODO XXX": "all((False for None in list(self._get_feature(X, feature_idx=i).dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim <= 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i).sparse.to_coo())"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None).dtype.kind != 'c'"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim > 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i))"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(self._get_feature(X, feature_idx=i), None, None), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i), None, None).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(self._get_feature(X, feature_idx=i), None, None).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i), None, None).dtype.kind != 'c'"
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
                                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i), 'dtypes')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i).dtypes, '__array__')"
                                                    },
                                                ]
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "not hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim <= 1"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i).sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None).dtype.kind != 'c'"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim > 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i))"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(self._get_feature(X, feature_idx=i), None, None), 'dtype')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i), None, None).dtype is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(self._get_feature(X, feature_idx=i), None, None).dtype, 'kind')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i), None, None).dtype.kind != 'c'"
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
        "description": "From /utils/validation.py:None:_ensure_sparse_format, Exception: raise TypeError(     'A sparse matrix was passed, but dense data is required. Use X.toarray() to convert to a dense numpy array.'     ) ",
        "anyOf": [
            {"XXX TODO XXX": "i not in range(X.shape[1])"},
            {"type": "object", "laleNot": "X/isSparse"},
        ],
    },
    {
        "description": "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) ",
        "anyOf": [
            {"XXX TODO XXX": "i not in range(X.shape[1])"},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "hasattr(getattr(self._get_feature(X, feature_idx=i), 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {
                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i), 'dtypes')"
                                    },
                                    {
                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i).dtypes, '__array__')"
                                    },
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                            },
                                            {
                                                "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim <= 1"
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(self._get_feature(X, feature_idx=i).sparse.to_coo(), False, None, False, False, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(self._get_feature(X, feature_idx=i).sparse.to_coo(), False, None, False, False, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i).sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None).fit)"
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
                                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim > 1"
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(self._get_feature(X, feature_idx=i), False, None, False, False, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(self._get_feature(X, feature_idx=i), False, None, False, False, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i))"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(self._get_feature(X, feature_idx=i), None, None), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(self._get_feature(X, feature_idx=i), None, None).fit)"
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
                                "XXX TODO XXX": "not hasattr(getattr(self._get_feature(X, feature_idx=i), 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {
                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i), 'dtypes')"
                                    },
                                    {
                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i).dtypes, '__array__')"
                                    },
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                            },
                                            {
                                                "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim <= 1"
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(self._get_feature(X, feature_idx=i).sparse.to_coo(), False, None, False, False, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(self._get_feature(X, feature_idx=i).sparse.to_coo(), False, None, False, False, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i).sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None).fit)"
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
                                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim > 1"
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(self._get_feature(X, feature_idx=i), False, None, False, False, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(self._get_feature(X, feature_idx=i), False, None, False, False, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i))"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not hasattr(np.asarray(self._get_feature(X, feature_idx=i), None, None), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(np.asarray(self._get_feature(X, feature_idx=i), None, None).fit)"
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
            {"XXX TODO XXX": "i not in range(X.shape[1])"},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "not hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                            },
                            {
                                "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim <= 1"
                            },
                            {
                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i).sparse.to_coo())"
                            },
                        ]
                    },
                    {
                        "anyOf": [
                            {
                                "allOf": [
                                    {
                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                    },
                                    {
                                        "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim > 1"
                                    },
                                ]
                            },
                            {
                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i))"
                            },
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": "From /utils/validation.py:None:check_array, Exception: raise ValueError('Found array with dim %d. %s expected <= 2.' % (array.ndim,     estimator_name)) ",
        "anyOf": [
            {"XXX TODO XXX": "i not in range(X.shape[1])"},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "hasattr(getattr(self._get_feature(X, feature_idx=i), 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {
                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i), 'dtypes')"
                                    },
                                    {
                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i).dtypes, '__array__')"
                                    },
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                            },
                                            {
                                                "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim <= 1"
                                            },
                                            {
                                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i).sparse.to_coo())"
                                            },
                                            {
                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None).ndim < 3"
                                            },
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim > 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i))"
                                            },
                                            {
                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i), None, None).ndim < 3"
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
                                "XXX TODO XXX": "not hasattr(getattr(self._get_feature(X, feature_idx=i), 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {
                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i), 'dtypes')"
                                    },
                                    {
                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i).dtypes, '__array__')"
                                    },
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                            },
                                            {
                                                "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim <= 1"
                                            },
                                            {
                                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i).sparse.to_coo())"
                                            },
                                            {
                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None).ndim < 3"
                                            },
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim > 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i))"
                                            },
                                            {
                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i), None, None).ndim < 3"
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
            {"XXX TODO XXX": "i not in range(X.shape[1])"},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "hasattr(getattr(self._get_feature(X, feature_idx=i), 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {
                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i), 'dtypes')"
                                    },
                                    {
                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i).dtypes, '__array__')"
                                    },
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                            },
                                            {
                                                "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim <= 1"
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(self._get_feature(X, feature_idx=i).sparse.to_coo(), False, None, False, False, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i).sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None)) >= 1"
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
                                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim > 1"
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(self._get_feature(X, feature_idx=i), False, None, False, False, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i))"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(self._get_feature(X, feature_idx=i), None, None)) >= 1"
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
                                "XXX TODO XXX": "not hasattr(getattr(self._get_feature(X, feature_idx=i), 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {
                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i), 'dtypes')"
                                    },
                                    {
                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i).dtypes, '__array__')"
                                    },
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                            },
                                            {
                                                "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim <= 1"
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(self._get_feature(X, feature_idx=i).sparse.to_coo(), False, None, False, False, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i).sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None)) >= 1"
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
                                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim > 1"
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(self._get_feature(X, feature_idx=i), False, None, False, False, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i))"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "_num_samples(np.asarray(self._get_feature(X, feature_idx=i), None, None)) >= 1"
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
            {"XXX TODO XXX": "i not in range(X.shape[1])"},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "hasattr(getattr(self._get_feature(X, feature_idx=i), 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {
                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i), 'dtypes')"
                                    },
                                    {
                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i).dtypes, '__array__')"
                                    },
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                            },
                                            {
                                                "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim <= 1"
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(self._get_feature(X, feature_idx=i).sparse.to_coo(), False, None, False, False, True).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i).sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None).ndim != 2"
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
                                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim > 1"
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(self._get_feature(X, feature_idx=i), False, None, False, False, True).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i))"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i), None, None).ndim != 2"
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
                                "XXX TODO XXX": "not hasattr(getattr(self._get_feature(X, feature_idx=i), 'dtype', None), 'kind')"
                            },
                            {
                                "allOf": [
                                    {
                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i), 'dtypes')"
                                    },
                                    {
                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i).dtypes, '__array__')"
                                    },
                                ]
                            },
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "not hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                            },
                                            {
                                                "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim <= 1"
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(self._get_feature(X, feature_idx=i).sparse.to_coo(), False, None, False, False, True).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i).sparse.to_coo())"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i).sparse.to_coo(), None, None).ndim != 2"
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
                                                        "XXX TODO XXX": "hasattr(self._get_feature(X, feature_idx=i), 'sparse')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "self._get_feature(X, feature_idx=i).ndim > 1"
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(self._get_feature(X, feature_idx=i), False, None, False, False, True).ndim != 2"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "array.shape[1] >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(self._get_feature(X, feature_idx=i))"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "np.asarray(self._get_feature(X, feature_idx=i), None, None).ndim != 2"
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
        "description": "From /utils/_encode.py:None:_unique_python, Exception: raise TypeError(     f'Encoders require their input to be uniformly strings or numbers. Got {types}'     ) ",
        "anyOf": [
            {
                "XXX TODO XXX": "i not in range(self._check_X(X, force_all_finite=force_all_finite)[2])"
            },
            {
                "type": "object",
                "properties": {"categories": {"not": {"enum": ["auto"]}}},
            },
            {"XXX TODO XXX": "X_list[i].dtype != object"},
        ],
    },
    {
        "description": "From /preprocessing/_encoders.py:_BaseEncoder:_fit, Exception: raise ValueError(     'Shape mismatch: if categories is an array, it has to be of shape (n_features,).'     ) ",
        "anyOf": [
            {"type": "object", "properties": {"categories": {"enum": ["auto"]}}},
            {
                "XXX TODO XXX": "len(self.categories) == self._check_X(X, force_all_finite=force_all_finite)[2]"
            },
        ],
    },
    {
        "description": "From /preprocessing/_encoders.py:_BaseEncoder:_fit, Exception: raise ValueError(error_msg) ",
        "anyOf": [
            {
                "XXX TODO XXX": "i not in range(self._check_X(X, force_all_finite=force_all_finite)[2])"
            },
            {"type": "object", "properties": {"categories": {"enum": ["auto"]}}},
            {"XXX TODO XXX": "X_list[i].dtype.kind in 'OUS'"},
            {
                "allOf": [
                    {
                        "XXX TODO XXX": "not np.any(sorted_cats[:stop_idx] != cats[:stop_idx])"
                    },
                    {
                        "anyOf": [
                            {"XXX TODO XXX": "not np.isnan(sorted_cats[-1])"},
                            {"XXX TODO XXX": "np.isnan(sorted_cats[-1])"},
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": "From /preprocessing/_encoders.py:_BaseEncoder:_fit, Exception: raise ValueError(msg) ",
        "anyOf": [
            {
                "XXX TODO XXX": "i not in range(self._check_X(X, force_all_finite=force_all_finite)[2])"
            },
            {"type": "object", "properties": {"categories": {"enum": ["auto"]}}},
            {
                "XXX TODO XXX": "not _check_unknown(X_list[i], np.array(self.categories[i], dtype=X_list[i].dtype))"
            },
        ],
    },
    {
        "description": "From /preprocessing/_encoders.py:OrdinalEncoder:fit, Exception: raise ValueError(     f\"handle_unknown should be either 'error' or 'use_encoded_value', got {self.handle_unknown}.\"     ) ",
        "type": "object",
        "properties": {"handle_unknown": {"enum": ["error", "use_encoded_value"]}},
    },
    {
        "description": "From /preprocessing/_encoders.py:OrdinalEncoder:fit, Exception: raise ValueError(     f'When unknown_value is np.nan, the dtype parameter should be a float dtype. Got {self.dtype}.'     ) ",
        "anyOf": [
            {
                "type": "object",
                "properties": {
                    "handle_unknown": {"not": {"enum": ["use_encoded_value"]}}
                },
            },
            {"XXX TODO XXX": "not is_scalar_nan(self.unknown_value)"},
            {"XXX TODO XXX": "np.dtype(self.dtype).kind == 'f'"},
        ],
    },
    {
        "description": "From /preprocessing/_encoders.py:OrdinalEncoder:fit, Exception: raise TypeError(     f\"unknown_value should be an integer or np.nan when handle_unknown is 'use_encoded_value', got {self.unknown_value}.\"     ) ",
        "anyOf": [
            {
                "type": "object",
                "properties": {
                    "handle_unknown": {"not": {"enum": ["use_encoded_value"]}}
                },
            },
            {"XXX TODO XXX": "is_scalar_nan(self.unknown_value)"},
            {"type": "object", "properties": {"unknown_value": {"type": "integer"}}},
        ],
    },
    {
        "description": "From /preprocessing/_encoders.py:OrdinalEncoder:fit, Exception: raise TypeError(     f\"unknown_value should only be set when handle_unknown is 'use_encoded_value', got {self.unknown_value}.\"     ) ",
        "anyOf": [
            {
                "type": "object",
                "properties": {"handle_unknown": {"enum": ["use_encoded_value"]}},
            },
            {"type": "object", "properties": {"unknown_value": {"enum": [None]}}},
        ],
    },
    {
        "description": "From /preprocessing/_encoders.py:OrdinalEncoder:fit, Exception: raise ValueError(     f'The used value for unknown_value {self.unknown_value} is one of the values already used for encoding the seen categories.'     ) ",
        "anyOf": [
            {
                "type": "object",
                "properties": {
                    "handle_unknown": {"not": {"enum": ["use_encoded_value"]}}
                },
            },
            {"XXX TODO XXX": "feature_cats not in self.categories_"},
            {
                "type": "object",
                "properties": {
                    "unknown_value": {
                        "type": "number",
                        "maximum": 0,
                        "exclusiveMaximum": True,
                    }
                },
            },
            {"XXX TODO XXX": "self.unknown_value >= len(feature_cats)"},
        ],
    },
]
