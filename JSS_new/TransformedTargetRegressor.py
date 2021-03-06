[
    {
        "description": 'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) ',
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "not hasattr(y, 'sparse')"},
                    {"XXX TODO XXX": "y.ndim <= 1"},
                    {"type": "object", "laleNot": "X/isSparse"},
                    {"XXX TODO XXX": "not hasattr(y.sparse.to_coo(), 'dtype')"},
                    {"XXX TODO XXX": "y.sparse.to_coo().dtype is None"},
                    {"XXX TODO XXX": "not hasattr(y.sparse.to_coo().dtype, 'kind')"},
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
        ],
    },
    {
        "description": 'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) ',
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "hasattr(getattr(y, 'dtype', None), 'kind')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {"XXX TODO XXX": "not hasattr(y, 'dtypes')"},
                                    {
                                        "XXX TODO XXX": "not hasattr(y.dtypes, '__array__')"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "not all((False for 'numeric' in list(y.dtypes)))"
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
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, dtype=np.float64), 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype, 'kind')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype.kind != 'c'"
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
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(y, None, dtype=np.float64), 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(y, None, dtype=np.float64).dtype, 'kind')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype.kind != 'c'"
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "all((False for 'numeric' in list(y.dtypes)))"
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
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, dtype=np.float64), 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype, 'kind')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype.kind != 'c'"
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
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(y, None, dtype=np.float64), 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(y, None, dtype=np.float64).dtype, 'kind')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype.kind != 'c'"
                                                                    },
                                                                ]
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
                                            {"XXX TODO XXX": "hasattr(y, 'dtypes')"},
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
                                                    {"XXX TODO XXX": "y.ndim <= 1"},
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(y.sparse.to_coo())"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, dtype=np.float64), 'dtype')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype is None"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype, 'kind')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype.kind != 'c'"
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
                                                    {"XXX TODO XXX": "sp.issparse(y)"},
                                                    {
                                                        "XXX TODO XXX": "not hasattr(np.asarray(y, None, dtype=np.float64), 'dtype')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype is None"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(np.asarray(y, None, dtype=np.float64).dtype, 'kind')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype.kind != 'c'"
                                                    },
                                                ]
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
                    {"XXX TODO XXX": "not hasattr(getattr(y, 'dtype', None), 'kind')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {"XXX TODO XXX": "not hasattr(y, 'dtypes')"},
                                    {
                                        "XXX TODO XXX": "not hasattr(y.dtypes, '__array__')"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "not all((False for 'numeric' in list(y.dtypes)))"
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
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, dtype=np.float64), 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype, 'kind')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype.kind != 'c'"
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
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(y, None, dtype=np.float64), 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(y, None, dtype=np.float64).dtype, 'kind')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype.kind != 'c'"
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "all((False for 'numeric' in list(y.dtypes)))"
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
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, dtype=np.float64), 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype, 'kind')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype.kind != 'c'"
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
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(y, None, dtype=np.float64), 'dtype')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype is None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(y, None, dtype=np.float64).dtype, 'kind')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype.kind != 'c'"
                                                                    },
                                                                ]
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
                                            {"XXX TODO XXX": "hasattr(y, 'dtypes')"},
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
                                                    {"XXX TODO XXX": "y.ndim <= 1"},
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(y.sparse.to_coo())"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, dtype=np.float64), 'dtype')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype is None"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype, 'kind')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype.kind != 'c'"
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
                                                    {"XXX TODO XXX": "sp.issparse(y)"},
                                                    {
                                                        "XXX TODO XXX": "not hasattr(np.asarray(y, None, dtype=np.float64), 'dtype')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype is None"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not hasattr(np.asarray(y, None, dtype=np.float64).dtype, 'kind')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype.kind != 'c'"
                                                    },
                                                ]
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
                    {"XXX TODO XXX": "hasattr(getattr(y, 'dtype', None), 'kind')"},
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
                                    {"XXX TODO XXX": "not hasattr(y, 'sparse')"},
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
                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(y.sparse.to_coo(), False, dtype=np.float64, False, True, True), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(y.sparse.to_coo(), False, dtype=np.float64, False, True, True).fit)"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(y.sparse.to_coo())"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, dtype=np.float64).astype(np.float64), 'fit')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not callable(np.asarray(y.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).fit)"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, dtype=np.float64), 'fit')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not callable(np.asarray(y.sparse.to_coo(), None, dtype=np.float64).fit)"
                                                                    },
                                                                ]
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
                                            {"XXX TODO XXX": "hasattr(y, 'sparse')"},
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
                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(y, False, dtype=np.float64, False, True, True), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(y, False, dtype=np.float64, False, True, True).fit)"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {"XXX TODO XXX": "sp.issparse(y)"},
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(y, None, dtype=np.float64).astype(np.float64), 'fit')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not callable(np.asarray(y, None, dtype=np.float64).astype(np.float64).fit)"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(y, None, dtype=np.float64), 'fit')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not callable(np.asarray(y, None, dtype=np.float64).fit)"
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
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
                    {"XXX TODO XXX": "not hasattr(getattr(y, 'dtype', None), 'kind')"},
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
                                    {"XXX TODO XXX": "not hasattr(y, 'sparse')"},
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
                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(y.sparse.to_coo(), False, dtype=np.float64, False, True, True), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(y.sparse.to_coo(), False, dtype=np.float64, False, True, True).fit)"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(y.sparse.to_coo())"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, dtype=np.float64).astype(np.float64), 'fit')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not callable(np.asarray(y.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).fit)"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(y.sparse.to_coo(), None, dtype=np.float64), 'fit')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not callable(np.asarray(y.sparse.to_coo(), None, dtype=np.float64).fit)"
                                                                    },
                                                                ]
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
                                            {"XXX TODO XXX": "hasattr(y, 'sparse')"},
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
                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(y, False, dtype=np.float64, False, True, True), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(y, False, dtype=np.float64, False, True, True).fit)"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {"XXX TODO XXX": "sp.issparse(y)"},
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(y, None, dtype=np.float64).astype(np.float64), 'fit')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not callable(np.asarray(y, None, dtype=np.float64).astype(np.float64).fit)"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not hasattr(np.asarray(y, None, dtype=np.float64), 'fit')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not callable(np.asarray(y, None, dtype=np.float64).fit)"
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
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
                    {"XXX TODO XXX": "hasattr(getattr(y, 'dtype', None), 'kind')"},
                    {
                        "allOf": [
                            {"XXX TODO XXX": "hasattr(y, 'dtypes')"},
                            {"XXX TODO XXX": "hasattr(y.dtypes, '__array__')"},
                        ]
                    },
                    {"XXX TODO XXX": "not hasattr(y, 'sparse')"},
                    {"XXX TODO XXX": "y.ndim <= 1"},
                    {"XXX TODO XXX": "y.sparse.to_coo().dtype != np.dtype('object')"},
                    {
                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in y.dtypes])) <= 1"
                    },
                ]
            },
            {
                "anyOf": [
                    {"XXX TODO XXX": "not hasattr(getattr(y, 'dtype', None), 'kind')"},
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
                                        "XXX TODO XXX": "getattr(y, 'dtype', None) is None"
                                    },
                                    {
                                        "XXX TODO XXX": "getattr(y, 'dtype', None).kind != 'O'"
                                    },
                                    {"XXX TODO XXX": "not hasattr(y, 'sparse')"},
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
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "getattr(y, 'dtype', None) is not None"
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(y, 'dtype', None).kind == 'O'"
                                            },
                                        ]
                                    },
                                    {"XXX TODO XXX": "not hasattr(y, 'sparse')"},
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
        ],
    },
    {
        "description": 'From /utils/validation.py:None:check_array, Exception: raise ValueError("""Complex data not supported {} """.format(array)     ) from complex_warning ',
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
        ],
    },
    {
        "description": "From /utils/validation.py:None:check_array, Exception: raise ValueError(     \"Unable to convert array of bytes/strings into decimal numbers with dtype='numeric'\"     ) from e ",
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "hasattr(getattr(y, 'dtype', None), 'kind')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {"XXX TODO XXX": "not hasattr(y, 'dtypes')"},
                                    {
                                        "XXX TODO XXX": "not hasattr(y.dtypes, '__array__')"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "not all((False for 'numeric' in list(y.dtypes)))"
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
                                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
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
                                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "all((False for 'numeric' in list(y.dtypes)))"
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
                                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
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
                                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                ]
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
                                            {"XXX TODO XXX": "hasattr(y, 'dtypes')"},
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
                                                    {"XXX TODO XXX": "y.ndim <= 1"},
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(y.sparse.to_coo())"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
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
                                                    {"XXX TODO XXX": "sp.issparse(y)"},
                                                    {
                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                    },
                                                ]
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
                    {"XXX TODO XXX": "not hasattr(getattr(y, 'dtype', None), 'kind')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {"XXX TODO XXX": "not hasattr(y, 'dtypes')"},
                                    {
                                        "XXX TODO XXX": "not hasattr(y.dtypes, '__array__')"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "not all((False for 'numeric' in list(y.dtypes)))"
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
                                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
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
                                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "all((False for 'numeric' in list(y.dtypes)))"
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
                                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
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
                                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                ]
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
                                            {"XXX TODO XXX": "hasattr(y, 'dtypes')"},
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
                                                    {"XXX TODO XXX": "y.ndim <= 1"},
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(y.sparse.to_coo())"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
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
                                                    {"XXX TODO XXX": "sp.issparse(y)"},
                                                    {
                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                    },
                                                ]
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
                    {"XXX TODO XXX": "hasattr(getattr(y, 'dtype', None), 'kind')"},
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
                                    {"XXX TODO XXX": "not hasattr(y, 'sparse')"},
                                    {"XXX TODO XXX": "y.ndim <= 1"},
                                    {"XXX TODO XXX": "sp.issparse(y.sparse.to_coo())"},
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).ndim < 3"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).ndim < 3"
                                                    },
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
                                            {"XXX TODO XXX": "hasattr(y, 'sparse')"},
                                            {"XXX TODO XXX": "y.ndim > 1"},
                                        ]
                                    },
                                    {"XXX TODO XXX": "sp.issparse(y)"},
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).astype(np.float64).ndim < 3"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).ndim < 3"
                                                    },
                                                ]
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
                    {"XXX TODO XXX": "not hasattr(getattr(y, 'dtype', None), 'kind')"},
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
                                    {"XXX TODO XXX": "not hasattr(y, 'sparse')"},
                                    {"XXX TODO XXX": "y.ndim <= 1"},
                                    {"XXX TODO XXX": "sp.issparse(y.sparse.to_coo())"},
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).ndim < 3"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).ndim < 3"
                                                    },
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
                                            {"XXX TODO XXX": "hasattr(y, 'sparse')"},
                                            {"XXX TODO XXX": "y.ndim > 1"},
                                        ]
                                    },
                                    {"XXX TODO XXX": "sp.issparse(y)"},
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).astype(np.float64).ndim < 3"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).ndim < 3"
                                                    },
                                                ]
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
                    {"XXX TODO XXX": "hasattr(getattr(y, 'dtype', None), 'kind')"},
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
                                    {"XXX TODO XXX": "not hasattr(y, 'sparse')"},
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
                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(y.sparse.to_coo(), False, dtype=np.float64, False, True, True)) >= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(y.sparse.to_coo())"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "_num_samples(np.asarray(y.sparse.to_coo(), None, dtype=np.float64).astype(np.float64)) >= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "_num_samples(np.asarray(y.sparse.to_coo(), None, dtype=np.float64)) >= 1"
                                                                    },
                                                                ]
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
                                            {"XXX TODO XXX": "hasattr(y, 'sparse')"},
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
                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(y, False, dtype=np.float64, False, True, True)) >= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {"XXX TODO XXX": "sp.issparse(y)"},
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "_num_samples(np.asarray(y, None, dtype=np.float64).astype(np.float64)) >= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "_num_samples(np.asarray(y, None, dtype=np.float64)) >= 1"
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
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
                    {"XXX TODO XXX": "not hasattr(getattr(y, 'dtype', None), 'kind')"},
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
                                    {"XXX TODO XXX": "not hasattr(y, 'sparse')"},
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
                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(y.sparse.to_coo(), False, dtype=np.float64, False, True, True)) >= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(y.sparse.to_coo())"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "_num_samples(np.asarray(y.sparse.to_coo(), None, dtype=np.float64).astype(np.float64)) >= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "_num_samples(np.asarray(y.sparse.to_coo(), None, dtype=np.float64)) >= 1"
                                                                    },
                                                                ]
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
                                            {"XXX TODO XXX": "hasattr(y, 'sparse')"},
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
                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(y, False, dtype=np.float64, False, True, True)) >= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {"XXX TODO XXX": "sp.issparse(y)"},
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "_num_samples(np.asarray(y, None, dtype=np.float64).astype(np.float64)) >= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "_num_samples(np.asarray(y, None, dtype=np.float64)) >= 1"
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
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
                    {"XXX TODO XXX": "hasattr(getattr(y, 'dtype', None), 'kind')"},
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
                                    {"XXX TODO XXX": "not hasattr(y, 'sparse')"},
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
                                                        "XXX TODO XXX": "_ensure_sparse_format(y.sparse.to_coo(), False, dtype=np.float64, False, True, True).ndim != 2"
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
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).ndim != 2"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "array.shape[1] >= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).ndim != 2"
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
                                            {"XXX TODO XXX": "hasattr(y, 'sparse')"},
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
                                                        "XXX TODO XXX": "_ensure_sparse_format(y, False, dtype=np.float64, False, True, True).ndim != 2"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "array.shape[1] >= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {"XXX TODO XXX": "sp.issparse(y)"},
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).astype(np.float64).ndim != 2"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "array.shape[1] >= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).ndim != 2"
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
                    {"XXX TODO XXX": "not hasattr(getattr(y, 'dtype', None), 'kind')"},
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
                                    {"XXX TODO XXX": "not hasattr(y, 'sparse')"},
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
                                                        "XXX TODO XXX": "_ensure_sparse_format(y.sparse.to_coo(), False, dtype=np.float64, False, True, True).ndim != 2"
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
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).ndim != 2"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "array.shape[1] >= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y.sparse.to_coo(), None, dtype=np.float64).ndim != 2"
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
                                            {"XXX TODO XXX": "hasattr(y, 'sparse')"},
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
                                                        "XXX TODO XXX": "_ensure_sparse_format(y, False, dtype=np.float64, False, True, True).ndim != 2"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "array.shape[1] >= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {"XXX TODO XXX": "sp.issparse(y)"},
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype.kind not in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).astype(np.float64).ndim != 2"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "array.shape[1] >= 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).dtype.kind in 'OUSV'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "np.asarray(y, None, dtype=np.float64).ndim != 2"
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
        "description": "From /base.py:None:clone, Exception: raise TypeError('Cannot clone object. ' +     'You should provide an instance of ' +     'scikit-learn estimator instead of a class.') ",
        "anyOf": [
            {
                "allOf": [
                    {
                        "type": "object",
                        "properties": {"transformer": {"not": {"enum": [None]}}},
                    },
                    {
                        "anyOf": [
                            {
                                "type": "object",
                                "properties": {"func": {"not": {"enum": [None]}}},
                            },
                            {
                                "type": "object",
                                "properties": {
                                    "inverse_func": {"not": {"enum": [None]}}
                                },
                            },
                        ]
                    },
                ]
            },
            {"type": "object", "properties": {"transformer": {"enum": [None]}}},
            {"XXX TODO XXX": "type(self.transformer) in [list, tuple, set, frozenset]"},
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(self.transformer, 'get_params')"},
                    {"XXX TODO XXX": "isinstance(self.transformer, type)"},
                ]
            },
            {"XXX TODO XXX": "isinstance(self.transformer, type)"},
        ],
    },
    {
        "description": "From /base.py:None:clone, Exception: raise TypeError(     \"Cannot clone object '%s' (type %s): it does not seem to be a scikit-learn estimator as it does not implement a 'get_params' method.\"      % (repr(estimator), type(estimator))) ",
        "anyOf": [
            {
                "allOf": [
                    {
                        "type": "object",
                        "properties": {"transformer": {"not": {"enum": [None]}}},
                    },
                    {
                        "anyOf": [
                            {
                                "type": "object",
                                "properties": {"func": {"not": {"enum": [None]}}},
                            },
                            {
                                "type": "object",
                                "properties": {
                                    "inverse_func": {"not": {"enum": [None]}}
                                },
                            },
                        ]
                    },
                ]
            },
            {"type": "object", "properties": {"transformer": {"enum": [None]}}},
            {"XXX TODO XXX": "type(self.transformer) in [list, tuple, set, frozenset]"},
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(self.transformer, 'get_params')"},
                    {"XXX TODO XXX": "isinstance(self.transformer, type)"},
                ]
            },
            {"XXX TODO XXX": "isinstance(self.transformer, type)"},
        ],
    },
    {
        "description": "From /base.py:None:clone, Exception: raise RuntimeError(     'Cannot clone object %s, as the constructor either does not set or modifies parameter %s'      % (estimator, name)) ",
        "anyOf": [
            {
                "allOf": [
                    {
                        "type": "object",
                        "properties": {"transformer": {"not": {"enum": [None]}}},
                    },
                    {
                        "anyOf": [
                            {
                                "type": "object",
                                "properties": {"func": {"not": {"enum": [None]}}},
                            },
                            {
                                "type": "object",
                                "properties": {
                                    "inverse_func": {"not": {"enum": [None]}}
                                },
                            },
                        ]
                    },
                ]
            },
            {"type": "object", "properties": {"transformer": {"enum": [None]}}},
            {"XXX TODO XXX": "name not in self.transformer.get_params(False)"},
            {"XXX TODO XXX": "new_object_params[name] is params_set[name]"},
        ],
    },
    {
        "description": "From /utils/__init__.py:None:_determine_key_type, Exception: raise ValueError(err_msg) ",
        "anyOf": [
            {"type": "object", "properties": {"check_inverse": {"enum": [False]}}},
            {"XXX TODO XXX": "slice(None, None, max(1, y.shape[0] // 10)) is None"},
            {"XXX TODO XXX": "slice(None, None, max(1, y.shape[0] // 10)) is None"},
            {
                "XXX TODO XXX": "isinstance(slice(None, None, max(1, y.shape[0] // 10)), tuple({int: 'int', str: 'str', bool: 'bool', np.bool_: 'bool'}.keys()))"
            },
        ],
    },
    {
        "description": "From /utils/__init__.py:None:_determine_key_type, Exception: raise ValueError(err_msg) ",
        "anyOf": [
            {"type": "object", "properties": {"check_inverse": {"enum": [False]}}},
            {"XXX TODO XXX": "slice(None, None, max(1, y.shape[0] // 10)) is None"},
            {"XXX TODO XXX": "slice(None, None, max(1, y.shape[0] // 10)) is None"},
            {
                "XXX TODO XXX": "isinstance(slice(None, None, max(1, y.shape[0] // 10)), tuple({int: 'int', str: 'str', bool: 'bool', np.bool_: 'bool'}.keys()))"
            },
            {
                "XXX TODO XXX": "isinstance(slice(None, None, max(1, y.shape[0] // 10)), slice)"
            },
            {
                "allOf": [
                    {
                        "XXX TODO XXX": "slice(None, None, max(1, y.shape[0] // 10)).start is None"
                    },
                    {
                        "XXX TODO XXX": "slice(None, None, max(1, y.shape[0] // 10)).stop is None"
                    },
                ]
            },
            {
                "XXX TODO XXX": "_determine_key_type(slice(None, None, max(1, y.shape[0] // 10)).start) is None"
            },
            {
                "XXX TODO XXX": "_determine_key_type(slice(None, None, max(1, y.shape[0] // 10)).stop) is None"
            },
            {
                "XXX TODO XXX": "_determine_key_type(slice(None, None, max(1, y.shape[0] // 10)).start) == _determine_key_type(slice(None, None, max(1, y.shape[0] // 10)).stop)"
            },
        ],
    },
    {
        "description": "From /utils/__init__.py:None:_determine_key_type, Exception: raise ValueError(err_msg) ",
        "anyOf": [
            {"type": "object", "properties": {"check_inverse": {"enum": [False]}}},
            {"XXX TODO XXX": "slice(None, None, max(1, y.shape[0] // 10)) is None"},
            {"XXX TODO XXX": "slice(None, None, max(1, y.shape[0] // 10)) is None"},
            {
                "XXX TODO XXX": "isinstance(slice(None, None, max(1, y.shape[0] // 10)), tuple({int: 'int', str: 'str', bool: 'bool', np.bool_: 'bool'}.keys()))"
            },
            {
                "XXX TODO XXX": "isinstance(slice(None, None, max(1, y.shape[0] // 10)), slice)"
            },
            {
                "XXX TODO XXX": "isinstance(slice(None, None, max(1, y.shape[0] // 10)), [list, tuple])"
            },
            {
                "XXX TODO XXX": "not {_determine_key_type(elt) for elt in set(slice(None, None, max(1, y.shape[0] // 10)))}"
            },
            {
                "XXX TODO XXX": "len({_determine_key_type(elt) for elt in set(slice(None, None, max(1, y.shape[0] // 10)))}) == 1"
            },
        ],
    },
    {
        "description": "From /utils/__init__.py:None:_determine_key_type, Exception: raise ValueError(err_msg) ",
        "anyOf": [
            {"type": "object", "properties": {"check_inverse": {"enum": [False]}}},
            {"XXX TODO XXX": "slice(None, None, max(1, y.shape[0] // 10)) is None"},
            {"XXX TODO XXX": "slice(None, None, max(1, y.shape[0] // 10)) is None"},
            {
                "XXX TODO XXX": "isinstance(slice(None, None, max(1, y.shape[0] // 10)), tuple({int: 'int', str: 'str', bool: 'bool', np.bool_: 'bool'}.keys()))"
            },
            {
                "XXX TODO XXX": "isinstance(slice(None, None, max(1, y.shape[0] // 10)), slice)"
            },
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "isinstance(slice(None, None, max(1, y.shape[0] // 10)), [list, tuple])"
                            },
                            {
                                "XXX TODO XXX": "not {_determine_key_type(elt) for elt in set(slice(None, None, max(1, y.shape[0] // 10)))}"
                            },
                            {
                                "XXX TODO XXX": "not hasattr(slice(None, None, max(1, y.shape[0] // 10)), 'dtype')"
                            },
                        ]
                    },
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "isinstance(slice(None, None, max(1, y.shape[0] // 10)), [list, tuple])"
                            },
                            {
                                "XXX TODO XXX": "not hasattr(slice(None, None, max(1, y.shape[0] // 10)), 'dtype')"
                            },
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": "From /utils/__init__.py:None:_determine_key_type, Exception: raise ValueError(err_msg) ",
        "anyOf": [
            {"type": "object", "properties": {"check_inverse": {"enum": [False]}}},
            {"XXX TODO XXX": "slice(None, None, max(1, y.shape[0] // 10)) is None"},
            {"XXX TODO XXX": "slice(None, None, max(1, y.shape[0] // 10)) is None"},
            {
                "XXX TODO XXX": "isinstance(slice(None, None, max(1, y.shape[0] // 10)), tuple({int: 'int', str: 'str', bool: 'bool', np.bool_: 'bool'}.keys()))"
            },
            {
                "XXX TODO XXX": "isinstance(slice(None, None, max(1, y.shape[0] // 10)), slice)"
            },
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "isinstance(slice(None, None, max(1, y.shape[0] // 10)), [list, tuple])"
                            },
                            {
                                "XXX TODO XXX": "not {_determine_key_type(elt) for elt in set(slice(None, None, max(1, y.shape[0] // 10)))}"
                            },
                            {
                                "XXX TODO XXX": "hasattr(slice(None, None, max(1, y.shape[0] // 10)), 'dtype')"
                            },
                        ]
                    },
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "isinstance(slice(None, None, max(1, y.shape[0] // 10)), [list, tuple])"
                            },
                            {
                                "XXX TODO XXX": "hasattr(slice(None, None, max(1, y.shape[0] // 10)), 'dtype')"
                            },
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": "From /utils/__init__.py:None:_safe_indexing, Exception: raise ValueError(\"String indexing is not supported with 'axis=0'\") ",
        "anyOf": [
            {"type": "object", "properties": {"check_inverse": {"enum": [False]}}},
            {"XXX TODO XXX": "slice(None, None, max(1, y.shape[0] // 10)) is None"},
            {
                "XXX TODO XXX": "_determine_key_type(slice(None, None, max(1, y.shape[0] // 10))) != 'str'"
            },
        ],
    },
    {
        "description": "From /compose/_target.py:TransformedTargetRegressor:_fit_transformer, Exception: raise ValueError(     \"'transformer' and functions 'func'/'inverse_func' cannot both be set.\") ",
        "anyOf": [
            {"type": "object", "properties": {"transformer": {"enum": [None]}}},
            {
                "allOf": [
                    {"type": "object", "properties": {"func": {"enum": [None]}}},
                    {
                        "type": "object",
                        "properties": {"inverse_func": {"enum": [None]}},
                    },
                ]
            },
        ],
    },
    {
        "description": "From /compose/_target.py:TransformedTargetRegressor:_fit_transformer, Exception: raise ValueError(     \"When 'func' is provided, 'inverse_func' must also be provided\") ",
        "anyOf": [
            {
                "allOf": [
                    {
                        "type": "object",
                        "properties": {"transformer": {"not": {"enum": [None]}}},
                    },
                    {
                        "anyOf": [
                            {
                                "type": "object",
                                "properties": {"func": {"not": {"enum": [None]}}},
                            },
                            {
                                "type": "object",
                                "properties": {
                                    "inverse_func": {"not": {"enum": [None]}}
                                },
                            },
                        ]
                    },
                ]
            },
            {
                "type": "object",
                "properties": {"transformer": {"not": {"enum": [None]}}},
            },
            {"type": "object", "properties": {"func": {"enum": [None]}}},
            {
                "type": "object",
                "properties": {"inverse_func": {"not": {"enum": [None]}}},
            },
        ],
    },
    {
        "description": "From /base.py:None:clone, Exception: raise TypeError('Cannot clone object. ' +     'You should provide an instance of ' +     'scikit-learn estimator instead of a class.') ",
        "anyOf": [
            {"type": "object", "properties": {"regressor": {"enum": [None]}}},
            {"XXX TODO XXX": "type(self.regressor) in [list, tuple, set, frozenset]"},
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(self.regressor, 'get_params')"},
                    {"XXX TODO XXX": "isinstance(self.regressor, type)"},
                ]
            },
            {"XXX TODO XXX": "isinstance(self.regressor, type)"},
        ],
    },
    {
        "description": "From /base.py:None:clone, Exception: raise TypeError(     \"Cannot clone object '%s' (type %s): it does not seem to be a scikit-learn estimator as it does not implement a 'get_params' method.\"      % (repr(estimator), type(estimator))) ",
        "anyOf": [
            {"type": "object", "properties": {"regressor": {"enum": [None]}}},
            {"XXX TODO XXX": "type(self.regressor) in [list, tuple, set, frozenset]"},
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(self.regressor, 'get_params')"},
                    {"XXX TODO XXX": "isinstance(self.regressor, type)"},
                ]
            },
            {"XXX TODO XXX": "isinstance(self.regressor, type)"},
        ],
    },
    {
        "description": "From /base.py:None:clone, Exception: raise RuntimeError(     'Cannot clone object %s, as the constructor either does not set or modifies parameter %s'      % (estimator, name)) ",
        "anyOf": [
            {"type": "object", "properties": {"regressor": {"enum": [None]}}},
            {"XXX TODO XXX": "name not in self.regressor.get_params(False)"},
            {"XXX TODO XXX": "new_object_params[name] is params_set[name]"},
        ],
    },
]
