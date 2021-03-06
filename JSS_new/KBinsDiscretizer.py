[
    {
        "description": 'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) ',
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "not hasattr(X, 'sparse')"},
                    {"XXX TODO XXX": "X.ndim <= 1"},
                    {"type": "object", "laleNot": "X/isSparse"},
                    {"XXX TODO XXX": "not hasattr(X.sparse.to_coo(), 'dtype')"},
                    {"XXX TODO XXX": "X.sparse.to_coo().dtype is None"},
                    {"XXX TODO XXX": "not hasattr(X.sparse.to_coo().dtype, 'kind')"},
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
        ],
    },
    {
        "description": 'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) ',
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {"XXX TODO XXX": "not hasattr(X, 'dtypes')"},
                                    {
                                        "XXX TODO XXX": "not hasattr(X.dtypes, '__array__')"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "not all((False for 'numeric' in list(X.dtypes)))"
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
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64), 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype, 'kind')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind != 'c'"
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
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=np.float64), 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=np.float64).dtype, 'kind')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype.kind != 'c'"
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "all((False for 'numeric' in list(X.dtypes)))"
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
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64), 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype, 'kind')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind != 'c'"
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
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=np.float64), 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=np.float64).dtype, 'kind')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype.kind != 'c'"
                                                                    },
                                                                ]
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
                                            {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
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
                                                    {"XXX TODO XXX": "X.ndim <= 1"},
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64), 'dtype')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype is None"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype, 'kind')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind != 'c'"
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
                                                    {"XXX TODO XXX": "sp.issparse(X)"},
                                                    {
                                                        "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=np.float64), 'dtype')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype is None"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=np.float64).dtype, 'kind')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype.kind != 'c'"
                                                    },
                                                ]
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
                    {"XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {"XXX TODO XXX": "not hasattr(X, 'dtypes')"},
                                    {
                                        "XXX TODO XXX": "not hasattr(X.dtypes, '__array__')"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "not all((False for 'numeric' in list(X.dtypes)))"
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
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64), 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype, 'kind')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind != 'c'"
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
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=np.float64), 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=np.float64).dtype, 'kind')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype.kind != 'c'"
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "all((False for 'numeric' in list(X.dtypes)))"
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
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64), 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype, 'kind')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind != 'c'"
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
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=np.float64), 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=np.float64).dtype, 'kind')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype.kind != 'c'"
                                                                    },
                                                                ]
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
                                            {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
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
                                                    {"XXX TODO XXX": "X.ndim <= 1"},
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64), 'dtype')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype is None"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype, 'kind')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind != 'c'"
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
                                                    {"XXX TODO XXX": "sp.issparse(X)"},
                                                    {
                                                        "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=np.float64), 'dtype')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype is None"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=np.float64).dtype, 'kind')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype.kind != 'c'"
                                                    },
                                                ]
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
        "type": "object",
        "laleNot": "X/isSparse",
    },
    {
        "description": "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) ",
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"},
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
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "laleNot": "X/isSparse",
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), False, dtype=np.float64, False, True, True), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), False, dtype=np.float64, False, True, True).fit)"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64), 'fit')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).fit)"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64), 'fit')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).fit)"
                                                                    },
                                                                ]
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
                                            {"XXX TODO XXX": "hasattr(X, 'sparse')"},
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
                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, False, dtype=np.float64, False, True, True), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(X, False, dtype=np.float64, False, True, True).fit)"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {"XXX TODO XXX": "sp.issparse(X)"},
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=np.float64).astype(np.float64), 'fit')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not callable(np.asarray(X, None, dtype=np.float64).astype(np.float64).fit)"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=np.float64), 'fit')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not callable(np.asarray(X, None, dtype=np.float64).fit)"
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
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
                    {"XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"},
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
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "laleNot": "X/isSparse",
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), False, dtype=np.float64, False, True, True), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), False, dtype=np.float64, False, True, True).fit)"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64), 'fit')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).fit)"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64), 'fit')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).fit)"
                                                                    },
                                                                ]
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
                                            {"XXX TODO XXX": "hasattr(X, 'sparse')"},
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
                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, False, dtype=np.float64, False, True, True), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(X, False, dtype=np.float64, False, True, True).fit)"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {"XXX TODO XXX": "sp.issparse(X)"},
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=np.float64).astype(np.float64), 'fit')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not callable(np.asarray(X, None, dtype=np.float64).astype(np.float64).fit)"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=np.float64), 'fit')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not callable(np.asarray(X, None, dtype=np.float64).fit)"
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
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
                    {"XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"},
                    {
                        "allOf": [
                            {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                            {"XXX TODO XXX": "hasattr(X.dtypes, '__array__')"},
                        ]
                    },
                    {"XXX TODO XXX": "not hasattr(X, 'sparse')"},
                    {"XXX TODO XXX": "X.ndim <= 1"},
                    {"XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"},
                    {
                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
                    },
                ]
            },
            {
                "anyOf": [
                    {"XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"},
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
                                        "XXX TODO XXX": "getattr(X, 'dtype', None) is None"
                                    },
                                    {
                                        "XXX TODO XXX": "getattr(X, 'dtype', None).kind != 'O'"
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
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "getattr(X, 'dtype', None) is not None"
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(X, 'dtype', None).kind == 'O'"
                                            },
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
                ]
            },
        ],
    },
    {
        "description": 'From /utils/validation.py:None:check_array, Exception: raise ValueError("""Complex data not supported {} """.format(array)     ) from complex_warning ',
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
        ],
    },
    {
        "description": "From /utils/validation.py:None:check_array, Exception: raise ValueError(     \"Unable to convert array of bytes/strings into decimal numbers with dtype='numeric'\"     ) from e ",
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {"XXX TODO XXX": "not hasattr(X, 'dtypes')"},
                                    {
                                        "XXX TODO XXX": "not hasattr(X.dtypes, '__array__')"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "not all((False for 'numeric' in list(X.dtypes)))"
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
                                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
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
                                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "all((False for 'numeric' in list(X.dtypes)))"
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
                                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
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
                                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                ]
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
                                            {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
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
                                                    {"XXX TODO XXX": "X.ndim <= 1"},
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
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
                                                    {"XXX TODO XXX": "sp.issparse(X)"},
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                    },
                                                ]
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
                    {"XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {"XXX TODO XXX": "not hasattr(X, 'dtypes')"},
                                    {
                                        "XXX TODO XXX": "not hasattr(X.dtypes, '__array__')"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "not all((False for 'numeric' in list(X.dtypes)))"
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
                                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
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
                                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "all((False for 'numeric' in list(X.dtypes)))"
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
                                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
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
                                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                ]
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
                                            {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
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
                                                    {"XXX TODO XXX": "X.ndim <= 1"},
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
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
                                                    {"XXX TODO XXX": "sp.issparse(X)"},
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                    },
                                                ]
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
        "description": "From /utils/validation.py:None:check_array, Exception: raise ValueError('Found array with dim %d. %s expected <= 2.' % (array.ndim,     estimator_name)) ",
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"},
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
                                    {"XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"},
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).ndim < 3"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).ndim < 3"
                                                    },
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
                                    {"XXX TODO XXX": "sp.issparse(X)"},
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).astype(np.float64).ndim < 3"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).ndim < 3"
                                                    },
                                                ]
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
                    {"XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"},
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
                                    {"XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"},
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).ndim < 3"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).ndim < 3"
                                                    },
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
                                    {"XXX TODO XXX": "sp.issparse(X)"},
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).astype(np.float64).ndim < 3"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).ndim < 3"
                                                    },
                                                ]
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
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"},
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
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "laleNot": "X/isSparse",
                                                    },
                                                    {
                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), False, dtype=np.float64, False, True, True)) >= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64)) >= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=np.float64)) >= 1"
                                                                    },
                                                                ]
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
                                            {"XXX TODO XXX": "hasattr(X, 'sparse')"},
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
                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, False, dtype=np.float64, False, True, True)) >= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {"XXX TODO XXX": "sp.issparse(X)"},
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "_num_samples(np.asarray(X, None, dtype=np.float64).astype(np.float64)) >= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "_num_samples(np.asarray(X, None, dtype=np.float64)) >= 1"
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
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
                    {"XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"},
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
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "laleNot": "X/isSparse",
                                                    },
                                                    {
                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), False, dtype=np.float64, False, True, True)) >= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64)) >= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=np.float64)) >= 1"
                                                                    },
                                                                ]
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
                                            {"XXX TODO XXX": "hasattr(X, 'sparse')"},
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
                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, False, dtype=np.float64, False, True, True)) >= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {"XXX TODO XXX": "sp.issparse(X)"},
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "_num_samples(np.asarray(X, None, dtype=np.float64).astype(np.float64)) >= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "_num_samples(np.asarray(X, None, dtype=np.float64)) >= 1"
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
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
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "hasattr(getattr(X, 'dtype', None), 'kind')"},
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
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "laleNot": "X/isSparse",
                                                    },
                                                    {
                                                        "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), False, dtype=np.float64, False, True, True).ndim != 2"
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
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).ndim != 2"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "array.shape[1] >= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).ndim != 2"
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
                                        "allOf": [
                                            {"XXX TODO XXX": "hasattr(X, 'sparse')"},
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
                                                        "XXX TODO XXX": "_ensure_sparse_format(X, False, dtype=np.float64, False, True, True).ndim != 2"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "array.shape[1] >= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {"XXX TODO XXX": "sp.issparse(X)"},
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).astype(np.float64).ndim != 2"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "array.shape[1] >= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).ndim != 2"
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
                ]
            },
            {
                "anyOf": [
                    {"XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"},
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
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "laleNot": "X/isSparse",
                                                    },
                                                    {
                                                        "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), False, dtype=np.float64, False, True, True).ndim != 2"
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
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).ndim != 2"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "array.shape[1] >= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).ndim != 2"
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
                                        "allOf": [
                                            {"XXX TODO XXX": "hasattr(X, 'sparse')"},
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
                                                        "XXX TODO XXX": "_ensure_sparse_format(X, False, dtype=np.float64, False, True, True).ndim != 2"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "array.shape[1] >= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {"XXX TODO XXX": "sp.issparse(X)"},
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).astype(np.float64).ndim != 2"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "array.shape[1] >= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).ndim != 2"
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
                ]
            },
        ],
    },
    {
        "description": 'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) ',
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "not hasattr(self.n_bins, 'sparse')"},
                    {"XXX TODO XXX": "self.n_bins.ndim <= 1"},
                    {"type": "object", "laleNot": "X/isSparse"},
                    {
                        "XXX TODO XXX": "not hasattr(self.n_bins.sparse.to_coo(), 'dtype')"
                    },
                    {"XXX TODO XXX": "self.n_bins.sparse.to_coo().dtype is None"},
                    {
                        "XXX TODO XXX": "not hasattr(self.n_bins.sparse.to_coo().dtype, 'kind')"
                    },
                    {"XXX TODO XXX": "self.n_bins.sparse.to_coo().dtype.kind != 'c'"},
                ]
            },
            {
                "anyOf": [
                    {
                        "allOf": [
                            {"XXX TODO XXX": "hasattr(self.n_bins, 'sparse')"},
                            {"XXX TODO XXX": "self.n_bins.ndim > 1"},
                        ]
                    },
                    {"type": "object", "laleNot": "X/isSparse"},
                    {"XXX TODO XXX": "not hasattr(self.n_bins, 'dtype')"},
                    {"XXX TODO XXX": "self.n_bins.dtype is None"},
                    {"XXX TODO XXX": "not hasattr(self.n_bins.dtype, 'kind')"},
                    {"XXX TODO XXX": "self.n_bins.dtype.kind != 'c'"},
                ]
            },
        ],
    },
    {
        "description": 'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) ',
        "allOf": [
            {
                "anyOf": [
                    {
                        "XXX TODO XXX": "hasattr(getattr(self.n_bins, 'dtype', None), 'kind')"
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "not hasattr(self.n_bins, 'dtypes')"
                                    },
                                    {
                                        "XXX TODO XXX": "not hasattr(self.n_bins.dtypes, '__array__')"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "not all((False for int in list(self.n_bins.dtypes)))"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(self.n_bins, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "self.n_bins.ndim <= 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "sp.issparse(self.n_bins.sparse.to_coo())"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False), 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False).dtype is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False).dtype, 'kind')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False).dtype.kind != 'c'"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(self.n_bins, 'sparse')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "self.n_bins.ndim > 1"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "sp.issparse(self.n_bins)"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(self.n_bins, None).astype(int, casting='unsafe', False), 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(self.n_bins, None).astype(int, casting='unsafe', False).dtype is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(self.n_bins, None).astype(int, casting='unsafe', False).dtype, 'kind')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(self.n_bins, None).astype(int, casting='unsafe', False).dtype.kind != 'c'"
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "all((False for int in list(self.n_bins.dtypes)))"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(self.n_bins, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "self.n_bins.ndim <= 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "sp.issparse(self.n_bins.sparse.to_coo())"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False), 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False).dtype is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False).dtype, 'kind')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False).dtype.kind != 'c'"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(self.n_bins, 'sparse')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "self.n_bins.ndim > 1"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "sp.issparse(self.n_bins)"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(self.n_bins, None).astype(int, casting='unsafe', False), 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(self.n_bins, None).astype(int, casting='unsafe', False).dtype is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(self.n_bins, None).astype(int, casting='unsafe', False).dtype, 'kind')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(self.n_bins, None).astype(int, casting='unsafe', False).dtype.kind != 'c'"
                                                                    },
                                                                ]
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
                                                "XXX TODO XXX": "hasattr(self.n_bins, 'dtypes')"
                                            },
                                            {
                                                "XXX TODO XXX": "hasattr(self.n_bins.dtypes, '__array__')"
                                            },
                                        ]
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "not hasattr(self.n_bins, 'sparse')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "self.n_bins.ndim <= 1"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(self.n_bins.sparse.to_coo())"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False), 'dtype')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False).dtype is None"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False).dtype, 'kind')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False).dtype.kind != 'c'"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "hasattr(self.n_bins, 'sparse')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "self.n_bins.ndim > 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(self.n_bins)"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(np.asarray(self.n_bins, None).astype(int, casting='unsafe', False), 'dtype')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(self.n_bins, None).astype(int, casting='unsafe', False).dtype is None"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(np.asarray(self.n_bins, None).astype(int, casting='unsafe', False).dtype, 'kind')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(self.n_bins, None).astype(int, casting='unsafe', False).dtype.kind != 'c'"
                                                    },
                                                ]
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
                        "XXX TODO XXX": "not hasattr(getattr(self.n_bins, 'dtype', None), 'kind')"
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "not hasattr(self.n_bins, 'dtypes')"
                                    },
                                    {
                                        "XXX TODO XXX": "not hasattr(self.n_bins.dtypes, '__array__')"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "not all((False for int in list(self.n_bins.dtypes)))"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(self.n_bins, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "self.n_bins.ndim <= 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "sp.issparse(self.n_bins.sparse.to_coo())"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False), 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False).dtype is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False).dtype, 'kind')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False).dtype.kind != 'c'"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(self.n_bins, 'sparse')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "self.n_bins.ndim > 1"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "sp.issparse(self.n_bins)"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(self.n_bins, None).astype(int, casting='unsafe', False), 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(self.n_bins, None).astype(int, casting='unsafe', False).dtype is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(self.n_bins, None).astype(int, casting='unsafe', False).dtype, 'kind')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(self.n_bins, None).astype(int, casting='unsafe', False).dtype.kind != 'c'"
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "all((False for int in list(self.n_bins.dtypes)))"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(self.n_bins, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "self.n_bins.ndim <= 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "sp.issparse(self.n_bins.sparse.to_coo())"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False), 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False).dtype is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False).dtype, 'kind')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False).dtype.kind != 'c'"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "hasattr(self.n_bins, 'sparse')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "self.n_bins.ndim > 1"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "sp.issparse(self.n_bins)"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(self.n_bins, None).astype(int, casting='unsafe', False), 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(self.n_bins, None).astype(int, casting='unsafe', False).dtype is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(self.n_bins, None).astype(int, casting='unsafe', False).dtype, 'kind')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(self.n_bins, None).astype(int, casting='unsafe', False).dtype.kind != 'c'"
                                                                    },
                                                                ]
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
                                                "XXX TODO XXX": "hasattr(self.n_bins, 'dtypes')"
                                            },
                                            {
                                                "XXX TODO XXX": "hasattr(self.n_bins.dtypes, '__array__')"
                                            },
                                        ]
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "not hasattr(self.n_bins, 'sparse')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "self.n_bins.ndim <= 1"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(self.n_bins.sparse.to_coo())"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False), 'dtype')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False).dtype is None"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False).dtype, 'kind')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False).dtype.kind != 'c'"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "hasattr(self.n_bins, 'sparse')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "self.n_bins.ndim > 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(self.n_bins)"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(np.asarray(self.n_bins, None).astype(int, casting='unsafe', False), 'dtype')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(self.n_bins, None).astype(int, casting='unsafe', False).dtype is None"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(np.asarray(self.n_bins, None).astype(int, casting='unsafe', False).dtype, 'kind')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(self.n_bins, None).astype(int, casting='unsafe', False).dtype.kind != 'c'"
                                                    },
                                                ]
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
        "type": "object",
        "laleNot": "X/isSparse",
    },
    {
        "description": "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "XXX TODO XXX": "hasattr(getattr(self.n_bins, 'dtype', None), 'kind')"
                    },
                    {
                        "allOf": [
                            {"XXX TODO XXX": "hasattr(self.n_bins, 'dtypes')"},
                            {
                                "XXX TODO XXX": "hasattr(self.n_bins.dtypes, '__array__')"
                            },
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "not hasattr(self.n_bins, 'sparse')"
                                    },
                                    {"XXX TODO XXX": "self.n_bins.ndim <= 1"},
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "laleNot": "X/isSparse",
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(self.n_bins.sparse.to_coo(), False, dtype=int, True, True, True), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(self.n_bins.sparse.to_coo(), False, dtype=int, True, True, True).fit)"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(self.n_bins.sparse.to_coo())"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False).fit)"
                                                    },
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
                                                "XXX TODO XXX": "hasattr(self.n_bins, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "self.n_bins.ndim > 1"},
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
                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(self.n_bins, False, dtype=int, True, True, True), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(self.n_bins, False, dtype=int, True, True, True).fit)"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(self.n_bins)"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(np.asarray(self.n_bins, None).astype(int, casting='unsafe', False), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(np.asarray(self.n_bins, None).astype(int, casting='unsafe', False).fit)"
                                                    },
                                                ]
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
                        "XXX TODO XXX": "not hasattr(getattr(self.n_bins, 'dtype', None), 'kind')"
                    },
                    {
                        "allOf": [
                            {"XXX TODO XXX": "hasattr(self.n_bins, 'dtypes')"},
                            {
                                "XXX TODO XXX": "hasattr(self.n_bins.dtypes, '__array__')"
                            },
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "not hasattr(self.n_bins, 'sparse')"
                                    },
                                    {"XXX TODO XXX": "self.n_bins.ndim <= 1"},
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "laleNot": "X/isSparse",
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(self.n_bins.sparse.to_coo(), False, dtype=int, True, True, True), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(self.n_bins.sparse.to_coo(), False, dtype=int, True, True, True).fit)"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(self.n_bins.sparse.to_coo())"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False).fit)"
                                                    },
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
                                                "XXX TODO XXX": "hasattr(self.n_bins, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "self.n_bins.ndim > 1"},
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
                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(self.n_bins, False, dtype=int, True, True, True), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(self.n_bins, False, dtype=int, True, True, True).fit)"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(self.n_bins)"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(np.asarray(self.n_bins, None).astype(int, casting='unsafe', False), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(np.asarray(self.n_bins, None).astype(int, casting='unsafe', False).fit)"
                                                    },
                                                ]
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
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "not hasattr(self.n_bins, 'sparse')"},
                    {"XXX TODO XXX": "self.n_bins.ndim <= 1"},
                    {"XXX TODO XXX": "sp.issparse(self.n_bins.sparse.to_coo())"},
                ]
            },
            {
                "anyOf": [
                    {
                        "allOf": [
                            {"XXX TODO XXX": "hasattr(self.n_bins, 'sparse')"},
                            {"XXX TODO XXX": "self.n_bins.ndim > 1"},
                        ]
                    },
                    {"XXX TODO XXX": "sp.issparse(self.n_bins)"},
                ]
            },
        ],
    },
    {
        "description": "From /utils/validation.py:None:check_array, Exception: raise ValueError('Found array with dim %d. %s expected <= 2.' % (array.ndim,     estimator_name)) ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "XXX TODO XXX": "hasattr(getattr(self.n_bins, 'dtype', None), 'kind')"
                    },
                    {
                        "allOf": [
                            {"XXX TODO XXX": "hasattr(self.n_bins, 'dtypes')"},
                            {
                                "XXX TODO XXX": "hasattr(self.n_bins.dtypes, '__array__')"
                            },
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "not hasattr(self.n_bins, 'sparse')"
                                    },
                                    {"XXX TODO XXX": "self.n_bins.ndim <= 1"},
                                    {
                                        "XXX TODO XXX": "sp.issparse(self.n_bins.sparse.to_coo())"
                                    },
                                    {
                                        "XXX TODO XXX": "np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False).ndim < 3"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "hasattr(self.n_bins, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "self.n_bins.ndim > 1"},
                                        ]
                                    },
                                    {"XXX TODO XXX": "sp.issparse(self.n_bins)"},
                                    {
                                        "XXX TODO XXX": "np.asarray(self.n_bins, None).astype(int, casting='unsafe', False).ndim < 3"
                                    },
                                ]
                            },
                        ]
                    },
                ]
            },
            {
                "anyOf": [
                    {
                        "XXX TODO XXX": "not hasattr(getattr(self.n_bins, 'dtype', None), 'kind')"
                    },
                    {
                        "allOf": [
                            {"XXX TODO XXX": "hasattr(self.n_bins, 'dtypes')"},
                            {
                                "XXX TODO XXX": "hasattr(self.n_bins.dtypes, '__array__')"
                            },
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "not hasattr(self.n_bins, 'sparse')"
                                    },
                                    {"XXX TODO XXX": "self.n_bins.ndim <= 1"},
                                    {
                                        "XXX TODO XXX": "sp.issparse(self.n_bins.sparse.to_coo())"
                                    },
                                    {
                                        "XXX TODO XXX": "np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False).ndim < 3"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "hasattr(self.n_bins, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "self.n_bins.ndim > 1"},
                                        ]
                                    },
                                    {"XXX TODO XXX": "sp.issparse(self.n_bins)"},
                                    {
                                        "XXX TODO XXX": "np.asarray(self.n_bins, None).astype(int, casting='unsafe', False).ndim < 3"
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
        "allOf": [
            {
                "anyOf": [
                    {
                        "XXX TODO XXX": "hasattr(getattr(self.n_bins, 'dtype', None), 'kind')"
                    },
                    {
                        "allOf": [
                            {"XXX TODO XXX": "hasattr(self.n_bins, 'dtypes')"},
                            {
                                "XXX TODO XXX": "hasattr(self.n_bins.dtypes, '__array__')"
                            },
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "not hasattr(self.n_bins, 'sparse')"
                                    },
                                    {"XXX TODO XXX": "self.n_bins.ndim <= 1"},
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "laleNot": "X/isSparse",
                                                    },
                                                    {
                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(self.n_bins.sparse.to_coo(), False, dtype=int, True, True, True)) >= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(self.n_bins.sparse.to_coo())"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "_num_samples(np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False)) >= 1"
                                                    },
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
                                                "XXX TODO XXX": "hasattr(self.n_bins, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "self.n_bins.ndim > 1"},
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
                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(self.n_bins, False, dtype=int, True, True, True)) >= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(self.n_bins)"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "_num_samples(np.asarray(self.n_bins, None).astype(int, casting='unsafe', False)) >= 1"
                                                    },
                                                ]
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
                        "XXX TODO XXX": "not hasattr(getattr(self.n_bins, 'dtype', None), 'kind')"
                    },
                    {
                        "allOf": [
                            {"XXX TODO XXX": "hasattr(self.n_bins, 'dtypes')"},
                            {
                                "XXX TODO XXX": "hasattr(self.n_bins.dtypes, '__array__')"
                            },
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "not hasattr(self.n_bins, 'sparse')"
                                    },
                                    {"XXX TODO XXX": "self.n_bins.ndim <= 1"},
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "laleNot": "X/isSparse",
                                                    },
                                                    {
                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(self.n_bins.sparse.to_coo(), False, dtype=int, True, True, True)) >= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(self.n_bins.sparse.to_coo())"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "_num_samples(np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False)) >= 1"
                                                    },
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
                                                "XXX TODO XXX": "hasattr(self.n_bins, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "self.n_bins.ndim > 1"},
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
                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(self.n_bins, False, dtype=int, True, True, True)) >= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(self.n_bins)"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "_num_samples(np.asarray(self.n_bins, None).astype(int, casting='unsafe', False)) >= 1"
                                                    },
                                                ]
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
        "allOf": [
            {
                "anyOf": [
                    {
                        "XXX TODO XXX": "hasattr(getattr(self.n_bins, 'dtype', None), 'kind')"
                    },
                    {
                        "allOf": [
                            {"XXX TODO XXX": "hasattr(self.n_bins, 'dtypes')"},
                            {
                                "XXX TODO XXX": "hasattr(self.n_bins.dtypes, '__array__')"
                            },
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "not hasattr(self.n_bins, 'sparse')"
                                    },
                                    {"XXX TODO XXX": "self.n_bins.ndim <= 1"},
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "laleNot": "X/isSparse",
                                                    },
                                                    {
                                                        "XXX TODO XXX": "_ensure_sparse_format(self.n_bins.sparse.to_coo(), False, dtype=int, True, True, True).ndim != 2"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "array.shape[1] >= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(self.n_bins.sparse.to_coo())"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False).ndim != 2"
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
                                                "XXX TODO XXX": "hasattr(self.n_bins, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "self.n_bins.ndim > 1"},
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
                                                        "XXX TODO XXX": "_ensure_sparse_format(self.n_bins, False, dtype=int, True, True, True).ndim != 2"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "array.shape[1] >= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(self.n_bins)"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(self.n_bins, None).astype(int, casting='unsafe', False).ndim != 2"
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
                        "XXX TODO XXX": "not hasattr(getattr(self.n_bins, 'dtype', None), 'kind')"
                    },
                    {
                        "allOf": [
                            {"XXX TODO XXX": "hasattr(self.n_bins, 'dtypes')"},
                            {
                                "XXX TODO XXX": "hasattr(self.n_bins.dtypes, '__array__')"
                            },
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "not hasattr(self.n_bins, 'sparse')"
                                    },
                                    {"XXX TODO XXX": "self.n_bins.ndim <= 1"},
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "laleNot": "X/isSparse",
                                                    },
                                                    {
                                                        "XXX TODO XXX": "_ensure_sparse_format(self.n_bins.sparse.to_coo(), False, dtype=int, True, True, True).ndim != 2"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "array.shape[1] >= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(self.n_bins.sparse.to_coo())"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(self.n_bins.sparse.to_coo(), None).astype(int, casting='unsafe', False).ndim != 2"
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
                                                "XXX TODO XXX": "hasattr(self.n_bins, 'sparse')"
                                            },
                                            {"XXX TODO XXX": "self.n_bins.ndim > 1"},
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
                                                        "XXX TODO XXX": "_ensure_sparse_format(self.n_bins, False, dtype=int, True, True, True).ndim != 2"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "array.shape[1] >= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(self.n_bins)"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(self.n_bins, None).astype(int, casting='unsafe', False).ndim != 2"
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
        ],
    },
    {
        "description": "From /preprocessing/_discretization.py:KBinsDiscretizer:_validate_n_bins, Exception: raise ValueError(     '{} received an invalid n_bins type. Received {}, expected int.'.format     (KBinsDiscretizer.__name__, type(orig_bins).__name__)) ",
        "anyOf": [
            {"type": "object", "properties": {"n_bins": {"not": {"type": "number"}}}},
            {"type": "object", "properties": {"n_bins": {"type": "integer"}}},
        ],
    },
    {
        "description": "From /preprocessing/_discretization.py:KBinsDiscretizer:_validate_n_bins, Exception: raise ValueError(     '{} received an invalid number of bins. Received {}, expected at least 2.'     .format(KBinsDiscretizer.__name__, orig_bins)) ",
        "anyOf": [
            {"type": "object", "properties": {"n_bins": {"not": {"type": "number"}}}},
            {
                "type": "object",
                "properties": {"n_bins": {"type": "number", "minimum": 2}},
            },
        ],
    },
    {
        "description": "From /preprocessing/_discretization.py:KBinsDiscretizer:_validate_n_bins, Exception: raise ValueError('n_bins must be a scalar or array of shape (n_features,).') ",
        "allOf": [
            {
                "XXX TODO XXX": "check_array(self.n_bins, dtype=int, True, False).ndim <= 1"
            },
            {"XXX TODO XXX": "n_bins.shape[0] == X.shape[1]"},
        ],
    },
    {
        "description": "From /preprocessing/_discretization.py:KBinsDiscretizer:_validate_n_bins, Exception: raise ValueError(     '{} received an invalid number of bins at indices {}. Number of bins must be at least 2, and must be an int.'     .format(KBinsDiscretizer.__name__, indices)) ",
        "XXX TODO XXX": "violating_indices.shape[0] <= 0",
    },
    {
        "description": "From /preprocessing/_discretization.py:KBinsDiscretizer:fit, Exception: raise ValueError(     f\"Valid options for 'dtype' are {supported_dtype + (None,)}. Got dtype={self.dtype}  instead.\"     ) ",
        "anyOf": [
            {
                "type": "object",
                "properties": {"dtype": {"enum": ["np.float64", "np.float32"]}},
            },
            {"type": "object", "properties": {"dtype": {"enum": [None]}}},
        ],
    },
    {
        "description": "From /preprocessing/_discretization.py:KBinsDiscretizer:fit, Exception: raise ValueError(\"Valid options for 'encode' are {}. Got encode={!r} instead.\"     .format(valid_encode, self.encode)) ",
        "type": "object",
        "properties": {"encode": {"enum": ["onehot", "onehot-dense", "ordinal"]}},
    },
    {
        "description": "From /preprocessing/_discretization.py:KBinsDiscretizer:fit, Exception: raise ValueError(     \"Valid options for 'strategy' are {}. Got strategy={!r} instead.\".     format(valid_strategy, self.strategy)) ",
        "type": "object",
        "properties": {"strategy": {"enum": ["uniform", "quantile", "kmeans"]}},
    },
]
