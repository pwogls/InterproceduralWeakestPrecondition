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
                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc', 'lil'], dtype=dtype[0], copy=self.copy, True, True), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc', 'lil'], dtype=dtype[0], copy=self.copy, True, True).fit)"
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
                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse=['csr', 'csc', 'lil'], dtype=dtype[0], copy=self.copy, True, True), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse=['csr', 'csc', 'lil'], dtype=dtype[0], copy=self.copy, True, True).fit)"
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
                                        "XXX TODO XXX": "getattr(X, 'dtype', None) not in [np.float64, np.float32]"
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
                                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc', 'lil'], None, copy=self.copy, True, True), 'fit')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc', 'lil'], None, copy=self.copy, True, True).fit)"
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
                                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse=['csr', 'csc', 'lil'], None, copy=self.copy, True, True), 'fit')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse=['csr', 'csc', 'lil'], None, copy=self.copy, True, True).fit)"
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
                                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc', 'lil'], dtype=dtype[0], copy=self.copy, True, True), 'fit')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc', 'lil'], dtype=dtype[0], copy=self.copy, True, True).fit)"
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
                                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse=['csr', 'csc', 'lil'], dtype=dtype[0], copy=self.copy, True, True), 'fit')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse=['csr', 'csc', 'lil'], dtype=dtype[0], copy=self.copy, True, True).fit)"
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
                                        "XXX TODO XXX": "getattr(X, 'dtype', None) not in [np.float64, np.float32]"
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
                                                "XXX TODO XXX": "getattr(X, 'dtype', None) in [np.float64, np.float32]"
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
                                        "XXX TODO XXX": "getattr(X, 'dtype', None) not in [np.float64, np.float32]"
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
                                                            {
                                                                "XXX TODO XXX": "X.ndim > 1"
                                                            },
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
                                                            {
                                                                "XXX TODO XXX": "X.ndim > 1"
                                                            },
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
                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc', 'lil'], dtype=dtype[0], copy=self.copy, True, True)) >= 1"
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
                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse=['csr', 'csc', 'lil'], dtype=dtype[0], copy=self.copy, True, True)) >= 1"
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
                                        "XXX TODO XXX": "getattr(X, 'dtype', None) not in [np.float64, np.float32]"
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
                                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc', 'lil'], None, copy=self.copy, True, True)) >= 1"
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
                                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse=['csr', 'csc', 'lil'], None, copy=self.copy, True, True)) >= 1"
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
                                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc', 'lil'], dtype=dtype[0], copy=self.copy, True, True)) >= 1"
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
                                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse=['csr', 'csc', 'lil'], dtype=dtype[0], copy=self.copy, True, True)) >= 1"
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
                                                        "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc', 'lil'], dtype=dtype[0], copy=self.copy, True, True).ndim != 2"
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
                                                        "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse=['csr', 'csc', 'lil'], dtype=dtype[0], copy=self.copy, True, True).ndim != 2"
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
                                        "XXX TODO XXX": "getattr(X, 'dtype', None) not in [np.float64, np.float32]"
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
                                                                        "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc', 'lil'], None, copy=self.copy, True, True).ndim != 2"
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
                                                                        "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse=['csr', 'csc', 'lil'], None, copy=self.copy, True, True).ndim != 2"
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
                                                                        "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc', 'lil'], dtype=dtype[0], copy=self.copy, True, True).ndim != 2"
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
                                                                        "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse=['csr', 'csc', 'lil'], dtype=dtype[0], copy=self.copy, True, True).ndim != 2"
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
        ],
    },
    {
        "description": "From /decomposition/_incremental_pca.py:IncrementalPCA:partial_fit, Exception: raise ValueError(     'n_components=%r invalid for n_features=%d, need more rows than columns for IncrementalPCA processing'      % (self.n_components, n_features)) ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "type": "object",
                        "properties": {"batch_size": {"not": {"enum": [None]}}},
                    },
                    {
                        "XXX TODO XXX": "batch not in gen_batches(X.shape[0], 5 * X.shape[1], min_batch_size=self.n_components)"
                    },
                    {
                        "type": "object",
                        "properties": {"n_components": {"enum": [None]}},
                    },
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {
                                    "n_components": {"type": "number", "minimum": 1}
                                },
                            },
                            {
                                "type": "object",
                                "properties": {
                                    "n_components": {"laleMaximum": "X/items/maxItems"}
                                },
                            },
                        ]
                    },
                ]
            },
            {
                "anyOf": [
                    {"type": "object", "properties": {"batch_size": {"enum": [None]}}},
                    {
                        "XXX TODO XXX": "batch not in gen_batches(X.shape[0], self.batch_size, min_batch_size=self.n_components)"
                    },
                    {
                        "type": "object",
                        "properties": {"n_components": {"enum": [None]}},
                    },
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {
                                    "n_components": {"type": "number", "minimum": 1}
                                },
                            },
                            {
                                "type": "object",
                                "properties": {
                                    "n_components": {"laleMaximum": "X/items/maxItems"}
                                },
                            },
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": "From /decomposition/_incremental_pca.py:IncrementalPCA:partial_fit, Exception: raise ValueError(     'n_components=%r must be less or equal to the batch number of samples %d.'      % (self.n_components, n_samples)) ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "type": "object",
                        "properties": {"batch_size": {"not": {"enum": [None]}}},
                    },
                    {
                        "XXX TODO XXX": "batch not in gen_batches(X.shape[0], 5 * X.shape[1], min_batch_size=self.n_components)"
                    },
                    {
                        "type": "object",
                        "properties": {"n_components": {"enum": [None]}},
                    },
                    {
                        "type": "object",
                        "properties": {
                            "n_components": {
                                "type": "number",
                                "maximum": 1,
                                "exclusiveMaximum": True,
                            }
                        },
                    },
                    {
                        "type": "object",
                        "properties": {
                            "n_components": {"laleMinimum": "X/items/maxItems"}
                        },
                    },
                    {
                        "type": "object",
                        "properties": {"n_components": {"laleMaximum": "X/maxItems"}},
                    },
                ]
            },
            {
                "anyOf": [
                    {"type": "object", "properties": {"batch_size": {"enum": [None]}}},
                    {
                        "XXX TODO XXX": "batch not in gen_batches(X.shape[0], self.batch_size, min_batch_size=self.n_components)"
                    },
                    {
                        "type": "object",
                        "properties": {"n_components": {"enum": [None]}},
                    },
                    {
                        "type": "object",
                        "properties": {
                            "n_components": {
                                "type": "number",
                                "maximum": 1,
                                "exclusiveMaximum": True,
                            }
                        },
                    },
                    {
                        "type": "object",
                        "properties": {
                            "n_components": {"laleMinimum": "X/items/maxItems"}
                        },
                    },
                    {
                        "type": "object",
                        "properties": {"n_components": {"laleMaximum": "X/maxItems"}},
                    },
                ]
            },
        ],
    },
]
