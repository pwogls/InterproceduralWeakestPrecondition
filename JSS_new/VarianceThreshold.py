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
                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], dtype=np.float64, False, force_all_finite='allow-nan', True), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], dtype=np.float64, False, force_all_finite='allow-nan', True).fit)"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
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
                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], dtype=np.float64, False, force_all_finite='allow-nan', True), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], dtype=np.float64, False, force_all_finite='allow-nan', True).fit)"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {"XXX TODO XXX": "sp.issparse(X)"},
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
                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], dtype=np.float64, False, force_all_finite='allow-nan', True), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], dtype=np.float64, False, force_all_finite='allow-nan', True).fit)"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
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
                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], dtype=np.float64, False, force_all_finite='allow-nan', True), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], dtype=np.float64, False, force_all_finite='allow-nan', True).fit)"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {"XXX TODO XXX": "sp.issparse(X)"},
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
                    {"XXX TODO XXX": "not hasattr(X, 'sparse')"},
                    {"XXX TODO XXX": "X.ndim <= 1"},
                    {"XXX TODO XXX": "X.sparse.to_coo().dtype != np.dtype('object')"},
                    {
                        "XXX TODO XXX": "len(set([dt.subtype.name for dt in X.dtypes])) <= 1"
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
                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).ndim < 3"
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
                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).ndim < 3"
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
                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).ndim < 3"
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
                                        "XXX TODO XXX": "np.asarray(X, None, dtype=np.float64).ndim < 3"
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
                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], dtype=np.float64, False, force_all_finite='allow-nan', True)) >= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
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
                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], dtype=np.float64, False, force_all_finite='allow-nan', True)) >= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {"XXX TODO XXX": "sp.issparse(X)"},
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
                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], dtype=np.float64, False, force_all_finite='allow-nan', True)) >= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "sp.issparse(X.sparse.to_coo())"
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
                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], dtype=np.float64, False, force_all_finite='allow-nan', True)) >= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {"XXX TODO XXX": "sp.issparse(X)"},
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
                                                        "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], dtype=np.float64, False, force_all_finite='allow-nan', True).ndim != 2"
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
                                                        "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], dtype=np.float64, False, force_all_finite='allow-nan', True).ndim != 2"
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
                                                        "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], dtype=np.float64, False, force_all_finite='allow-nan', True).ndim != 2"
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
                                                        "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], dtype=np.float64, False, force_all_finite='allow-nan', True).ndim != 2"
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
        ],
    },
    {
        "description": "From /utils/sparsefuncs.py:None:_raise_typeerror, Exception: raise TypeError(err) ",
        "anyOf": [
            {"XXX TODO XXX": "not hasattr(X, 'toarray')"},
            {"XXX TODO XXX": "isinstance(X, sp.csr_matrix)"},
            {"XXX TODO XXX": "isinstance(X, sp.csc_matrix)"},
        ],
    },
    {
        "description": "From /utils/sparsefuncs.py:None:_raise_typeerror, Exception: raise TypeError(err) ",
        "anyOf": [
            {"XXX TODO XXX": "not hasattr(X, 'toarray')"},
            {"type": "object", "properties": {"threshold": {"not": {"enum": [0]}}}},
            {"XXX TODO XXX": "isinstance(X, sp.csr_matrix)"},
            {"XXX TODO XXX": "isinstance(X, sp.csc_matrix)"},
        ],
    },
    {
        "description": "From /feature_selection/_variance_threshold.py:VarianceThreshold:fit, Exception: raise ValueError(msg.format(self.threshold)) ",
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "not hasattr(X, 'toarray')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "threshold": {"not": {"enum": [0]}}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "threshold": {"not": {"enum": [0]}}
                                        },
                                    },
                                    {
                                        "XXX TODO XXX": "not np.all(~np.isfinite(np.nanmin(np.array([mean_variance_axis(X, axis=0)[1], min_max_axis(X, axis=0)[1] - min_max_axis(X, axis=0)[0]]), 0)) | (np.nanmin(np.array([mean_variance_axis(X, axis=0)[1], min_max_axis(X, axis=0)[1] - min_max_axis(X, axis=0)[0]]), 0) <= self.threshold))"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {"threshold": {"enum": [0]}},
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "threshold": {"not": {"enum": [0]}}
                                        },
                                    },
                                    {
                                        "XXX TODO XXX": "not np.all(~np.isfinite(np.nanmin(np.array([mean_variance_axis(X, axis=0)[1], peak_to_peaks]), 0)) | (np.nanmin(np.array([mean_variance_axis(X, axis=0)[1], peak_to_peaks]), 0) <= self.threshold))"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {"threshold": {"enum": [0]}},
                                    },
                                    {
                                        "XXX TODO XXX": "not np.all(~np.isfinite(mean_variance_axis(X, axis=0)[1]) | (mean_variance_axis(X, axis=0)[1] <= self.threshold))"
                                    },
                                ]
                            },
                        ]
                    },
                ]
            },
            {
                "anyOf": [
                    {"XXX TODO XXX": "hasattr(X, 'toarray')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "threshold": {"not": {"enum": [0]}}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "threshold": {"not": {"enum": [0]}}
                                        },
                                    },
                                    {
                                        "XXX TODO XXX": "not np.all(~np.isfinite(np.nanmin(np.array([np.nanvar(X, axis=0), np.ptp(X, 0)]), 0)) | (np.nanmin(np.array([np.nanvar(X, axis=0), np.ptp(X, 0)]), 0) <= self.threshold))"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {"threshold": {"enum": [0]}},
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "threshold": {"not": {"enum": [0]}}
                                        },
                                    },
                                    {
                                        "XXX TODO XXX": "not np.all(~np.isfinite(np.nanmin(np.array([np.nanvar(X, axis=0), peak_to_peaks]), 0)) | (np.nanmin(np.array([np.nanvar(X, axis=0), peak_to_peaks]), 0) <= self.threshold))"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {"threshold": {"enum": [0]}},
                                    },
                                    {
                                        "XXX TODO XXX": "not np.all(~np.isfinite(np.nanvar(X, axis=0)) | (np.nanvar(X, axis=0) <= self.threshold))"
                                    },
                                ]
                            },
                        ]
                    },
                ]
            },
        ],
    },
]
