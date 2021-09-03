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
                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), False, dtype=dtype[0], copy=self.copy, True, True), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), False, dtype=dtype[0], copy=self.copy, True, True).fit)"
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
                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, False, dtype=dtype[0], copy=self.copy, True, True), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(X, False, dtype=dtype[0], copy=self.copy, True, True).fit)"
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
                                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), False, None, copy=self.copy, True, True), 'fit')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), False, None, copy=self.copy, True, True).fit)"
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
                                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, False, None, copy=self.copy, True, True), 'fit')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(X, False, None, copy=self.copy, True, True).fit)"
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
                                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), False, dtype=dtype[0], copy=self.copy, True, True), 'fit')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(X.sparse.to_coo(), False, dtype=dtype[0], copy=self.copy, True, True).fit)"
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
                                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, False, dtype=dtype[0], copy=self.copy, True, True), 'fit')"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(X, False, dtype=dtype[0], copy=self.copy, True, True).fit)"
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
                    {"type": "object", "laleNot": "X/isSparse"},
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
                ]
            },
            {
                "anyOf": [
                    {"XXX TODO XXX": "issparse(X)"},
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
                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), False, dtype=dtype[0], copy=self.copy, True, True)) >= 1"
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
                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, False, dtype=dtype[0], copy=self.copy, True, True)) >= 1"
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
                                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), False, None, copy=self.copy, True, True)) >= 1"
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
                                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, False, None, copy=self.copy, True, True)) >= 1"
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
                                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), False, dtype=dtype[0], copy=self.copy, True, True)) >= 1"
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
                                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, False, dtype=dtype[0], copy=self.copy, True, True)) >= 1"
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
                                                        "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), False, dtype=dtype[0], copy=self.copy, True, True).ndim != 2"
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
                                                        "XXX TODO XXX": "_ensure_sparse_format(X, False, dtype=dtype[0], copy=self.copy, True, True).ndim != 2"
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
                                                                        "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), False, None, copy=self.copy, True, True).ndim != 2"
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
                                                                        "XXX TODO XXX": "_ensure_sparse_format(X, False, None, copy=self.copy, True, True).ndim != 2"
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
                                                                        "XXX TODO XXX": "_ensure_sparse_format(X.sparse.to_coo(), False, dtype=dtype[0], copy=self.copy, True, True).ndim != 2"
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
                                                                        "XXX TODO XXX": "_ensure_sparse_format(X, False, dtype=dtype[0], copy=self.copy, True, True).ndim != 2"
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
        "description": "From /decomposition/_pca.py:None:_assess_dimension, Exception: raise ValueError('the tested rank should be in [1, n_features - 1]') ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "type": "object",
                        "properties": {"n_components": {"not": {"enum": [None]}}},
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"enum": ["arpack"]}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "not": {
                                                                    "enum": ["auto"]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "max(X.shape) > 500"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) != 'mle'"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) != 'mle'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "rank not in range(1, spectrum.shape[0])"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "properties": {
                                                                                    "rank": {
                                                                                        "type": "number",
                                                                                        "minimum": 1,
                                                                                    }
                                                                                },
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "rank < spectrum.shape[0]"
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "max(X.shape) <= 500"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) == 'mle'"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) >= 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) < 0.8 * min(X.shape)"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) != 'mle'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "rank not in range(1, spectrum.shape[0])"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "properties": {
                                                                                    "rank": {
                                                                                        "type": "number",
                                                                                        "minimum": 1,
                                                                                    }
                                                                                },
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "rank < spectrum.shape[0]"
                                                                            },
                                                                        ]
                                                                    },
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
                                                            "svd_solver": {
                                                                "enum": ["auto"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "not": {
                                                                    "enum": ["full"]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) != 'mle'"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "rank not in range(1, spectrum.shape[0])"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "rank": {
                                                                        "type": "number",
                                                                        "minimum": 1,
                                                                    }
                                                                },
                                                            },
                                                            {
                                                                "XXX TODO XXX": "rank < spectrum.shape[0]"
                                                            },
                                                        ]
                                                    },
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
                                            "svd_solver": {"not": {"enum": ["arpack"]}}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "not": {
                                                                    "enum": ["auto"]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "max(X.shape) > 500"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) - 1 != 'mle'"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) - 1 != 'mle'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "rank not in range(1, spectrum.shape[0])"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "properties": {
                                                                                    "rank": {
                                                                                        "type": "number",
                                                                                        "minimum": 1,
                                                                                    }
                                                                                },
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "rank < spectrum.shape[0]"
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "max(X.shape) <= 500"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) - 1 == 'mle'"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) - 1 >= 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) - 1 < 0.8 * min(X.shape)"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) - 1 != 'mle'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "rank not in range(1, spectrum.shape[0])"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "type": "object",
                                                                                "properties": {
                                                                                    "rank": {
                                                                                        "type": "number",
                                                                                        "minimum": 1,
                                                                                    }
                                                                                },
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "rank < spectrum.shape[0]"
                                                                            },
                                                                        ]
                                                                    },
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
                                                            "svd_solver": {
                                                                "enum": ["auto"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "not": {
                                                                    "enum": ["full"]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) - 1 != 'mle'"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "rank not in range(1, spectrum.shape[0])"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "rank": {
                                                                        "type": "number",
                                                                        "minimum": 1,
                                                                    }
                                                                },
                                                            },
                                                            {
                                                                "XXX TODO XXX": "rank < spectrum.shape[0]"
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                        ]
                                    },
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
                        "properties": {"n_components": {"enum": [None]}},
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"not": {"enum": ["auto"]}}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "max(X.shape) > 500"
                                                            },
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "n_components": {
                                                                        "not": {
                                                                            "enum": [
                                                                                "mle"
                                                                            ]
                                                                        }
                                                                    }
                                                                },
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "n_components": {
                                                                "not": {"enum": ["mle"]}
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "rank not in range(1, spectrum.shape[0])"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "rank": {
                                                                        "type": "number",
                                                                        "minimum": 1,
                                                                    }
                                                                },
                                                            },
                                                            {
                                                                "XXX TODO XXX": "rank < spectrum.shape[0]"
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "max(X.shape) <= 500"
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "n_components": {
                                                                "enum": ["mle"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "n_components": {
                                                                        "type": "number",
                                                                        "minimum": 1,
                                                                    }
                                                                },
                                                            },
                                                            {
                                                                "XXX TODO XXX": "self.n_components < 0.8 * min(X.shape)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "n_components": {
                                                                "not": {"enum": ["mle"]}
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "rank not in range(1, spectrum.shape[0])"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "rank": {
                                                                        "type": "number",
                                                                        "minimum": 1,
                                                                    }
                                                                },
                                                            },
                                                            {
                                                                "XXX TODO XXX": "rank < spectrum.shape[0]"
                                                            },
                                                        ]
                                                    },
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
                                            "svd_solver": {"enum": ["auto"]}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"not": {"enum": ["full"]}}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_components": {"not": {"enum": ["mle"]}}
                                        },
                                    },
                                    {
                                        "XXX TODO XXX": "rank not in range(1, spectrum.shape[0])"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "rank": {
                                                        "type": "number",
                                                        "minimum": 1,
                                                    }
                                                },
                                            },
                                            {
                                                "XXX TODO XXX": "rank < spectrum.shape[0]"
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
        "description": "From /decomposition/_pca.py:PCA:_fit_full, Exception: raise ValueError(     \"n_components='mle' is only supported if n_samples >= n_features\") ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "type": "object",
                        "properties": {"n_components": {"not": {"enum": [None]}}},
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"enum": ["arpack"]}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "not": {
                                                                    "enum": ["auto"]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "max(X.shape) > 500"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) != 'mle'"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) != 'mle'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.shape[0] >= X.shape[1]"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "max(X.shape) <= 500"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) == 'mle'"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) >= 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) < 0.8 * min(X.shape)"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) != 'mle'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.shape[0] >= X.shape[1]"
                                                                    },
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
                                                            "svd_solver": {
                                                                "enum": ["auto"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "not": {
                                                                    "enum": ["full"]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) != 'mle'"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "X.shape[0] >= X.shape[1]"
                                                    },
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
                                            "svd_solver": {"not": {"enum": ["arpack"]}}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "not": {
                                                                    "enum": ["auto"]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "max(X.shape) > 500"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) - 1 != 'mle'"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) - 1 != 'mle'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.shape[0] >= X.shape[1]"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "max(X.shape) <= 500"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) - 1 == 'mle'"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) - 1 >= 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) - 1 < 0.8 * min(X.shape)"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) - 1 != 'mle'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "X.shape[0] >= X.shape[1]"
                                                                    },
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
                                                            "svd_solver": {
                                                                "enum": ["auto"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "not": {
                                                                    "enum": ["full"]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) - 1 != 'mle'"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "X.shape[0] >= X.shape[1]"
                                                    },
                                                ]
                                            },
                                        ]
                                    },
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
                        "properties": {"n_components": {"enum": [None]}},
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"not": {"enum": ["auto"]}}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "max(X.shape) > 500"
                                                            },
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "n_components": {
                                                                        "not": {
                                                                            "enum": [
                                                                                "mle"
                                                                            ]
                                                                        }
                                                                    }
                                                                },
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "n_components": {
                                                                "not": {"enum": ["mle"]}
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "X.shape[0] >= X.shape[1]"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "max(X.shape) <= 500"
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "n_components": {
                                                                "enum": ["mle"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "n_components": {
                                                                        "type": "number",
                                                                        "minimum": 1,
                                                                    }
                                                                },
                                                            },
                                                            {
                                                                "XXX TODO XXX": "self.n_components < 0.8 * min(X.shape)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "n_components": {
                                                                "not": {"enum": ["mle"]}
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "X.shape[0] >= X.shape[1]"
                                                    },
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
                                            "svd_solver": {"enum": ["auto"]}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"not": {"enum": ["full"]}}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_components": {"not": {"enum": ["mle"]}}
                                        },
                                    },
                                    {"XXX TODO XXX": "X.shape[0] >= X.shape[1]"},
                                ]
                            },
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": "From /decomposition/_pca.py:PCA:_fit_full, Exception: raise ValueError(     \"n_components=%r must be between 0 and min(n_samples, n_features)=%r with svd_solver='full'\"      % (n_components, min(n_samples, n_features))) ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "type": "object",
                        "properties": {"n_components": {"not": {"enum": [None]}}},
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"enum": ["arpack"]}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "not": {
                                                                    "enum": ["auto"]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "max(X.shape) > 500"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) != 'mle'"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) == 'mle'"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "0 <= X.shape"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) <= X.shape[0]"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) <= X.shape[1]"
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "max(X.shape) <= 500"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) == 'mle'"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) >= 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) < 0.8 * min(X.shape)"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) == 'mle'"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "0 <= X.shape"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) <= X.shape[0]"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) <= X.shape[1]"
                                                                            },
                                                                        ]
                                                                    },
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
                                                            "svd_solver": {
                                                                "enum": ["auto"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "not": {
                                                                    "enum": ["full"]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) == 'mle'"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "0 <= X.shape"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "min(X.shape) <= X.shape[0]"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "min(X.shape) <= X.shape[1]"
                                                            },
                                                        ]
                                                    },
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
                                            "svd_solver": {"not": {"enum": ["arpack"]}}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "not": {
                                                                    "enum": ["auto"]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "max(X.shape) > 500"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) - 1 != 'mle'"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) - 1 == 'mle'"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "0 <= min(X.shape) - 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) - 1 <= X.shape[0]"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) - 1 <= X.shape[1]"
                                                                            },
                                                                        ]
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "max(X.shape) <= 500"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) - 1 == 'mle'"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) - 1 >= 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) - 1 < 0.8 * min(X.shape)"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) - 1 == 'mle'"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "0 <= min(X.shape) - 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) - 1 <= X.shape[0]"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) - 1 <= X.shape[1]"
                                                                            },
                                                                        ]
                                                                    },
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
                                                            "svd_solver": {
                                                                "enum": ["auto"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "not": {
                                                                    "enum": ["full"]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) - 1 == 'mle'"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "0 <= min(X.shape) - 1"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "min(X.shape) - 1 <= X.shape[0]"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "min(X.shape) - 1 <= X.shape[1]"
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                        ]
                                    },
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
                        "properties": {"n_components": {"enum": [None]}},
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"not": {"enum": ["auto"]}}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "max(X.shape) > 500"
                                                            },
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "n_components": {
                                                                        "not": {
                                                                            "enum": [
                                                                                "mle"
                                                                            ]
                                                                        }
                                                                    }
                                                                },
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "n_components": {
                                                                "enum": ["mle"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "n_components": {
                                                                        "type": "number",
                                                                        "minimum": 0,
                                                                    }
                                                                },
                                                            },
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "n_components": {
                                                                        "laleMaximum": "X/maxItems"
                                                                    }
                                                                },
                                                            },
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "n_components": {
                                                                        "laleMaximum": "X/items/maxItems"
                                                                    }
                                                                },
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "max(X.shape) <= 500"
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "n_components": {
                                                                "enum": ["mle"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "n_components": {
                                                                        "type": "number",
                                                                        "minimum": 1,
                                                                    }
                                                                },
                                                            },
                                                            {
                                                                "XXX TODO XXX": "self.n_components < 0.8 * min(X.shape)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "n_components": {
                                                                "enum": ["mle"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "n_components": {
                                                                        "type": "number",
                                                                        "minimum": 0,
                                                                    }
                                                                },
                                                            },
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "n_components": {
                                                                        "laleMaximum": "X/maxItems"
                                                                    }
                                                                },
                                                            },
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "n_components": {
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
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"enum": ["auto"]}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"not": {"enum": ["full"]}}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_components": {"enum": ["mle"]}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "n_components": {
                                                        "type": "number",
                                                        "minimum": 0,
                                                    }
                                                },
                                            },
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "n_components": {
                                                        "laleMaximum": "X/maxItems"
                                                    }
                                                },
                                            },
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "n_components": {
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
        "description": "From /decomposition/_pca.py:PCA:_fit_full, Exception: raise ValueError(     'n_components=%r must be of type int when greater than or equal to 1, was of type=%r'      % (n_components, type(n_components))) ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "type": "object",
                        "properties": {"n_components": {"not": {"enum": [None]}}},
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"enum": ["arpack"]}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "not": {
                                                                    "enum": ["auto"]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "max(X.shape) > 500"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) != 'mle'"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) == 'mle'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "0 > X.shape"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) > X.shape[0]"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) > X.shape[1]"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) < 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "isinstance(min(X.shape), numbers.Integral)"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "max(X.shape) <= 500"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) == 'mle'"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) >= 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) < 0.8 * min(X.shape)"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) == 'mle'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "0 > X.shape"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) > X.shape[0]"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) > X.shape[1]"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) < 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "isinstance(min(X.shape), numbers.Integral)"
                                                                    },
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
                                                            "svd_solver": {
                                                                "enum": ["auto"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "not": {
                                                                    "enum": ["full"]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) == 'mle'"
                                                    },
                                                    {"XXX TODO XXX": "0 > X.shape"},
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) > X.shape[0]"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) > X.shape[1]"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) < 1"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "isinstance(min(X.shape), numbers.Integral)"
                                                    },
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
                                            "svd_solver": {"not": {"enum": ["arpack"]}}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "not": {
                                                                    "enum": ["auto"]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "max(X.shape) > 500"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) - 1 != 'mle'"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) - 1 == 'mle'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "0 > min(X.shape) - 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) - 1 > X.shape[0]"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) - 1 > X.shape[1]"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) - 1 < 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "isinstance(min(X.shape) - 1, numbers.Integral)"
                                                                    },
                                                                ]
                                                            },
                                                            {
                                                                "anyOf": [
                                                                    {
                                                                        "XXX TODO XXX": "max(X.shape) <= 500"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) - 1 == 'mle'"
                                                                    },
                                                                    {
                                                                        "allOf": [
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) - 1 >= 1"
                                                                            },
                                                                            {
                                                                                "XXX TODO XXX": "min(X.shape) - 1 < 0.8 * min(X.shape)"
                                                                            },
                                                                        ]
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) - 1 == 'mle'"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "0 > min(X.shape) - 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) - 1 > X.shape[0]"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) - 1 > X.shape[1]"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "min(X.shape) - 1 < 1"
                                                                    },
                                                                    {
                                                                        "XXX TODO XXX": "isinstance(min(X.shape) - 1, numbers.Integral)"
                                                                    },
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
                                                            "svd_solver": {
                                                                "enum": ["auto"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "not": {
                                                                    "enum": ["full"]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) - 1 == 'mle'"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "0 > min(X.shape) - 1"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) - 1 > X.shape[0]"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) - 1 > X.shape[1]"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) - 1 < 1"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "isinstance(min(X.shape) - 1, numbers.Integral)"
                                                    },
                                                ]
                                            },
                                        ]
                                    },
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
                        "properties": {"n_components": {"enum": [None]}},
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"not": {"enum": ["auto"]}}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "max(X.shape) > 500"
                                                            },
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "n_components": {
                                                                        "not": {
                                                                            "enum": [
                                                                                "mle"
                                                                            ]
                                                                        }
                                                                    }
                                                                },
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "n_components": {
                                                                "enum": ["mle"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "n_components": {
                                                                "type": "number",
                                                                "maximum": 0,
                                                                "exclusiveMaximum": True,
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "n_components": {
                                                                "laleMinimum": "X/maxItems"
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "n_components": {
                                                                "laleMinimum": "X/items/maxItems"
                                                            }
                                                        },
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
                                                            "n_components": {
                                                                "type": "integer"
                                                            }
                                                        },
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "max(X.shape) <= 500"
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "n_components": {
                                                                "enum": ["mle"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "n_components": {
                                                                        "type": "number",
                                                                        "minimum": 1,
                                                                    }
                                                                },
                                                            },
                                                            {
                                                                "XXX TODO XXX": "self.n_components < 0.8 * min(X.shape)"
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "n_components": {
                                                                "enum": ["mle"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "n_components": {
                                                                "type": "number",
                                                                "maximum": 0,
                                                                "exclusiveMaximum": True,
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "n_components": {
                                                                "laleMinimum": "X/maxItems"
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "n_components": {
                                                                "laleMinimum": "X/items/maxItems"
                                                            }
                                                        },
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
                                                            "n_components": {
                                                                "type": "integer"
                                                            }
                                                        },
                                                    },
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
                                            "svd_solver": {"enum": ["auto"]}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"not": {"enum": ["full"]}}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_components": {"enum": ["mle"]}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_components": {
                                                "type": "number",
                                                "maximum": 0,
                                                "exclusiveMaximum": True,
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_components": {
                                                "laleMinimum": "X/maxItems"
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_components": {
                                                "laleMinimum": "X/items/maxItems"
                                            }
                                        },
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
                                            "n_components": {"type": "integer"}
                                        },
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
        "description": "From /utils/validation.py:None:check_random_state, Exception: raise ValueError(     '%r cannot be used to seed a numpy.random.RandomState instance' % seed) ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "type": "object",
                        "properties": {"n_components": {"not": {"enum": [None]}}},
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"enum": ["arpack"]}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"not": {"enum": ["auto"]}}
                                        },
                                    },
                                    {"XXX TODO XXX": "max(X.shape) <= 500"},
                                    {"XXX TODO XXX": "min(X.shape) == 'mle'"},
                                    {"XXX TODO XXX": "min(X.shape) < 1"},
                                    {
                                        "XXX TODO XXX": "min(X.shape) >= 0.8 * min(X.shape)"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "random_state": {"enum": [None]}
                                        },
                                    },
                                    {"XXX TODO XXX": "self.random_state is np.random"},
                                    {
                                        "XXX TODO XXX": "isinstance(self.random_state, np.random.RandomState)"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"not": {"enum": ["arpack"]}}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"not": {"enum": ["auto"]}}
                                        },
                                    },
                                    {"XXX TODO XXX": "max(X.shape) <= 500"},
                                    {"XXX TODO XXX": "min(X.shape) - 1 == 'mle'"},
                                    {"XXX TODO XXX": "min(X.shape) - 1 < 1"},
                                    {
                                        "XXX TODO XXX": "min(X.shape) - 1 >= 0.8 * min(X.shape)"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "random_state": {"enum": [None]}
                                        },
                                    },
                                    {"XXX TODO XXX": "self.random_state is np.random"},
                                    {
                                        "XXX TODO XXX": "isinstance(self.random_state, np.random.RandomState)"
                                    },
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
                        "properties": {"n_components": {"enum": [None]}},
                    },
                    {
                        "type": "object",
                        "properties": {"svd_solver": {"not": {"enum": ["auto"]}}},
                    },
                    {"XXX TODO XXX": "max(X.shape) <= 500"},
                    {
                        "type": "object",
                        "properties": {"n_components": {"enum": ["mle"]}},
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
                    {"XXX TODO XXX": "self.n_components >= 0.8 * min(X.shape)"},
                    {
                        "type": "object",
                        "properties": {"random_state": {"enum": [None]}},
                    },
                    {"XXX TODO XXX": "self.random_state is np.random"},
                    {
                        "XXX TODO XXX": "isinstance(self.random_state, np.random.RandomState)"
                    },
                ]
            },
            {
                "anyOf": [
                    {
                        "type": "object",
                        "properties": {"svd_solver": {"enum": ["auto"]}},
                    },
                    {
                        "type": "object",
                        "properties": {"svd_solver": {"enum": ["full"]}},
                    },
                    {
                        "type": "object",
                        "properties": {
                            "svd_solver": {"not": {"enum": ["arpack", "randomized"]}}
                        },
                    },
                    {
                        "type": "object",
                        "properties": {"random_state": {"enum": [None]}},
                    },
                    {"XXX TODO XXX": "self.random_state is np.random"},
                    {
                        "XXX TODO XXX": "isinstance(self.random_state, np.random.RandomState)"
                    },
                ]
            },
        ],
    },
    {
        "description": "From /utils/validation.py:None:check_random_state, Exception: raise ValueError(     '%r cannot be used to seed a numpy.random.RandomState instance' % seed) ",
        "anyOf": [
            {"type": "object", "properties": {"svd_solver": {"enum": ["auto"]}}},
            {"type": "object", "properties": {"svd_solver": {"enum": ["full"]}}},
            {
                "type": "object",
                "properties": {
                    "svd_solver": {"not": {"enum": ["arpack", "randomized"]}}
                },
            },
            {
                "type": "object",
                "properties": {"svd_solver": {"not": {"enum": ["arpack"]}}},
            },
            {"XXX TODO XXX": "check_random_state(self.random_state) is None"},
            {"XXX TODO XXX": "check_random_state(self.random_state) is np.random"},
            {
                "XXX TODO XXX": "isinstance(check_random_state(self.random_state), np.random.RandomState)"
            },
        ],
    },
    {
        "description": "From /utils/validation.py:None:check_random_state, Exception: raise ValueError(     '%r cannot be used to seed a numpy.random.RandomState instance' % seed) ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "type": "object",
                        "properties": {"n_components": {"not": {"enum": [None]}}},
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"enum": ["arpack"]}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"not": {"enum": ["auto"]}}
                                        },
                                    },
                                    {"XXX TODO XXX": "max(X.shape) <= 500"},
                                    {"XXX TODO XXX": "min(X.shape) == 'mle'"},
                                    {"XXX TODO XXX": "min(X.shape) < 1"},
                                    {
                                        "XXX TODO XXX": "min(X.shape) >= 0.8 * min(X.shape)"
                                    },
                                    {
                                        "XXX TODO XXX": "check_random_state(self.random_state) is None"
                                    },
                                    {
                                        "XXX TODO XXX": "check_random_state(self.random_state) is np.random"
                                    },
                                    {
                                        "XXX TODO XXX": "isinstance(check_random_state(self.random_state), np.random.RandomState)"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"not": {"enum": ["arpack"]}}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"not": {"enum": ["auto"]}}
                                        },
                                    },
                                    {"XXX TODO XXX": "max(X.shape) <= 500"},
                                    {"XXX TODO XXX": "min(X.shape) - 1 == 'mle'"},
                                    {"XXX TODO XXX": "min(X.shape) - 1 < 1"},
                                    {
                                        "XXX TODO XXX": "min(X.shape) - 1 >= 0.8 * min(X.shape)"
                                    },
                                    {
                                        "XXX TODO XXX": "check_random_state(self.random_state) is None"
                                    },
                                    {
                                        "XXX TODO XXX": "check_random_state(self.random_state) is np.random"
                                    },
                                    {
                                        "XXX TODO XXX": "isinstance(check_random_state(self.random_state), np.random.RandomState)"
                                    },
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
                        "properties": {"n_components": {"enum": [None]}},
                    },
                    {
                        "type": "object",
                        "properties": {"svd_solver": {"not": {"enum": ["auto"]}}},
                    },
                    {"XXX TODO XXX": "max(X.shape) <= 500"},
                    {
                        "type": "object",
                        "properties": {"n_components": {"enum": ["mle"]}},
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
                    {"XXX TODO XXX": "self.n_components >= 0.8 * min(X.shape)"},
                    {"XXX TODO XXX": "check_random_state(self.random_state) is None"},
                    {
                        "XXX TODO XXX": "check_random_state(self.random_state) is np.random"
                    },
                    {
                        "XXX TODO XXX": "isinstance(check_random_state(self.random_state), np.random.RandomState)"
                    },
                ]
            },
            {
                "anyOf": [
                    {
                        "type": "object",
                        "properties": {"svd_solver": {"enum": ["auto"]}},
                    },
                    {
                        "type": "object",
                        "properties": {"svd_solver": {"enum": ["full"]}},
                    },
                    {
                        "type": "object",
                        "properties": {
                            "svd_solver": {"not": {"enum": ["arpack", "randomized"]}}
                        },
                    },
                    {
                        "type": "object",
                        "properties": {"svd_solver": {"enum": ["arpack"]}},
                    },
                    {
                        "type": "object",
                        "properties": {"svd_solver": {"not": {"enum": ["randomized"]}}},
                    },
                    {"XXX TODO XXX": "check_random_state(self.random_state) is None"},
                    {
                        "XXX TODO XXX": "check_random_state(self.random_state) is np.random"
                    },
                    {
                        "XXX TODO XXX": "isinstance(check_random_state(self.random_state), np.random.RandomState)"
                    },
                ]
            },
        ],
    },
    {
        "description": "From /utils/validation.py:None:check_random_state, Exception: raise ValueError(     '%r cannot be used to seed a numpy.random.RandomState instance' % seed) ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "type": "object",
                        "properties": {"n_components": {"not": {"enum": [None]}}},
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"enum": ["arpack"]}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"not": {"enum": ["auto"]}}
                                        },
                                    },
                                    {"XXX TODO XXX": "max(X.shape) <= 500"},
                                    {"XXX TODO XXX": "min(X.shape) == 'mle'"},
                                    {"XXX TODO XXX": "min(X.shape) < 1"},
                                    {
                                        "XXX TODO XXX": "min(X.shape) >= 0.8 * min(X.shape)"
                                    },
                                    {
                                        "XXX TODO XXX": "check_random_state(check_random_state(self.random_state)) is None"
                                    },
                                    {
                                        "XXX TODO XXX": "check_random_state(check_random_state(self.random_state)) is np.random"
                                    },
                                    {
                                        "XXX TODO XXX": "isinstance(check_random_state(check_random_state(self.random_state)), np.random.RandomState)"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"not": {"enum": ["arpack"]}}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"not": {"enum": ["auto"]}}
                                        },
                                    },
                                    {"XXX TODO XXX": "max(X.shape) <= 500"},
                                    {"XXX TODO XXX": "min(X.shape) - 1 == 'mle'"},
                                    {"XXX TODO XXX": "min(X.shape) - 1 < 1"},
                                    {
                                        "XXX TODO XXX": "min(X.shape) - 1 >= 0.8 * min(X.shape)"
                                    },
                                    {
                                        "XXX TODO XXX": "check_random_state(check_random_state(self.random_state)) is None"
                                    },
                                    {
                                        "XXX TODO XXX": "check_random_state(check_random_state(self.random_state)) is np.random"
                                    },
                                    {
                                        "XXX TODO XXX": "isinstance(check_random_state(check_random_state(self.random_state)), np.random.RandomState)"
                                    },
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
                        "properties": {"n_components": {"enum": [None]}},
                    },
                    {
                        "type": "object",
                        "properties": {"svd_solver": {"not": {"enum": ["auto"]}}},
                    },
                    {"XXX TODO XXX": "max(X.shape) <= 500"},
                    {
                        "type": "object",
                        "properties": {"n_components": {"enum": ["mle"]}},
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
                    {"XXX TODO XXX": "self.n_components >= 0.8 * min(X.shape)"},
                    {
                        "XXX TODO XXX": "check_random_state(check_random_state(self.random_state)) is None"
                    },
                    {
                        "XXX TODO XXX": "check_random_state(check_random_state(self.random_state)) is np.random"
                    },
                    {
                        "XXX TODO XXX": "isinstance(check_random_state(check_random_state(self.random_state)), np.random.RandomState)"
                    },
                ]
            },
            {
                "anyOf": [
                    {
                        "type": "object",
                        "properties": {"svd_solver": {"enum": ["auto"]}},
                    },
                    {
                        "type": "object",
                        "properties": {"svd_solver": {"enum": ["full"]}},
                    },
                    {
                        "type": "object",
                        "properties": {
                            "svd_solver": {"not": {"enum": ["arpack", "randomized"]}}
                        },
                    },
                    {
                        "type": "object",
                        "properties": {"svd_solver": {"enum": ["arpack"]}},
                    },
                    {
                        "type": "object",
                        "properties": {"svd_solver": {"not": {"enum": ["randomized"]}}},
                    },
                    {
                        "XXX TODO XXX": "check_random_state(check_random_state(self.random_state)) is None"
                    },
                    {
                        "XXX TODO XXX": "check_random_state(check_random_state(self.random_state)) is np.random"
                    },
                    {
                        "XXX TODO XXX": "isinstance(check_random_state(check_random_state(self.random_state)), np.random.RandomState)"
                    },
                ]
            },
        ],
    },
    {
        "description": "From /decomposition/_pca.py:PCA:_fit_truncated, Exception: raise ValueError(\"n_components=%r cannot be a string with svd_solver='%s'\" %     (n_components, svd_solver)) ",
        "anyOf": [
            {"type": "object", "properties": {"n_components": {"enum": [None]}}},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "type": "object",
                                "properties": {
                                    "svd_solver": {"not": {"enum": ["auto"]}}
                                },
                            },
                            {"XXX TODO XXX": "max(X.shape) <= 500"},
                            {
                                "type": "object",
                                "properties": {"n_components": {"enum": ["mle"]}},
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
                            {"XXX TODO XXX": "self.n_components >= 0.8 * min(X.shape)"},
                            {
                                "type": "object",
                                "properties": {
                                    "n_components": {"not": {"type": "string"}}
                                },
                            },
                        ]
                    },
                    {
                        "anyOf": [
                            {
                                "type": "object",
                                "properties": {"svd_solver": {"enum": ["auto"]}},
                            },
                            {
                                "type": "object",
                                "properties": {"svd_solver": {"enum": ["full"]}},
                            },
                            {
                                "type": "object",
                                "properties": {
                                    "svd_solver": {
                                        "not": {"enum": ["arpack", "randomized"]}
                                    }
                                },
                            },
                            {
                                "type": "object",
                                "properties": {
                                    "n_components": {"not": {"type": "string"}}
                                },
                            },
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": "From /decomposition/_pca.py:PCA:_fit_truncated, Exception: raise ValueError(     \"n_components=%r must be between 1 and min(n_samples, n_features)=%r with svd_solver='%s'\"      % (n_components, min(n_samples, n_features), svd_solver)) ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "type": "object",
                        "properties": {"n_components": {"not": {"enum": [None]}}},
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"enum": ["arpack"]}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "not": {
                                                                    "enum": ["auto"]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "max(X.shape) <= 500"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) == 'mle'"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) < 1"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) >= 0.8 * min(X.shape)"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "1 <= X.shape"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "min(X.shape) <= X.shape[0]"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "min(X.shape) <= X.shape[1]"
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
                                                            "svd_solver": {
                                                                "enum": ["auto"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "enum": ["full"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "not": {
                                                                    "enum": [
                                                                        "arpack",
                                                                        "randomized",
                                                                    ]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "1 <= X.shape"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "min(X.shape) <= X.shape[0]"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "min(X.shape) <= X.shape[1]"
                                                            },
                                                        ]
                                                    },
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
                                            "svd_solver": {"not": {"enum": ["arpack"]}}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "not": {
                                                                    "enum": ["auto"]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "max(X.shape) <= 500"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) - 1 == 'mle'"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) - 1 < 1"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) - 1 >= 0.8 * min(X.shape)"
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "1 <= min(X.shape) - 1"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "min(X.shape) - 1 <= X.shape[0]"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "min(X.shape) - 1 <= X.shape[1]"
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
                                                            "svd_solver": {
                                                                "enum": ["auto"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "enum": ["full"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "not": {
                                                                    "enum": [
                                                                        "arpack",
                                                                        "randomized",
                                                                    ]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "1 <= min(X.shape) - 1"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "min(X.shape) - 1 <= X.shape[0]"
                                                            },
                                                            {
                                                                "XXX TODO XXX": "min(X.shape) - 1 <= X.shape[1]"
                                                            },
                                                        ]
                                                    },
                                                ]
                                            },
                                        ]
                                    },
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
                        "properties": {"n_components": {"enum": [None]}},
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"not": {"enum": ["auto"]}}
                                        },
                                    },
                                    {"XXX TODO XXX": "max(X.shape) <= 500"},
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_components": {"enum": ["mle"]}
                                        },
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
                                        "XXX TODO XXX": "self.n_components >= 0.8 * min(X.shape)"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_components": {"type": "string"}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "n_components": {
                                                        "type": "number",
                                                        "minimum": 1,
                                                    }
                                                },
                                            },
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "n_components": {
                                                        "laleMaximum": "X/maxItems"
                                                    }
                                                },
                                            },
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "n_components": {
                                                        "laleMaximum": "X/items/maxItems"
                                                    }
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
                                            "svd_solver": {"enum": ["auto"]}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"enum": ["full"]}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {
                                                "not": {
                                                    "enum": ["arpack", "randomized"]
                                                }
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_components": {"type": "string"}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "n_components": {
                                                        "type": "number",
                                                        "minimum": 1,
                                                    }
                                                },
                                            },
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "n_components": {
                                                        "laleMaximum": "X/maxItems"
                                                    }
                                                },
                                            },
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "n_components": {
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
        "description": "From /decomposition/_pca.py:PCA:_fit_truncated, Exception: raise ValueError(     'n_components=%r must be of type int when greater than or equal to 1, was of type=%r'      % (n_components, type(n_components))) ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "type": "object",
                        "properties": {"n_components": {"not": {"enum": [None]}}},
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"enum": ["arpack"]}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "not": {
                                                                    "enum": ["auto"]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "max(X.shape) <= 500"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) == 'mle'"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) < 1"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) >= 0.8 * min(X.shape)"
                                                    },
                                                    {"XXX TODO XXX": "1 > X.shape"},
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) > X.shape[0]"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) > X.shape[1]"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "isinstance(min(X.shape), numbers.Integral)"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "enum": ["auto"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "enum": ["full"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "not": {
                                                                    "enum": [
                                                                        "arpack",
                                                                        "randomized",
                                                                    ]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {"XXX TODO XXX": "1 > X.shape"},
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) > X.shape[0]"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) > X.shape[1]"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "isinstance(min(X.shape), numbers.Integral)"
                                                    },
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
                                            "svd_solver": {"not": {"enum": ["arpack"]}}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "not": {
                                                                    "enum": ["auto"]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "max(X.shape) <= 500"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) - 1 == 'mle'"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) - 1 < 1"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) - 1 >= 0.8 * min(X.shape)"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "1 > min(X.shape) - 1"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) - 1 > X.shape[0]"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) - 1 > X.shape[1]"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "isinstance(min(X.shape) - 1, numbers.Integral)"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "enum": ["auto"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "enum": ["full"]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "svd_solver": {
                                                                "not": {
                                                                    "enum": [
                                                                        "arpack",
                                                                        "randomized",
                                                                    ]
                                                                }
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "1 > min(X.shape) - 1"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) - 1 > X.shape[0]"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "min(X.shape) - 1 > X.shape[1]"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "isinstance(min(X.shape) - 1, numbers.Integral)"
                                                    },
                                                ]
                                            },
                                        ]
                                    },
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
                        "properties": {"n_components": {"enum": [None]}},
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"not": {"enum": ["auto"]}}
                                        },
                                    },
                                    {"XXX TODO XXX": "max(X.shape) <= 500"},
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_components": {"enum": ["mle"]}
                                        },
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
                                        "XXX TODO XXX": "self.n_components >= 0.8 * min(X.shape)"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_components": {"type": "string"}
                                        },
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
                                            "n_components": {
                                                "laleMinimum": "X/maxItems"
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_components": {
                                                "laleMinimum": "X/items/maxItems"
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_components": {"type": "integer"}
                                        },
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"enum": ["auto"]}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"enum": ["full"]}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {
                                                "not": {
                                                    "enum": ["arpack", "randomized"]
                                                }
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_components": {"type": "string"}
                                        },
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
                                            "n_components": {
                                                "laleMinimum": "X/maxItems"
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_components": {
                                                "laleMinimum": "X/items/maxItems"
                                            }
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "n_components": {"type": "integer"}
                                        },
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
        "description": "From /decomposition/_pca.py:PCA:_fit_truncated, Exception: raise ValueError(     \"n_components=%r must be strictly less than min(n_samples, n_features)=%r with svd_solver='%s'\"      % (n_components, min(n_samples, n_features), svd_solver)) ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "type": "object",
                        "properties": {"n_components": {"not": {"enum": [None]}}},
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"enum": ["arpack"]}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"enum": ["auto"]}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"enum": ["full"]}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {
                                                "not": {
                                                    "enum": ["arpack", "randomized"]
                                                }
                                            }
                                        },
                                    },
                                    {"XXX TODO XXX": "1 > X.shape"},
                                    {"XXX TODO XXX": "min(X.shape) > X.shape[0]"},
                                    {"XXX TODO XXX": "min(X.shape) > X.shape[1]"},
                                    {
                                        "XXX TODO XXX": "isinstance(min(X.shape), numbers.Integral)"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"not": {"enum": ["arpack"]}}
                                        },
                                    },
                                    {
                                        "XXX TODO XXX": "min(X.shape) != min(X.shape[0], X.shape[1])"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"not": {"enum": ["arpack"]}}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"enum": ["auto"]}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"enum": ["full"]}
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {
                                                "not": {
                                                    "enum": ["arpack", "randomized"]
                                                }
                                            }
                                        },
                                    },
                                    {"XXX TODO XXX": "1 > min(X.shape) - 1"},
                                    {"XXX TODO XXX": "min(X.shape) - 1 > X.shape[0]"},
                                    {"XXX TODO XXX": "min(X.shape) - 1 > X.shape[1]"},
                                    {
                                        "XXX TODO XXX": "isinstance(min(X.shape) - 1, numbers.Integral)"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "svd_solver": {"not": {"enum": ["arpack"]}}
                                        },
                                    },
                                    {
                                        "XXX TODO XXX": "min(X.shape) - 1 != min(X.shape[0], X.shape[1])"
                                    },
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
                        "properties": {"n_components": {"enum": [None]}},
                    },
                    {
                        "type": "object",
                        "properties": {"svd_solver": {"enum": ["auto"]}},
                    },
                    {
                        "type": "object",
                        "properties": {"svd_solver": {"enum": ["full"]}},
                    },
                    {
                        "type": "object",
                        "properties": {
                            "svd_solver": {"not": {"enum": ["arpack", "randomized"]}}
                        },
                    },
                    {
                        "type": "object",
                        "properties": {"n_components": {"type": "string"}},
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
                        "properties": {"n_components": {"laleMinimum": "X/maxItems"}},
                    },
                    {
                        "type": "object",
                        "properties": {
                            "n_components": {"laleMinimum": "X/items/maxItems"}
                        },
                    },
                    {
                        "type": "object",
                        "properties": {"n_components": {"not": {"type": "integer"}}},
                    },
                    {
                        "type": "object",
                        "properties": {"svd_solver": {"not": {"enum": ["arpack"]}}},
                    },
                    {
                        "XXX TODO XXX": "self.n_components != min(X.shape[0], X.shape[1])"
                    },
                ]
            },
        ],
    },
    {
        "description": "From /decomposition/_pca.py:PCA:_fit, Exception: raise TypeError(     'PCA does not support sparse input. See TruncatedSVD for a possible alternative.'     ) ",
        "type": "object",
        "laleNot": "X/isSparse",
    },
    {
        "description": "From /decomposition/_pca.py:PCA:_fit, Exception: raise ValueError(\"Unrecognized svd_solver='{0}'\".format(self._fit_svd_solver)) ",
        "anyOf": [
            {"type": "object", "properties": {"svd_solver": {"enum": ["auto"]}}},
            {"type": "object", "properties": {"svd_solver": {"enum": ["full"]}}},
            {
                "type": "object",
                "properties": {"svd_solver": {"enum": ["arpack", "randomized"]}},
            },
        ],
    },
]
