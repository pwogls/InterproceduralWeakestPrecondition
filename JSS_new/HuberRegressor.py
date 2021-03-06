[
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], dtype=dtype[0], False, True, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], dtype=dtype[0], False, True, True).fit)"
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
                                                                                "XXX TODO XXX": "dtype[0] is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).fit)"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).fit)"
                                                                            },
                                                                        ]
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse=['csr'], dtype=dtype[0], False, True, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse=['csr'], dtype=dtype[0], False, True, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).fit)"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(np.asarray(X, None, dtype=dtype[0]).fit)"
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
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
                                                "XXX TODO XXX": "getattr(X, 'dtype', None) is None"
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(X, 'dtype', None) not in [np.float64, np.float32]"
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
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "laleNot": "X/isSparse",
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], None, False, True, True), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], None, False, True, True).fit)"
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
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
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
                                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse=['csr'], None, False, True, True), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse=['csr'], None, False, True, True).fit)"
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
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) is not None"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) in [np.float64, np.float32]"
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
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "laleNot": "X/isSparse",
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], dtype=dtype[0], False, True, True), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], dtype=dtype[0], False, True, True).fit)"
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
                                                                                                "XXX TODO XXX": "dtype[0] is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'fit')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).fit)"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'fit')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).fit)"
                                                                                            },
                                                                                        ]
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
                                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
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
                                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse=['csr'], dtype=dtype[0], False, True, True), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse=['csr'], dtype=dtype[0], False, True, True).fit)"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'fit')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not callable(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).fit)"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'fit')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not callable(np.asarray(X, None, dtype=dtype[0]).fit)"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                ]
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
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
                                                                "XXX TODO XXX": "not all((False for [np.float64, np.float32] in list(X.dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "np.result_type(*list(X.dtypes)) is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.result_type(*list(X.dtypes)) not in [np.float64, np.float32]"
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
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "np.result_type(*list(X.dtypes)) is not None"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "np.result_type(*list(X.dtypes)) in [np.float64, np.float32]"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                                            },
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
                                                                                                    {
                                                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                                                    },
                                                                                                ]
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                                            },
                                                                                                        ]
                                                                                                    },
                                                                                                ]
                                                                                            },
                                                                                        ]
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
                                                                "XXX TODO XXX": "all((False for [np.float64, np.float32] in list(X.dtypes)))"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'dtype')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype, 'kind')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                            },
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
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'dtype')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]).dtype, 'kind')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                ]
                                                                            },
                                                                        ]
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                            },
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
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
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
                                                                "XXX TODO XXX": "not all((False for [np.float64, np.float32] in list(X.dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "np.result_type(*list(X.dtypes)) is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.result_type(*list(X.dtypes)) not in [np.float64, np.float32]"
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
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "np.result_type(*list(X.dtypes)) is not None"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "np.result_type(*list(X.dtypes)) in [np.float64, np.float32]"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                                            },
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
                                                                                                    {
                                                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                                                    },
                                                                                                ]
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                                            },
                                                                                                        ]
                                                                                                    },
                                                                                                ]
                                                                                            },
                                                                                        ]
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
                                                                "XXX TODO XXX": "all((False for [np.float64, np.float32] in list(X.dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "getattr(X, 'dtype', None) is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "getattr(X, 'dtype', None) not in [np.float64, np.float32]"
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
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) is not None"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) in [np.float64, np.float32]"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                                            },
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
                                                                                                    {
                                                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                                                    },
                                                                                                ]
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                                            },
                                                                                                        ]
                                                                                                    },
                                                                                                ]
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                ]
                                                                            },
                                                                        ]
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
                                                                "XXX TODO XXX": "getattr(X, 'dtype', None) is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "getattr(X, 'dtype', None) not in [np.float64, np.float32]"
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
                                                                "allOf": [
                                                                    {
                                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) is not None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) in [np.float64, np.float32]"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'dtype')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype, 'kind')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                            },
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
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'dtype')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]).dtype, 'kind')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                ]
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
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
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "getattr(X, 'dtype', None) is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "getattr(X, 'dtype', None) not in [np.float64, np.float32]"
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
                                                                "allOf": [
                                                                    {
                                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) is not None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) in [np.float64, np.float32]"
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
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "getattr(X, 'dtype', None) is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "getattr(X, 'dtype', None) not in [np.float64, np.float32]"
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
                                                                "allOf": [
                                                                    {
                                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) is not None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) in [np.float64, np.float32]"
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
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).ndim < 3"
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
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).ndim < 3"
                                                            },
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
                                            {"XXX TODO XXX": "sp.issparse(X)"},
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
                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).ndim < 3"
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
                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).ndim < 3"
                                                            },
                                                        ]
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
                                                "XXX TODO XXX": "getattr(X, 'dtype', None) is None"
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(X, 'dtype', None) not in [np.float64, np.float32]"
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
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
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
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) is not None"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) in [np.float64, np.float32]"
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
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).ndim < 3"
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
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).ndim < 3"
                                                                            },
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
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).ndim < 3"
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
                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).ndim < 3"
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], dtype=dtype[0], False, True, True)) >= 1"
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
                                                                                "XXX TODO XXX": "dtype[0] is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False)) >= 1"
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
                                                                                "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0])) >= 1"
                                                                            },
                                                                        ]
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse=['csr'], dtype=dtype[0], False, True, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                "XXX TODO XXX": "_num_samples(np.asarray(X, None).astype(dtype[0], casting='unsafe', False)) >= 1"
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
                                                                                "XXX TODO XXX": "_num_samples(np.asarray(X, None, dtype=dtype[0])) >= 1"
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
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
                                                "XXX TODO XXX": "getattr(X, 'dtype', None) is None"
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(X, 'dtype', None) not in [np.float64, np.float32]"
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
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "laleNot": "X/isSparse",
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], None, False, True, True)) >= 1"
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
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
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
                                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse=['csr'], None, False, True, True)) >= 1"
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
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) is not None"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) in [np.float64, np.float32]"
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
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "laleNot": "X/isSparse",
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], dtype=dtype[0], False, True, True)) >= 1"
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
                                                                                                "XXX TODO XXX": "dtype[0] is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False)) >= 1"
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
                                                                                                "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0])) >= 1"
                                                                                            },
                                                                                        ]
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
                                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
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
                                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse=['csr'], dtype=dtype[0], False, True, True)) >= 1"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                                "XXX TODO XXX": "_num_samples(np.asarray(X, None).astype(dtype[0], casting='unsafe', False)) >= 1"
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
                                                                                                "XXX TODO XXX": "_num_samples(np.asarray(X, None, dtype=dtype[0])) >= 1"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                ]
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], dtype=dtype[0], False, True, True).ndim != 2"
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
                                                                                "XXX TODO XXX": "dtype[0] is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).ndim != 2"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "array.shape[1] >= 1"
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
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).ndim != 2"
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse=['csr'], dtype=dtype[0], False, True, True).ndim != 2"
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
                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).ndim != 2"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "array.shape[1] >= 1"
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
                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).ndim != 2"
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
                                                "XXX TODO XXX": "getattr(X, 'dtype', None) is None"
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(X, 'dtype', None) not in [np.float64, np.float32]"
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
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "laleNot": "X/isSparse",
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], None, False, True, True).ndim != 2"
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
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
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
                                                                                "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse=['csr'], None, False, True, True).ndim != 2"
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
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) is not None"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) in [np.float64, np.float32]"
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
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "laleNot": "X/isSparse",
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], dtype=dtype[0], False, True, True).ndim != 2"
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
                                                                                                "XXX TODO XXX": "dtype[0] is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).ndim != 2"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "array.shape[1] >= 1"
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
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).ndim != 2"
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
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
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
                                                                                "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse=['csr'], dtype=dtype[0], False, True, True).ndim != 2"
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
                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).ndim != 2"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "array.shape[1] >= 1"
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
                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).ndim != 2"
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], dtype=dtype[0], False, True, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], dtype=dtype[0], False, True, True).fit)"
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
                                                                                "XXX TODO XXX": "dtype[0] is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).fit)"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).fit)"
                                                                            },
                                                                        ]
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse=['csr'], dtype=dtype[0], False, True, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse=['csr'], dtype=dtype[0], False, True, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).fit)"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(np.asarray(X, None, dtype=dtype[0]).fit)"
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
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
                                                "XXX TODO XXX": "getattr(X, 'dtype', None) is None"
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(X, 'dtype', None) not in [np.float64, np.float32]"
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
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "laleNot": "X/isSparse",
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], None, False, True, True), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], None, False, True, True).fit)"
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
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
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
                                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse=['csr'], None, False, True, True), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse=['csr'], None, False, True, True).fit)"
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
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) is not None"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) in [np.float64, np.float32]"
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
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "laleNot": "X/isSparse",
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], dtype=dtype[0], False, True, True), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], dtype=dtype[0], False, True, True).fit)"
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
                                                                                                "XXX TODO XXX": "dtype[0] is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'fit')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).fit)"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'fit')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).fit)"
                                                                                            },
                                                                                        ]
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
                                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
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
                                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse=['csr'], dtype=dtype[0], False, True, True), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse=['csr'], dtype=dtype[0], False, True, True).fit)"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'fit')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not callable(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).fit)"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'fit')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not callable(np.asarray(X, None, dtype=dtype[0]).fit)"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                ]
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
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
                                                                "XXX TODO XXX": "not all((False for [np.float64, np.float32] in list(X.dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "np.result_type(*list(X.dtypes)) is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.result_type(*list(X.dtypes)) not in [np.float64, np.float32]"
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
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "np.result_type(*list(X.dtypes)) is not None"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "np.result_type(*list(X.dtypes)) in [np.float64, np.float32]"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                                            },
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
                                                                                                    {
                                                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                                                    },
                                                                                                ]
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                                            },
                                                                                                        ]
                                                                                                    },
                                                                                                ]
                                                                                            },
                                                                                        ]
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
                                                                "XXX TODO XXX": "all((False for [np.float64, np.float32] in list(X.dtypes)))"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'dtype')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype, 'kind')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                            },
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
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'dtype')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]).dtype, 'kind')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                ]
                                                                            },
                                                                        ]
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                            },
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
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
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
                                                                "XXX TODO XXX": "not all((False for [np.float64, np.float32] in list(X.dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "np.result_type(*list(X.dtypes)) is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.result_type(*list(X.dtypes)) not in [np.float64, np.float32]"
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
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "np.result_type(*list(X.dtypes)) is not None"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "np.result_type(*list(X.dtypes)) in [np.float64, np.float32]"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                                            },
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
                                                                                                    {
                                                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                                                    },
                                                                                                ]
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                                            },
                                                                                                        ]
                                                                                                    },
                                                                                                ]
                                                                                            },
                                                                                        ]
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
                                                                "XXX TODO XXX": "all((False for [np.float64, np.float32] in list(X.dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "getattr(X, 'dtype', None) is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "getattr(X, 'dtype', None) not in [np.float64, np.float32]"
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
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) is not None"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) in [np.float64, np.float32]"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                                            },
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
                                                                                                    {
                                                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                                                    },
                                                                                                ]
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                                            },
                                                                                                        ]
                                                                                                    },
                                                                                                ]
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                ]
                                                                            },
                                                                        ]
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
                                                                "XXX TODO XXX": "getattr(X, 'dtype', None) is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "getattr(X, 'dtype', None) not in [np.float64, np.float32]"
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
                                                                "allOf": [
                                                                    {
                                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) is not None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) in [np.float64, np.float32]"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'dtype')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype, 'kind')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                            },
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
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'dtype')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]).dtype, 'kind')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                ]
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
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
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {
                                                "XXX TODO XXX": "getattr(X, 'dtype', None) is None"
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(X, 'dtype', None) not in [np.float64, np.float32]"
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
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) is not None"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) in [np.float64, np.float32]"
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
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).ndim < 3"
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
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).ndim < 3"
                                                            },
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
                                            {"XXX TODO XXX": "sp.issparse(X)"},
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
                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).ndim < 3"
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
                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).ndim < 3"
                                                            },
                                                        ]
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
                                                "XXX TODO XXX": "getattr(X, 'dtype', None) is None"
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(X, 'dtype', None) not in [np.float64, np.float32]"
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
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
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
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) is not None"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) in [np.float64, np.float32]"
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
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).ndim < 3"
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
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).ndim < 3"
                                                                            },
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
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).ndim < 3"
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
                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).ndim < 3"
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], dtype=dtype[0], False, True, True)) >= 1"
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
                                                                                "XXX TODO XXX": "dtype[0] is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False)) >= 1"
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
                                                                                "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0])) >= 1"
                                                                            },
                                                                        ]
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse=['csr'], dtype=dtype[0], False, True, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                "XXX TODO XXX": "_num_samples(np.asarray(X, None).astype(dtype[0], casting='unsafe', False)) >= 1"
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
                                                                                "XXX TODO XXX": "_num_samples(np.asarray(X, None, dtype=dtype[0])) >= 1"
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
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
                                                "XXX TODO XXX": "getattr(X, 'dtype', None) is None"
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(X, 'dtype', None) not in [np.float64, np.float32]"
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
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "laleNot": "X/isSparse",
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], None, False, True, True)) >= 1"
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
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
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
                                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse=['csr'], None, False, True, True)) >= 1"
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
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) is not None"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) in [np.float64, np.float32]"
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
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "laleNot": "X/isSparse",
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], dtype=dtype[0], False, True, True)) >= 1"
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
                                                                                                "XXX TODO XXX": "dtype[0] is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False)) >= 1"
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
                                                                                                "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0])) >= 1"
                                                                                            },
                                                                                        ]
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
                                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
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
                                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse=['csr'], dtype=dtype[0], False, True, True)) >= 1"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                                "XXX TODO XXX": "_num_samples(np.asarray(X, None).astype(dtype[0], casting='unsafe', False)) >= 1"
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
                                                                                                "XXX TODO XXX": "_num_samples(np.asarray(X, None, dtype=dtype[0])) >= 1"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                ]
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], dtype=dtype[0], False, True, True).ndim != 2"
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
                                                                                "XXX TODO XXX": "dtype[0] is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).ndim != 2"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "array.shape[1] >= 1"
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
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).ndim != 2"
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse=['csr'], dtype=dtype[0], False, True, True).ndim != 2"
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
                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).ndim != 2"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "array.shape[1] >= 1"
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
                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).ndim != 2"
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
                                                "XXX TODO XXX": "getattr(X, 'dtype', None) is None"
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(X, 'dtype', None) not in [np.float64, np.float32]"
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
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "laleNot": "X/isSparse",
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], None, False, True, True).ndim != 2"
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
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
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
                                                                                "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse=['csr'], None, False, True, True).ndim != 2"
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
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) is not None"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) in [np.float64, np.float32]"
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
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "laleNot": "X/isSparse",
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], dtype=dtype[0], False, True, True).ndim != 2"
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
                                                                                                "XXX TODO XXX": "dtype[0] is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).ndim != 2"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "array.shape[1] >= 1"
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
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).ndim != 2"
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
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
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
                                                                                "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse=['csr'], dtype=dtype[0], False, True, True).ndim != 2"
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
                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).ndim != 2"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "array.shape[1] >= 1"
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
                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).ndim != 2"
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], dtype=dtype[0], False, True, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], dtype=dtype[0], False, True, True).fit)"
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
                                                                                "XXX TODO XXX": "dtype[0] is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).fit)"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).fit)"
                                                                            },
                                                                        ]
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
                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse=['csr'], dtype=dtype[0], False, True, True), 'fit')"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse=['csr'], dtype=dtype[0], False, True, True).fit)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).fit)"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(np.asarray(X, None, dtype=dtype[0]).fit)"
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
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
                                                "XXX TODO XXX": "getattr(X, 'dtype', None) is None"
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(X, 'dtype', None) not in [np.float64, np.float32]"
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
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "laleNot": "X/isSparse",
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], None, False, True, True), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], None, False, True, True).fit)"
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
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
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
                                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse=['csr'], None, False, True, True), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse=['csr'], None, False, True, True).fit)"
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
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) is not None"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) in [np.float64, np.float32]"
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
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "laleNot": "X/isSparse",
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], dtype=dtype[0], False, True, True), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], dtype=dtype[0], False, True, True).fit)"
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
                                                                                                "XXX TODO XXX": "dtype[0] is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'fit')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).fit)"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'fit')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not callable(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).fit)"
                                                                                            },
                                                                                        ]
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
                                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
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
                                                                                "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse=['csr'], dtype=dtype[0], False, True, True), 'fit')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse=['csr'], dtype=dtype[0], False, True, True).fit)"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'fit')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not callable(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).fit)"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'fit')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not callable(np.asarray(X, None, dtype=dtype[0]).fit)"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                ]
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
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
                                                                "XXX TODO XXX": "not all((False for [np.float64, np.float32] in list(X.dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "np.result_type(*list(X.dtypes)) is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.result_type(*list(X.dtypes)) not in [np.float64, np.float32]"
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
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "np.result_type(*list(X.dtypes)) is not None"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "np.result_type(*list(X.dtypes)) in [np.float64, np.float32]"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                                            },
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
                                                                                                    {
                                                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                                                    },
                                                                                                ]
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                                            },
                                                                                                        ]
                                                                                                    },
                                                                                                ]
                                                                                            },
                                                                                        ]
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
                                                                "XXX TODO XXX": "all((False for [np.float64, np.float32] in list(X.dtypes)))"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'dtype')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype, 'kind')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                            },
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
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'dtype')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]).dtype, 'kind')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                ]
                                                                            },
                                                                        ]
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                            },
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
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'dtype')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]).dtype, 'kind')"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
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
                                                                "XXX TODO XXX": "not all((False for [np.float64, np.float32] in list(X.dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "np.result_type(*list(X.dtypes)) is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.result_type(*list(X.dtypes)) not in [np.float64, np.float32]"
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
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "np.result_type(*list(X.dtypes)) is not None"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "np.result_type(*list(X.dtypes)) in [np.float64, np.float32]"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                                            },
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
                                                                                                    {
                                                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                                                    },
                                                                                                ]
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                                            },
                                                                                                        ]
                                                                                                    },
                                                                                                ]
                                                                                            },
                                                                                        ]
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
                                                                "XXX TODO XXX": "all((False for [np.float64, np.float32] in list(X.dtypes)))"
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "getattr(X, 'dtype', None) is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "getattr(X, 'dtype', None) not in [np.float64, np.float32]"
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
                                                                                "allOf": [
                                                                                    {
                                                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) is not None"
                                                                                    },
                                                                                    {
                                                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) in [np.float64, np.float32]"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                                            },
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
                                                                                                    {
                                                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                                                    },
                                                                                                ]
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'dtype')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype is None"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]).dtype, 'kind')"
                                                                                                            },
                                                                                                            {
                                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                                            },
                                                                                                        ]
                                                                                                    },
                                                                                                ]
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                ]
                                                                            },
                                                                        ]
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
                                                                "XXX TODO XXX": "getattr(X, 'dtype', None) is None"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "getattr(X, 'dtype', None) not in [np.float64, np.float32]"
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
                                                                "allOf": [
                                                                    {
                                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) is not None"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) in [np.float64, np.float32]"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'dtype')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype, 'kind')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                            },
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
                                                                                    {
                                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                                    },
                                                                                ]
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'dtype')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
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
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'dtype')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "not hasattr(np.asarray(X, None, dtype=dtype[0]).dtype, 'kind')"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).dtype.kind != 'c'"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                ]
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
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
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).ndim < 3"
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
                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).ndim < 3"
                                                            },
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
                                            {"XXX TODO XXX": "sp.issparse(X)"},
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
                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).ndim < 3"
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
                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).ndim < 3"
                                                            },
                                                        ]
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
                                                "XXX TODO XXX": "getattr(X, 'dtype', None) is None"
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(X, 'dtype', None) not in [np.float64, np.float32]"
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
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
                                                            },
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
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) is not None"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) in [np.float64, np.float32]"
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
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).ndim < 3"
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
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).ndim < 3"
                                                                            },
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
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).ndim < 3"
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
                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).ndim < 3"
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], dtype=dtype[0], False, True, True)) >= 1"
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
                                                                                "XXX TODO XXX": "dtype[0] is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False)) >= 1"
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
                                                                                "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0])) >= 1"
                                                                            },
                                                                        ]
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
                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse=['csr'], dtype=dtype[0], False, True, True)) >= 1"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                "XXX TODO XXX": "_num_samples(np.asarray(X, None).astype(dtype[0], casting='unsafe', False)) >= 1"
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
                                                                                "XXX TODO XXX": "_num_samples(np.asarray(X, None, dtype=dtype[0])) >= 1"
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
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
                                                "XXX TODO XXX": "getattr(X, 'dtype', None) is None"
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(X, 'dtype', None) not in [np.float64, np.float32]"
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
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "laleNot": "X/isSparse",
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], None, False, True, True)) >= 1"
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
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
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
                                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse=['csr'], None, False, True, True)) >= 1"
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
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) is not None"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) in [np.float64, np.float32]"
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
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "laleNot": "X/isSparse",
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], dtype=dtype[0], False, True, True)) >= 1"
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
                                                                                                "XXX TODO XXX": "dtype[0] is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False)) >= 1"
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
                                                                                                "XXX TODO XXX": "_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0])) >= 1"
                                                                                            },
                                                                                        ]
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
                                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
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
                                                                                "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse=['csr'], dtype=dtype[0], False, True, True)) >= 1"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "XXX TODO XXX": "sp.issparse(X)"
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
                                                                                                "XXX TODO XXX": "_num_samples(np.asarray(X, None).astype(dtype[0], casting='unsafe', False)) >= 1"
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
                                                                                                "XXX TODO XXX": "_num_samples(np.asarray(X, None, dtype=dtype[0])) >= 1"
                                                                                            },
                                                                                        ]
                                                                                    },
                                                                                ]
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                        ]
                                                    },
                                                ]
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], dtype=dtype[0], False, True, True).ndim != 2"
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
                                                                                "XXX TODO XXX": "dtype[0] is None"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).ndim != 2"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "array.shape[1] >= 1"
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
                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).ndim != 2"
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
                                                                "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse=['csr'], dtype=dtype[0], False, True, True).ndim != 2"
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
                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).ndim != 2"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "array.shape[1] >= 1"
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
                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).ndim != 2"
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
                                                "XXX TODO XXX": "getattr(X, 'dtype', None) is None"
                                            },
                                            {
                                                "XXX TODO XXX": "getattr(X, 'dtype', None) not in [np.float64, np.float32]"
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
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "laleNot": "X/isSparse",
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], None, False, True, True).ndim != 2"
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
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
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
                                                                                "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse=['csr'], None, False, True, True).ndim != 2"
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
                                                "allOf": [
                                                    {
                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) is not None"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "getattr(X, 'dtype', None) in [np.float64, np.float32]"
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
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "laleNot": "X/isSparse",
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr'], dtype=dtype[0], False, True, True).ndim != 2"
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
                                                                                                "XXX TODO XXX": "dtype[0] is None"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.dtype(dtype[0]).kind not in 'iu'"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).ndim != 2"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "array.shape[1] >= 1"
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
                                                                                                "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).ndim != 2"
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
                                                                    {
                                                                        "XXX TODO XXX": "hasattr(X, 'sparse')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.ndim > 1"
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
                                                                                "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse=['csr'], dtype=dtype[0], False, True, True).ndim != 2"
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
                                                                                                "XXX TODO XXX": "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).ndim != 2"
                                                                                            },
                                                                                            {
                                                                                                "XXX TODO XXX": "array.shape[1] >= 1"
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
                                                                                                "XXX TODO XXX": "np.asarray(X, None, dtype=dtype[0]).ndim != 2"
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
        "description": "From /utils/validation.py:None:column_or_1d, Exception: raise ValueError('y should be a 1d array, got an array of shape {} instead.'     .format(shape)) ",
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
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {"XXX TODO XXX": "y.dtype.kind != 'O'"},
                                            {
                                                "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
                                            },
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {"XXX TODO XXX": "y.dtype.kind == 'O'"},
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
                            {"type": "object", "properties": {"y": {"enum": [None]}}},
                            {
                                "allOf": [
                                    {
                                        "anyOf": [
                                            {"XXX TODO XXX": "y.dtype.kind != 'O'"},
                                            {
                                                "XXX TODO XXX": "len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1"
                                            },
                                        ]
                                    },
                                    {
                                        "anyOf": [
                                            {"XXX TODO XXX": "y.dtype.kind == 'O'"},
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
            {"type": "object", "properties": {"sample_weight": {"type": "number"}}},
            {"type": "object", "laleNot": "X/isSparse"},
        ],
    },
    {
        "description": "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Pandas DataFrame with mixed sparse extension arrays generated a sparse matrix with object dtype which can not be converted to a scipy sparse matrix.Sparse extension arrays should all have the same numeric type.'     ) ",
        "anyOf": [
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
        "description": "From /utils/validation.py:None:_check_sample_weight, Exception: raise ValueError('Sample weights must be 1D array or scalar') ",
        "anyOf": [
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
            {"type": "object", "properties": {"sample_weight": {"type": "number"}}},
            {
                "XXX TODO XXX": "check_array(sample_weight, False, False, dtype=[np.float64, np.float32], order='C', False).shape == [_num_samples(X)]"
            },
        ],
    },
    {
        "description": "From /linear_model/_huber.py:HuberRegressor:fit, Exception: raise ValueError('epsilon should be greater than or equal to 1.0, got %f' %     self.epsilon) ",
        "type": "object",
        "properties": {"epsilon": {"type": "number", "minimum": 1.0}},
    },
    {
        "description": "From /linear_model/_huber.py:HuberRegressor:fit, Exception: raise ValueError(     'HuberRegressor convergence failed: l-BFGS-b solver terminated with %s' %     opt_res.message) ",
        "allOf": [
            {
                "anyOf": [
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'coef_')"},
                    {
                        "XXX TODO XXX": "optimize.minimize(_huber_loss_and_gradient, np.concatenate([self.coef_, [self.intercept_, self.scale_]]), method='L-BFGS-B', True, args=[X, y, self.epsilon, self.alpha, _check_sample_weight(sample_weight, X)], options={'maxiter': self.max_iter, 'gtol': self.tol, 'iprint': -1}, bounds=np.tile([-np.inf, np.inf], [parameters.shape[0], 1])).status != 2"
                    },
                ]
            },
            {
                "anyOf": [
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'coef_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "fit_intercept": {"enum": [False]}
                                        },
                                    },
                                    {
                                        "XXX TODO XXX": "optimize.minimize(_huber_loss_and_gradient, np.zeros(X.shape[1] + 2), method='L-BFGS-B', True, args=[X, y, self.epsilon, self.alpha, _check_sample_weight(sample_weight, X)], options={'maxiter': self.max_iter, 'gtol': self.tol, 'iprint': -1}, bounds=np.tile([-np.inf, np.inf], [parameters.shape[0], 1])).status != 2"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "fit_intercept": {"enum": [True]}
                                        },
                                    },
                                    {
                                        "XXX TODO XXX": "optimize.minimize(_huber_loss_and_gradient, np.zeros(X.shape[1] + 1), method='L-BFGS-B', True, args=[X, y, self.epsilon, self.alpha, _check_sample_weight(sample_weight, X)], options={'maxiter': self.max_iter, 'gtol': self.tol, 'iprint': -1}, bounds=np.tile([-np.inf, np.inf], [parameters.shape[0], 1])).status != 2"
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
