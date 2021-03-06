[
    {
        "description": "From /linear_model/_stochastic_gradient.py:BaseSGD:_validate_params, Exception: raise ValueError('shuffle must be either True or False') ",
        "type": "object",
        "properties": {"shuffle": {"type": "boolean"}},
    },
    {
        "description": "From /linear_model/_stochastic_gradient.py:BaseSGD:_validate_params, Exception: raise ValueError('early_stopping must be either True or False') ",
        "type": "object",
        "properties": {"early_stopping": {"type": "boolean"}},
    },
    {
        "description": "From /linear_model/_stochastic_gradient.py:BaseSGD:_validate_params, Exception: raise ValueError('max_iter must be > zero. Got %f' % self.max_iter) ",
        "anyOf": [
            {"type": "object", "properties": {"max_iter": {"enum": [None]}}},
            {
                "type": "object",
                "properties": {
                    "max_iter": {
                        "type": "number",
                        "minimum": 0,
                        "exclusiveMinimum": True,
                    }
                },
            },
        ],
    },
    {
        "description": "From /linear_model/_stochastic_gradient.py:BaseSGD:_validate_params, Exception: raise ValueError('l1_ratio must be in [0, 1]') ",
        "allOf": [
            {
                "type": "object",
                "properties": {"l1_ratio": {"type": "number", "minimum": 0.0}},
            },
            {
                "type": "object",
                "properties": {"l1_ratio": {"type": "number", "maximum": 1.0}},
            },
        ],
    },
    {
        "description": "From /linear_model/_stochastic_gradient.py:BaseSGD:_validate_params, Exception: raise ValueError('alpha must be >= 0') ",
        "type": "object",
        "properties": {"alpha": {"type": "number", "minimum": 0.0}},
    },
    {
        "description": "From /linear_model/_stochastic_gradient.py:BaseSGD:_validate_params, Exception: raise ValueError('n_iter_no_change must be >= 1') ",
        "type": "object",
        "properties": {"n_iter_no_change": {"type": "number", "minimum": 1}},
    },
    {
        "description": "From /linear_model/_stochastic_gradient.py:BaseSGD:_validate_params, Exception: raise ValueError('validation_fraction must be in range (0, 1)') ",
        "allOf": [
            {
                "type": "object",
                "properties": {
                    "validation_fraction": {
                        "type": "number",
                        "minimum": 0.0,
                        "exclusiveMinimum": True,
                    }
                },
            },
            {
                "type": "object",
                "properties": {
                    "validation_fraction": {
                        "type": "number",
                        "maximum": 1.0,
                        "exclusiveMaximum": True,
                    }
                },
            },
        ],
    },
    {
        "description": "From /linear_model/_stochastic_gradient.py:BaseSGD:_validate_params, Exception: raise ValueError('eta0 must be > 0') ",
        "anyOf": [
            {
                "type": "object",
                "properties": {
                    "learning_rate": {
                        "not": {"enum": ["constant", "invscaling", "adaptive"]}
                    }
                },
            },
            {
                "type": "object",
                "properties": {
                    "eta0": {"type": "number", "minimum": 0.0, "exclusiveMinimum": True}
                },
            },
        ],
    },
    {
        "description": "From /linear_model/_stochastic_gradient.py:BaseSGD:_validate_params, Exception: raise ValueError(     \"alpha must be > 0 since learning_rate is 'optimal'. alpha is used to compute the optimal learning rate.\"     ) ",
        "anyOf": [
            {
                "type": "object",
                "properties": {"learning_rate": {"not": {"enum": ["optimal"]}}},
            },
            {"type": "object", "properties": {"alpha": {"not": {"enum": [0]}}}},
        ],
    },
    {
        "description": "From /linear_model/_stochastic_gradient.py:BaseSGD:_validate_params, Exception: raise ValueError('The loss %s is not supported. ' % self.loss) ",
        "XXX TODO XXX": "self.loss in self.loss_functions",
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
        "description": "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Pandas DataFrame with mixed sparse extension arrays generated a sparse matrix with object dtype which can not be converted to a scipy sparse matrix.Sparse extension arrays should all have the same numeric type.'     ) ",
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "not hasattr(self, 'classes_')"},
                    {"type": "object", "properties": {"y": {"not": {"enum": [None]}}}},
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
                ]
            },
            {
                "anyOf": [
                    {"XXX TODO XXX": "hasattr(self, 'classes_')"},
                    {"type": "object", "properties": {"y": {"not": {"enum": [None]}}}},
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
        "description": "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Pandas DataFrame with mixed sparse extension arrays generated a sparse matrix with object dtype which can not be converted to a scipy sparse matrix.Sparse extension arrays should all have the same numeric type.'     ) ",
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "not hasattr(self, 'classes_')"},
                    {"type": "object", "properties": {"y": {"enum": [None]}}},
                    {
                        "type": "object",
                        "properties": {"y": {"not": {"type": "string"}}},
                    },
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
                    {"XXX TODO XXX": "hasattr(self, 'classes_')"},
                    {"type": "object", "properties": {"y": {"enum": [None]}}},
                    {
                        "type": "object",
                        "properties": {"y": {"not": {"type": "string"}}},
                    },
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
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "not hasattr(self, 'classes_')"},
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
                                    {
                                        "type": "object",
                                        "properties": {"y": {"enum": [None]}},
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
                    {"XXX TODO XXX": "hasattr(self, 'classes_')"},
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
                                    {
                                        "type": "object",
                                        "properties": {"y": {"enum": [None]}},
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
                                                    {"XXX TODO XXX": "sp.issparse(X)"},
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
                                                    {"XXX TODO XXX": "sp.issparse(X)"},
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
        ],
    },
    {
        "description": "From /utils/validation.py:None:_check_large_sparse, Exception: raise ValueError(     'Only sparse matrices with 32-bit integer indices are accepted. Got %s indices.'      % indices_datatype) ",
        "anyOf": [
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
                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False).fit)"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {"XXX TODO XXX": "sp.issparse(X)"},
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
                                                        "XXX TODO XXX": "not hasattr(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False), 'fit')"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not callable(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False).fit)"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {"XXX TODO XXX": "sp.issparse(X)"},
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
                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).ndim < 3"
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
                                        "XXX TODO XXX": "np.asarray(X.sparse.to_coo(), order='C', dtype=np.float64).ndim < 3"
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
                                        "XXX TODO XXX": "np.asarray(X, order='C', dtype=np.float64).ndim < 3"
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
                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False)) >= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {"XXX TODO XXX": "sp.issparse(X)"},
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
                                                        "XXX TODO XXX": "_num_samples(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False)) >= 1"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {"XXX TODO XXX": "sp.issparse(X)"},
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
                                                        "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False).ndim != 2"
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
                                                        "XXX TODO XXX": "_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, False).ndim != 2"
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
        ],
    },
    {
        "description": "From /utils/validation.py:None:_assert_all_finite, Exception: raise ValueError(msg_err.format(type_err, msg_dtype if msg_dtype is not     None else X.dtype)) ",
        "anyOf": [
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
        "description": "From /utils/validation.py:None:check_consistent_length, Exception: raise ValueError(     'Found input variables with inconsistent numbers of samples: %r' % [int     (l) for l in lengths]) ",
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "not hasattr(self, 'classes_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {"warm_start": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "not hasattr(self, 'coef_')"},
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "coef_init": {
                                                                "not": {"enum": [None]}
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
                                                                            "intercept_init": {
                                                                                "not": {
                                                                                    "enum": [
                                                                                        None
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
                                                                                        "type": "object",
                                                                                        "properties": {
                                                                                            "average": {
                                                                                                "type": "number",
                                                                                                "maximum": 0,
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
                                                                                            "average": {
                                                                                                "type": "number",
                                                                                                "minimum": 0,
                                                                                                "exclusiveMinimum": True,
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
                                                                        "type": "object",
                                                                        "properties": {
                                                                            "intercept_init": {
                                                                                "enum": [
                                                                                    None
                                                                                ]
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
                                                                                            "average": {
                                                                                                "type": "number",
                                                                                                "maximum": 0,
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
                                                                                            "average": {
                                                                                                "type": "number",
                                                                                                "minimum": 0,
                                                                                                "exclusiveMinimum": True,
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
                                                        ]
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "coef_init": {
                                                                "enum": [None]
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
                                                                            "intercept_init": {
                                                                                "not": {
                                                                                    "enum": [
                                                                                        None
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
                                                                                        "type": "object",
                                                                                        "properties": {
                                                                                            "average": {
                                                                                                "type": "number",
                                                                                                "maximum": 0,
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
                                                                                            "average": {
                                                                                                "type": "number",
                                                                                                "minimum": 0,
                                                                                                "exclusiveMinimum": True,
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
                                                                        "type": "object",
                                                                        "properties": {
                                                                            "intercept_init": {
                                                                                "enum": [
                                                                                    None
                                                                                ]
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
                                                                                            "average": {
                                                                                                "type": "number",
                                                                                                "maximum": 0,
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
                                                                                            "average": {
                                                                                                "type": "number",
                                                                                                "minimum": 0,
                                                                                                "exclusiveMinimum": True,
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
                                                        ]
                                                    },
                                                ]
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
                                                "type": "object",
                                                "properties": {
                                                    "warm_start": {"enum": [True]}
                                                },
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
                                                            "average": {
                                                                "type": "number",
                                                                "maximum": 0,
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
                                                            "average": {
                                                                "type": "number",
                                                                "minimum": 0,
                                                                "exclusiveMinimum": True,
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
                        ]
                    },
                ]
            },
            {
                "anyOf": [
                    {"XXX TODO XXX": "hasattr(self, 'classes_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {"warm_start": {"enum": [False]}},
                                    },
                                    {"XXX TODO XXX": "not hasattr(self, 'coef_')"},
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "coef_init": {
                                                                "not": {"enum": [None]}
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
                                                                            "intercept_init": {
                                                                                "not": {
                                                                                    "enum": [
                                                                                        None
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
                                                                                        "type": "object",
                                                                                        "properties": {
                                                                                            "average": {
                                                                                                "type": "number",
                                                                                                "maximum": 0,
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
                                                                                            "average": {
                                                                                                "type": "number",
                                                                                                "minimum": 0,
                                                                                                "exclusiveMinimum": True,
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
                                                                        "type": "object",
                                                                        "properties": {
                                                                            "intercept_init": {
                                                                                "enum": [
                                                                                    None
                                                                                ]
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
                                                                                            "average": {
                                                                                                "type": "number",
                                                                                                "maximum": 0,
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
                                                                                            "average": {
                                                                                                "type": "number",
                                                                                                "minimum": 0,
                                                                                                "exclusiveMinimum": True,
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
                                                        ]
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "coef_init": {
                                                                "enum": [None]
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
                                                                            "intercept_init": {
                                                                                "not": {
                                                                                    "enum": [
                                                                                        None
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
                                                                                        "type": "object",
                                                                                        "properties": {
                                                                                            "average": {
                                                                                                "type": "number",
                                                                                                "maximum": 0,
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
                                                                                            "average": {
                                                                                                "type": "number",
                                                                                                "minimum": 0,
                                                                                                "exclusiveMinimum": True,
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
                                                                        "type": "object",
                                                                        "properties": {
                                                                            "intercept_init": {
                                                                                "enum": [
                                                                                    None
                                                                                ]
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
                                                                                            "average": {
                                                                                                "type": "number",
                                                                                                "maximum": 0,
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
                                                                                            "average": {
                                                                                                "type": "number",
                                                                                                "minimum": 0,
                                                                                                "exclusiveMinimum": True,
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
                                                        ]
                                                    },
                                                ]
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
                                                "type": "object",
                                                "properties": {
                                                    "warm_start": {"enum": [True]}
                                                },
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
                                                            "average": {
                                                                "type": "number",
                                                                "maximum": 0,
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
                                                            "average": {
                                                                "type": "number",
                                                                "minimum": 0,
                                                                "exclusiveMinimum": True,
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
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": "From /utils/validation.py:None:check_X_y, Exception: raise ValueError('y cannot be None') ",
        "type": "object",
        "properties": {"y": {"not": {"enum": [None]}}},
    },
    {
        "description": "From /utils/validation.py:None:_assert_all_finite, Exception: raise ValueError(msg_err.format(type_err, msg_dtype if msg_dtype is not     None else X.dtype)) ",
        "anyOf": [
            {
                "allOf": [
                    {"XXX TODO XXX": "getattr(self, 'classes_', None) is None"},
                    {"XXX TODO XXX": "np.unique(y) is None"},
                ]
            },
            {"XXX TODO XXX": "np.unique(y) is None"},
            {"XXX TODO XXX": "getattr(self, 'classes_', None) is not None"},
            {"XXX TODO XXX": "is_multilabel(x)"},
            {"XXX TODO XXX": "x.ndim > 2"},
            {
                "allOf": [
                    {"XXX TODO XXX": "x.dtype == object"},
                    {"XXX TODO XXX": "len(x)"},
                    {"XXX TODO XXX": "isinstance(y.flat[0], str)"},
                ]
            },
            {
                "allOf": [
                    {"XXX TODO XXX": "x.ndim == 2"},
                    {"XXX TODO XXX": "y.shape[1] == 0"},
                ]
            },
            {"XXX TODO XXX": "x.dtype.kind != 'f'"},
            {"XXX TODO XXX": "not np.any(x != x.astype(int))"},
            {"XXX TODO XXX": "_get_config()['assume_finite']"},
            {
                "allOf": [
                    {"XXX TODO XXX": "x.dtype.kind in 'fc'"},
                    {"XXX TODO XXX": "np.isfinite(_safe_accumulator_op(np.sum, x))"},
                ]
            },
            {"XXX TODO XXX": "x.dtype.kind not in 'fc'"},
            {"XXX TODO XXX": "np.isfinite(x).all()"},
        ],
    },
    {
        "description": "From /utils/validation.py:None:_assert_all_finite, Exception: raise ValueError('Input contains NaN') ",
        "anyOf": [
            {
                "allOf": [
                    {"XXX TODO XXX": "getattr(self, 'classes_', None) is None"},
                    {"XXX TODO XXX": "np.unique(y) is None"},
                ]
            },
            {"XXX TODO XXX": "np.unique(y) is None"},
            {"XXX TODO XXX": "getattr(self, 'classes_', None) is not None"},
            {"XXX TODO XXX": "is_multilabel(x)"},
            {"XXX TODO XXX": "x.ndim > 2"},
            {
                "allOf": [
                    {"XXX TODO XXX": "x.dtype == object"},
                    {"XXX TODO XXX": "len(x)"},
                    {"XXX TODO XXX": "isinstance(y.flat[0], str)"},
                ]
            },
            {
                "allOf": [
                    {"XXX TODO XXX": "x.ndim == 2"},
                    {"XXX TODO XXX": "y.shape[1] == 0"},
                ]
            },
            {"XXX TODO XXX": "x.dtype.kind != 'f'"},
            {"XXX TODO XXX": "not np.any(x != x.astype(int))"},
            {"XXX TODO XXX": "_get_config()['assume_finite']"},
            {
                "allOf": [
                    {"XXX TODO XXX": "x.dtype.kind in 'fc'"},
                    {"XXX TODO XXX": "np.isfinite(_safe_accumulator_op(np.sum, x))"},
                ]
            },
            {"XXX TODO XXX": "x.dtype.kind in 'fc'"},
            {"XXX TODO XXX": "x.dtype != np.dtype('object')"},
            {"XXX TODO XXX": "not _object_dtype_isnan(x).any()"},
        ],
    },
    {
        "description": "From /utils/multiclass.py:None:type_of_target, Exception: raise ValueError(     'Expected array-like (array or non-string sequence), got %r' % y) ",
        "anyOf": [
            {
                "allOf": [
                    {"XXX TODO XXX": "getattr(self, 'classes_', None) is None"},
                    {"XXX TODO XXX": "np.unique(y) is None"},
                ]
            },
            {"XXX TODO XXX": "np.unique(y) is None"},
            {"XXX TODO XXX": "getattr(self, 'classes_', None) is not None"},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {"XXX TODO XXX": "isinstance(x, [Sequence, spmatrix])"},
                            {"XXX TODO XXX": "hasattr(x, '__array__')"},
                        ]
                    },
                    {
                        "type": "object",
                        "properties": {"x": {"not": {"type": "string"}}},
                    },
                ]
            },
        ],
    },
    {
        "description": "From /utils/multiclass.py:None:type_of_target, Exception: raise ValueError(\"y cannot be class 'SparseSeries' or 'SparseArray'\") ",
        "anyOf": [
            {
                "allOf": [
                    {"XXX TODO XXX": "getattr(self, 'classes_', None) is None"},
                    {"XXX TODO XXX": "np.unique(y) is None"},
                ]
            },
            {"XXX TODO XXX": "np.unique(y) is None"},
            {"XXX TODO XXX": "getattr(self, 'classes_', None) is not None"},
            {
                "XXX TODO XXX": "x.__class__.__name__ not in ['SparseSeries', 'SparseArray']"
            },
        ],
    },
    {
        "description": "From /utils/multiclass.py:None:type_of_target, Exception: raise ValueError(     'You appear to be using a legacy multi-label data representation. Sequence of sequences are no longer supported; use a binary array or sparse matrix instead - the MultiLabelBinarizer transformer can convert to this format.'     ) ",
        "anyOf": [
            {
                "allOf": [
                    {"XXX TODO XXX": "getattr(self, 'classes_', None) is None"},
                    {"XXX TODO XXX": "np.unique(y) is None"},
                ]
            },
            {"XXX TODO XXX": "np.unique(y) is None"},
            {"XXX TODO XXX": "getattr(self, 'classes_', None) is not None"},
            {"XXX TODO XXX": "is_multilabel(x)"},
            {"XXX TODO XXX": "hasattr(y[0], '__array__')"},
            {"XXX TODO XXX": "isinstance(y[0], Sequence)"},
            {"XXX TODO XXX": "isinstance(y[0], str)"},
        ],
    },
    {
        "description": "From /utils/multiclass.py:None:unique_labels, Exception: raise ValueError('No argument has been passed.') ",
        "anyOf": [
            {
                "allOf": [
                    {"XXX TODO XXX": "getattr(self, 'classes_', None) is None"},
                    {"XXX TODO XXX": "np.unique(y) is None"},
                ]
            },
            {"XXX TODO XXX": "np.unique(y) is None"},
            {"XXX TODO XXX": "getattr(self, 'classes_', None) is not None"},
            {"type": "object", "properties": {"ys": {"enum": [True]}}},
        ],
    },
    {
        "description": "From /utils/multiclass.py:None:unique_labels, Exception: raise ValueError('Mix type of y not allowed, got types %s' % ys_types) ",
        "anyOf": [
            {
                "allOf": [
                    {"XXX TODO XXX": "getattr(self, 'classes_', None) is None"},
                    {"XXX TODO XXX": "np.unique(y) is None"},
                ]
            },
            {"XXX TODO XXX": "np.unique(y) is None"},
            {"XXX TODO XXX": "getattr(self, 'classes_', None) is not None"},
            {
                "XXX TODO XXX": "set((type_of_target(x) for x in ys)) == {'binary', 'multiclass'}"
            },
            {"XXX TODO XXX": "len(set((type_of_target(x) for x in ys))) <= 1"},
        ],
    },
    {
        "description": "From /utils/multiclass.py:None:unique_labels, Exception: raise ValueError(     'Multi-label binary indicator input with different numbers of labels') ",
        "anyOf": [
            {
                "allOf": [
                    {"XXX TODO XXX": "getattr(self, 'classes_', None) is None"},
                    {"XXX TODO XXX": "np.unique(y) is None"},
                ]
            },
            {"XXX TODO XXX": "np.unique(y) is None"},
            {"XXX TODO XXX": "getattr(self, 'classes_', None) is not None"},
            {
                "XXX TODO XXX": "set((type_of_target(x) for x in ys)) == {'binary', 'multiclass'}"
            },
            {
                "XXX TODO XXX": "set((type_of_target(x) for x in ys)).pop() != 'multilabel-indicator'"
            },
            {
                "XXX TODO XXX": "len(set((check_array(y, accept_sparse=['csr', 'csc', 'coo']).shape[1] for y in ys))) <= 1"
            },
        ],
    },
    {
        "description": "From /utils/multiclass.py:None:unique_labels, Exception: raise ValueError('Unknown label type: %s' % repr(ys)) ",
        "anyOf": [
            {
                "allOf": [
                    {"XXX TODO XXX": "getattr(self, 'classes_', None) is None"},
                    {"XXX TODO XXX": "np.unique(y) is None"},
                ]
            },
            {"XXX TODO XXX": "np.unique(y) is None"},
            {"XXX TODO XXX": "getattr(self, 'classes_', None) is not None"},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "set((type_of_target(x) for x in ys)) != {'binary', 'multiclass'}"
                            },
                            {
                                "XXX TODO XXX": "_FN_UNIQUE_LABELS.get({'multiclass'}.pop(), None)"
                            },
                        ]
                    },
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "set((type_of_target(x) for x in ys)) == {'binary', 'multiclass'}"
                            },
                            {
                                "XXX TODO XXX": "_FN_UNIQUE_LABELS.get(set((type_of_target(x) for x in ys)).pop(), None)"
                            },
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": "From /utils/multiclass.py:None:unique_labels, Exception: raise ValueError('Mix of label input types (string and number)') ",
        "anyOf": [
            {
                "allOf": [
                    {"XXX TODO XXX": "getattr(self, 'classes_', None) is None"},
                    {"XXX TODO XXX": "np.unique(y) is None"},
                ]
            },
            {"XXX TODO XXX": "np.unique(y) is None"},
            {"XXX TODO XXX": "getattr(self, 'classes_', None) is not None"},
            {
                "allOf": [
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "set((type_of_target(x) for x in ys)) != {'binary', 'multiclass'}"
                            },
                            {
                                "XXX TODO XXX": "len(set((isinstance(label, str) for label in set(chain.from_iterable((_FN_UNIQUE_LABELS.get({'multiclass'}.pop(), None)(y) for y in ys)))))) <= 1"
                            },
                        ]
                    },
                    {
                        "anyOf": [
                            {
                                "XXX TODO XXX": "set((type_of_target(x) for x in ys)) == {'binary', 'multiclass'}"
                            },
                            {
                                "XXX TODO XXX": "len(set((isinstance(label, str) for label in set(chain.from_iterable((_FN_UNIQUE_LABELS.get(set((type_of_target(x) for x in ys)).pop(), None)(y) for y in ys)))))) <= 1"
                            },
                        ]
                    },
                ]
            },
        ],
    },
    {
        "description": "From /utils/multiclass.py:None:_check_partial_fit_first_call, Exception: raise ValueError('classes must be passed on the first call to partial_fit.') ",
        "anyOf": [
            {"XXX TODO XXX": "getattr(self, 'classes_', None) is not None"},
            {"XXX TODO XXX": "np.unique(y) is not None"},
        ],
    },
    {
        "description": "From /utils/multiclass.py:None:_check_partial_fit_first_call, Exception: raise ValueError(     '`classes=%r` is not the same as on last call to partial_fit, was: %r' %     (classes, clf.classes_)) ",
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "not hasattr(self, 'classes_')"},
                    {
                        "allOf": [
                            {"XXX TODO XXX": "getattr(self, 'classes_', None) is None"},
                            {"XXX TODO XXX": "np.unique(y) is None"},
                        ]
                    },
                    {"XXX TODO XXX": "np.unique(y) is None"},
                    {"XXX TODO XXX": "getattr(self, 'classes_', None) is None"},
                    {
                        "XXX TODO XXX": "np.array_equal(None, unique_labels(np.unique(y)))"
                    },
                ]
            },
            {
                "anyOf": [
                    {"XXX TODO XXX": "hasattr(self, 'classes_')"},
                    {
                        "allOf": [
                            {"XXX TODO XXX": "getattr(self, 'classes_', None) is None"},
                            {"XXX TODO XXX": "np.unique(y) is None"},
                        ]
                    },
                    {"XXX TODO XXX": "np.unique(y) is None"},
                    {"XXX TODO XXX": "getattr(self, 'classes_', None) is None"},
                    {
                        "XXX TODO XXX": "np.array_equal(self.classes_, unique_labels(np.unique(y)))"
                    },
                ]
            },
        ],
    },
    {
        "description": "From /utils/class_weight.py:None:compute_class_weight, Exception: raise ValueError('classes should include all valid labels that can be in y') ",
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "not hasattr(self, 'classes_')"},
                    {"XXX TODO XXX": "not set(y) - set(None)"},
                ]
            },
            {
                "anyOf": [
                    {"XXX TODO XXX": "hasattr(self, 'classes_')"},
                    {"XXX TODO XXX": "not set(y) - set(self.classes_)"},
                ]
            },
        ],
    },
    {
        "description": "From /utils/class_weight.py:None:compute_class_weight, Exception: raise ValueError('classes should have valid labels that are in y') ",
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "not hasattr(self, 'classes_')"},
                    {
                        "type": "object",
                        "properties": {"class_weight": {"enum": [None]}},
                    },
                    {"XXX TODO XXX": "len(self.class_weight) == 0"},
                    {
                        "type": "object",
                        "properties": {"class_weight": {"not": {"enum": ["balanced"]}}},
                    },
                    {"XXX TODO XXX": "all(np.in1d(None, LabelEncoder().classes_))"},
                ]
            },
            {
                "anyOf": [
                    {"XXX TODO XXX": "hasattr(self, 'classes_')"},
                    {
                        "type": "object",
                        "properties": {"class_weight": {"enum": [None]}},
                    },
                    {"XXX TODO XXX": "len(self.class_weight) == 0"},
                    {
                        "type": "object",
                        "properties": {"class_weight": {"not": {"enum": ["balanced"]}}},
                    },
                    {
                        "XXX TODO XXX": "all(np.in1d(self.classes_, LabelEncoder().classes_))"
                    },
                ]
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
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "not hasattr(self, 'classes_')"},
                    {
                        "type": "object",
                        "properties": {"class_weight": {"enum": [None]}},
                    },
                    {"XXX TODO XXX": "len(self.class_weight) == 0"},
                    {
                        "type": "object",
                        "properties": {"class_weight": {"enum": ["balanced"]}},
                    },
                    {"XXX TODO XXX": "c not in self.class_weight"},
                    {
                        "allOf": [
                            {"XXX TODO XXX": "np.searchsorted(None, c) < len(None)"},
                            {"XXX TODO XXX": "classes[i] == c"},
                        ]
                    },
                ]
            },
            {
                "anyOf": [
                    {"XXX TODO XXX": "hasattr(self, 'classes_')"},
                    {
                        "type": "object",
                        "properties": {"class_weight": {"enum": [None]}},
                    },
                    {"XXX TODO XXX": "len(self.class_weight) == 0"},
                    {
                        "type": "object",
                        "properties": {"class_weight": {"enum": ["balanced"]}},
                    },
                    {"XXX TODO XXX": "c not in self.class_weight"},
                    {
                        "allOf": [
                            {
                                "XXX TODO XXX": "np.searchsorted(self.classes_, c) < len(self.classes_)"
                            },
                            {"XXX TODO XXX": "classes[i] == c"},
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
        "description": "From /linear_model/_stochastic_gradient.py:BaseSGD:_allocate_parameter_mem, Exception: raise ValueError('Provided ``coef_`` does not match dataset. ') ",
        "allOf": [
            {
                "anyOf": [
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'coef_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "coef_init": {"not": {"enum": [None]}}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "getattr(self, 'coef_', None) is not None"
                                            },
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "coef_": {"enum": [None]}
                                                },
                                            },
                                        ]
                                    },
                                    {"XXX TODO XXX": "self.classes_.shape[0] <= 2"},
                                    {
                                        "type": "object",
                                        "properties": {"coef_": {"enum": [None]}},
                                    },
                                    {
                                        "XXX TODO XXX": "np.asarray(self.coef_, order='C').shape == [self.classes_.shape[0], X.shape[1]]"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {"coef_init": {"enum": [None]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "getattr(self, 'coef_', None) is not None"
                                            },
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "coef_init": {"enum": [None]}
                                                },
                                            },
                                        ]
                                    },
                                    {"XXX TODO XXX": "self.classes_.shape[0] <= 2"},
                                    {
                                        "type": "object",
                                        "properties": {"coef_init": {"enum": [None]}},
                                    },
                                    {
                                        "XXX TODO XXX": "np.asarray(coef_init, order='C').shape == [self.classes_.shape[0], X.shape[1]]"
                                    },
                                ]
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
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'coef_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "XXX TODO XXX": "getattr(self, 'coef_', None) is not None"
                            },
                            {
                                "type": "object",
                                "properties": {"coef_init": {"enum": [None]}},
                            },
                        ]
                    },
                    {"XXX TODO XXX": "self.classes_.shape[0] <= 2"},
                    {"type": "object", "properties": {"coef_init": {"enum": [None]}}},
                    {
                        "XXX TODO XXX": "np.asarray(coef_init, order='C').shape == [self.classes_.shape[0], X.shape[1]]"
                    },
                ]
            },
        ],
    },
    {
        "description": "From /linear_model/_stochastic_gradient.py:BaseSGD:_allocate_parameter_mem, Exception: raise ValueError('Provided intercept_init does not match dataset.') ",
        "allOf": [
            {
                "anyOf": [
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'coef_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "coef_init": {"not": {"enum": [None]}}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "intercept_init": {
                                                                "not": {"enum": [None]}
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "getattr(self, 'coef_', None) is not None"
                                                            },
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "coef_": {
                                                                        "enum": [None]
                                                                    }
                                                                },
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "XXX TODO XXX": "self.classes_.shape[0] <= 2"
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "intercept_": {
                                                                "enum": [None]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(self.intercept_, order='C').shape == [self.classes_.shape[0]]"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "intercept_init": {
                                                                "enum": [None]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "getattr(self, 'coef_', None) is not None"
                                                            },
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "coef_": {
                                                                        "enum": [None]
                                                                    }
                                                                },
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "XXX TODO XXX": "self.classes_.shape[0] <= 2"
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "intercept_init": {
                                                                "enum": [None]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(intercept_init, order='C').shape == [self.classes_.shape[0]]"
                                                    },
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
                                        "properties": {"coef_init": {"enum": [None]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "intercept_init": {
                                                                "not": {"enum": [None]}
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "getattr(self, 'coef_', None) is not None"
                                                            },
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "coef_init": {
                                                                        "enum": [None]
                                                                    }
                                                                },
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "XXX TODO XXX": "self.classes_.shape[0] <= 2"
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "intercept_": {
                                                                "enum": [None]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(self.intercept_, order='C').shape == [self.classes_.shape[0]]"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "intercept_init": {
                                                                "enum": [None]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "getattr(self, 'coef_', None) is not None"
                                                            },
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "coef_init": {
                                                                        "enum": [None]
                                                                    }
                                                                },
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "XXX TODO XXX": "self.classes_.shape[0] <= 2"
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "intercept_init": {
                                                                "enum": [None]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(intercept_init, order='C').shape == [self.classes_.shape[0]]"
                                                    },
                                                ]
                                            },
                                        ]
                                    },
                                ]
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
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'coef_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "XXX TODO XXX": "getattr(self, 'coef_', None) is not None"
                            },
                            {
                                "type": "object",
                                "properties": {"coef_init": {"enum": [None]}},
                            },
                        ]
                    },
                    {"XXX TODO XXX": "self.classes_.shape[0] <= 2"},
                    {
                        "type": "object",
                        "properties": {"intercept_init": {"enum": [None]}},
                    },
                    {
                        "XXX TODO XXX": "np.asarray(intercept_init, order='C').shape == [self.classes_.shape[0]]"
                    },
                ]
            },
        ],
    },
    {
        "description": "From /linear_model/_stochastic_gradient.py:BaseSGD:_allocate_parameter_mem, Exception: raise ValueError('Provided coef_init does not match dataset.') ",
        "allOf": [
            {
                "anyOf": [
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'coef_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "coef_init": {"not": {"enum": [None]}}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "getattr(self, 'coef_', None) is not None"
                                            },
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "coef_": {"enum": [None]}
                                                },
                                            },
                                        ]
                                    },
                                    {"XXX TODO XXX": "self.classes_.shape[0] > 2"},
                                    {
                                        "type": "object",
                                        "properties": {"coef_": {"enum": [None]}},
                                    },
                                    {
                                        "XXX TODO XXX": "np.asarray(self.coef_, dtype=np.float64, order='C').ravel().shape == [X.shape[1]]"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {"coef_init": {"enum": [None]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "XXX TODO XXX": "getattr(self, 'coef_', None) is not None"
                                            },
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "coef_init": {"enum": [None]}
                                                },
                                            },
                                        ]
                                    },
                                    {"XXX TODO XXX": "self.classes_.shape[0] > 2"},
                                    {
                                        "type": "object",
                                        "properties": {"coef_init": {"enum": [None]}},
                                    },
                                    {
                                        "XXX TODO XXX": "np.asarray(coef_init, dtype=np.float64, order='C').ravel().shape == [X.shape[1]]"
                                    },
                                ]
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
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'coef_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "XXX TODO XXX": "getattr(self, 'coef_', None) is not None"
                            },
                            {
                                "type": "object",
                                "properties": {"coef_init": {"enum": [None]}},
                            },
                        ]
                    },
                    {"XXX TODO XXX": "self.classes_.shape[0] > 2"},
                    {"type": "object", "properties": {"coef_init": {"enum": [None]}}},
                    {
                        "XXX TODO XXX": "np.asarray(coef_init, dtype=np.float64, order='C').ravel().shape == [X.shape[1]]"
                    },
                ]
            },
        ],
    },
    {
        "description": "From /linear_model/_stochastic_gradient.py:BaseSGD:_allocate_parameter_mem, Exception: raise ValueError('Provided intercept_init does not match dataset.') ",
        "allOf": [
            {
                "anyOf": [
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'coef_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "coef_init": {"not": {"enum": [None]}}
                                        },
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "intercept_init": {
                                                                "not": {"enum": [None]}
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "getattr(self, 'coef_', None) is not None"
                                                            },
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "coef_": {
                                                                        "enum": [None]
                                                                    }
                                                                },
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "XXX TODO XXX": "self.classes_.shape[0] > 2"
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "intercept_": {
                                                                "enum": [None]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(self.intercept_, dtype=np.float64).shape == [1]"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(self.intercept_, dtype=np.float64).shape == []"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "intercept_init": {
                                                                "enum": [None]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "getattr(self, 'coef_', None) is not None"
                                                            },
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "coef_": {
                                                                        "enum": [None]
                                                                    }
                                                                },
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "XXX TODO XXX": "self.classes_.shape[0] > 2"
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "intercept_init": {
                                                                "enum": [None]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(intercept_init, dtype=np.float64).shape == [1]"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(intercept_init, dtype=np.float64).shape == []"
                                                    },
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
                                        "properties": {"coef_init": {"enum": [None]}},
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "intercept_init": {
                                                                "not": {"enum": [None]}
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "getattr(self, 'coef_', None) is not None"
                                                            },
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "coef_init": {
                                                                        "enum": [None]
                                                                    }
                                                                },
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "XXX TODO XXX": "self.classes_.shape[0] > 2"
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "intercept_": {
                                                                "enum": [None]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(self.intercept_, dtype=np.float64).shape == [1]"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(self.intercept_, dtype=np.float64).shape == []"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "intercept_init": {
                                                                "enum": [None]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "XXX TODO XXX": "getattr(self, 'coef_', None) is not None"
                                                            },
                                                            {
                                                                "type": "object",
                                                                "properties": {
                                                                    "coef_init": {
                                                                        "enum": [None]
                                                                    }
                                                                },
                                                            },
                                                        ]
                                                    },
                                                    {
                                                        "XXX TODO XXX": "self.classes_.shape[0] > 2"
                                                    },
                                                    {
                                                        "type": "object",
                                                        "properties": {
                                                            "intercept_init": {
                                                                "enum": [None]
                                                            }
                                                        },
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(intercept_init, dtype=np.float64).shape == [1]"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "np.asarray(intercept_init, dtype=np.float64).shape == []"
                                                    },
                                                ]
                                            },
                                        ]
                                    },
                                ]
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
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'coef_')"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "XXX TODO XXX": "getattr(self, 'coef_', None) is not None"
                            },
                            {
                                "type": "object",
                                "properties": {"coef_init": {"enum": [None]}},
                            },
                        ]
                    },
                    {"XXX TODO XXX": "self.classes_.shape[0] > 2"},
                    {
                        "type": "object",
                        "properties": {"intercept_init": {"enum": [None]}},
                    },
                    {
                        "XXX TODO XXX": "np.asarray(intercept_init, dtype=np.float64).shape == [1]"
                    },
                    {
                        "XXX TODO XXX": "np.asarray(intercept_init, dtype=np.float64).shape == []"
                    },
                ]
            },
        ],
    },
    {
        "description": "From /linear_model/_stochastic_gradient.py:BaseSGD:_make_validation_split, Exception: raise ValueError(     'Splitting %d samples into a train set and a validation set with validation_fraction=%r led to an empty set (%d and %d samples). Please either change validation_fraction, increase number of samples, or disable early_stopping.'      % (n_samples, self.validation_fraction, idx_train.shape[0], idx_val.     shape[0])) ",
        "anyOf": [
            {"XXX TODO XXX": "self.classes_.shape[0] <= 2"},
            {"type": "object", "properties": {"early_stopping": {"enum": [False]}}},
            {
                "allOf": [
                    {"XXX TODO XXX": "idx_train.shape[0] != 0"},
                    {"XXX TODO XXX": "idx_val.shape[0] != 0"},
                ]
            },
        ],
    },
    {
        "description": "From /utils/validation.py:None:check_random_state, Exception: raise ValueError(     '%r cannot be used to seed a numpy.random.RandomState instance' % seed) ",
        "anyOf": [
            {"XXX TODO XXX": "self.classes_.shape[0] <= 2"},
            {"type": "object", "properties": {"random_state": {"enum": [None]}}},
            {"XXX TODO XXX": "self.random_state is np.random"},
            {"XXX TODO XXX": "isinstance(self.random_state, np.random.RandomState)"},
        ],
    },
    {
        "description": "From /utils/fixes.py:None:_joblib_parallel_args, Exception: raise ValueError('require=%s is not supported' % require) ",
        "anyOf": [
            {"XXX TODO XXX": "self.classes_.shape[0] <= 2"},
            {
                "XXX TODO XXX": "parse_version(joblib.__version__) >= parse_version('0.12')"
            },
            {"XXX TODO XXX": "kwargs['require'] in [None, 'sharedmem']"},
        ],
    },
    {
        "description": "From /utils/validation.py:None:check_random_state, Exception: raise ValueError(     '%r cannot be used to seed a numpy.random.RandomState instance' % seed) ",
        "anyOf": [
            {"XXX TODO XXX": "self.classes_.shape[0] > 2"},
            {"XXX TODO XXX": "self.classes_.shape[0] != 2"},
            {"type": "object", "properties": {"random_state": {"enum": [None]}}},
            {"XXX TODO XXX": "self.random_state is np.random"},
            {"XXX TODO XXX": "isinstance(self.random_state, np.random.RandomState)"},
        ],
    },
    {
        "description": "From /utils/validation.py:None:check_random_state, Exception: raise ValueError(     '%r cannot be used to seed a numpy.random.RandomState instance' % seed) ",
        "anyOf": [
            {"XXX TODO XXX": "self.classes_.shape[0] > 2"},
            {"XXX TODO XXX": "self.classes_.shape[0] != 2"},
            {"XXX TODO XXX": "check_random_state(self.random_state) is None"},
            {"XXX TODO XXX": "check_random_state(self.random_state) is np.random"},
            {
                "XXX TODO XXX": "isinstance(check_random_state(self.random_state), np.random.RandomState)"
            },
        ],
    },
    {
        "description": "From /linear_model/_stochastic_gradient.py:BaseSGDClassifier:_partial_fit, Exception: raise ValueError('Number of features %d does not match previous data %d.' %     (n_features, self.coef_.shape[-1])) ",
        "allOf": [
            {
                "anyOf": [
                    {"type": "object", "properties": {"warm_start": {"enum": [False]}}},
                    {"XXX TODO XXX": "not hasattr(self, 'coef_')"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "coef_init": {"not": {"enum": [None]}}
                                        },
                                    },
                                    {
                                        "XXX TODO XXX": "getattr(self, 'coef_', None) is None"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "coef_": {"not": {"enum": [None]}}
                                        },
                                    },
                                    {
                                        "XXX TODO XXX": "X.shape[1] == self.coef_.shape[-1]"
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "properties": {"coef_init": {"enum": [None]}},
                                    },
                                    {
                                        "XXX TODO XXX": "getattr(self, 'coef_', None) is None"
                                    },
                                    {
                                        "type": "object",
                                        "properties": {
                                            "coef_init": {"not": {"enum": [None]}}
                                        },
                                    },
                                    {
                                        "XXX TODO XXX": "X.shape[1] == self.coef_.shape[-1]"
                                    },
                                ]
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
                                "type": "object",
                                "properties": {"warm_start": {"enum": [True]}},
                            },
                            {"XXX TODO XXX": "hasattr(self, 'coef_')"},
                        ]
                    },
                    {"XXX TODO XXX": "getattr(self, 'coef_', None) is None"},
                    {
                        "type": "object",
                        "properties": {"coef_init": {"not": {"enum": [None]}}},
                    },
                    {"XXX TODO XXX": "X.shape[1] == self.coef_.shape[-1]"},
                ]
            },
        ],
    },
    {
        "description": "From /linear_model/_stochastic_gradient.py:BaseSGDClassifier:_partial_fit, Exception: raise ValueError(     'The number of classes has to be greater than one; got %d class' %     n_classes) ",
        "anyOf": [
            {"XXX TODO XXX": "self.classes_.shape[0] > 2"},
            {"XXX TODO XXX": "self.classes_.shape[0] == 2"},
        ],
    },
]
