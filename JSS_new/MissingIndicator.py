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
                                                    {"XXX TODO XXX": "sp.issparse(X)"},
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
                                                    {"XXX TODO XXX": "sp.issparse(X)"},
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
                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr'], None, False, True, True), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr'], None, False, True, True).fit)"
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
                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse=['csc', 'csr'], None, False, True, True), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse=['csc', 'csr'], None, False, True, True).fit)"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {"XXX TODO XXX": "sp.issparse(X)"},
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
                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr'], None, False, True, True), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr'], None, False, True, True).fit)"
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
                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse=['csc', 'csr'], None, False, True, True), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse=['csc', 'csr'], None, False, True, True).fit)"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {"XXX TODO XXX": "sp.issparse(X)"},
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
        ],
    },
    {
        "description": "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Pandas DataFrame with mixed sparse extension arrays generated a sparse matrix with object dtype which can not be converted to a scipy sparse matrix.Sparse extension arrays should all have the same numeric type.'     ) ",
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "is_scalar_nan(self.missing_values)"},
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
                                            {
                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
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
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                                    },
                                    {
                                        "allOf": [
                                            {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                                            {
                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
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
            {
                "anyOf": [
                    {"XXX TODO XXX": "not is_scalar_nan(self.missing_values)"},
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
                                            {
                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
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
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "not hasattr(getattr(X, 'dtype', None), 'kind')"
                                    },
                                    {
                                        "allOf": [
                                            {"XXX TODO XXX": "hasattr(X, 'dtypes')"},
                                            {
                                                "XXX TODO XXX": "hasattr(X.dtypes, '__array__')"
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
                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).ndim < 3"
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
                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, None).ndim < 3"
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
                                        "XXX TODO XXX": "np.asarray(X, None, None).ndim < 3"
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
                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr'], None, False, True, True)) >= 1"
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
                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse=['csc', 'csr'], None, False, True, True)) >= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {"XXX TODO XXX": "sp.issparse(X)"},
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
                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr'], None, False, True, True)) >= 1"
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
                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse=['csc', 'csr'], None, False, True, True)) >= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {"XXX TODO XXX": "sp.issparse(X)"},
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
                                                        "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr'], None, False, True, True).ndim != 2"
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
                                                        "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse=['csc', 'csr'], None, False, True, True).ndim != 2"
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
                                                        "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr'], None, False, True, True).ndim != 2"
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
                                                        "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse=['csc', 'csr'], None, False, True, True).ndim != 2"
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
        ],
    },
    {
        "description": "From /impute/_base.py:None:_check_inputs_dtype, Exception: raise ValueError(     \"'X' and 'missing_values' types are expected to be both numerical. Got X.dtype={} and  type(missing_values)={}.\"     .format(X.dtype, type(missing_values))) ",
        "anyOf": [
            {"XXX TODO XXX": "X.dtype.kind not in ['f', 'i', 'u']"},
            {"type": "object", "properties": {"missing_values": {"type": "number"}}},
        ],
    },
    {
        "description": "From /impute/_base.py:MissingIndicator:_validate_input, Exception: raise ValueError(     'MissingIndicator does not support data with dtype {0}. Please provide either a numeric array (with a floating point or integer dtype) or categorical data represented either as an array with integer dtype or an array of string values with an object dtype.'     .format(X.dtype)) ",
        "XXX TODO XXX": "X.dtype.kind in ['i', 'u', 'f', 'O']",
    },
    {
        "description": "From /impute/_base.py:MissingIndicator:_validate_input, Exception: raise ValueError(     'Sparse input with missing_values=0 is not supported. Provide a dense array instead.'     ) ",
        "anyOf": [
            {"type": "object", "laleNot": "X/isSparse"},
            {
                "type": "object",
                "properties": {"missing_values": {"not": {"enum": [0]}}},
            },
        ],
    },
    {
        "description": "From /impute/_base.py:MissingIndicator:_fit, Exception: raise ValueError(     \"'features' has to be either 'missing-only' or 'all'. Got {} instead.\".     format(self.features)) ",
        "type": "object",
        "properties": {"features": {"enum": ["missing-only", "all"]}},
    },
    {
        "description": "From /impute/_base.py:MissingIndicator:_fit, Exception: raise ValueError(\"'sparse' has to be a boolean or 'auto'. Got {!r} instead.\"     .format(self.sparse)) ",
        "anyOf": [
            {
                "allOf": [
                    {"type": "object", "properties": {"sparse": {"type": "string"}}},
                    {"type": "object", "properties": {"sparse": {"enum": ["auto"]}}},
                ]
            },
            {"type": "object", "properties": {"sparse": {"type": "boolean"}}},
        ],
    },
]
