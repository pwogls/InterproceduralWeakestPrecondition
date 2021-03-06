[{'description':
    'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) '
    , 'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(X.sparse.to_coo(), 'dtype')"}, {'XXX TODO XXX':
    'X.sparse.to_coo().dtype is None'}, {'XXX TODO XXX':
    "not hasattr(X.sparse.to_coo().dtype, 'kind')"}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype.kind != 'c'"}]}, {'anyOf': [{'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}
    ]}, {'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(X, 'dtype')"}, {'XXX TODO XXX': 'X.dtype is None'}, {
    'XXX TODO XXX': "not hasattr(X.dtype, 'kind')"}, {'XXX TODO XXX':
    "X.dtype.kind != 'c'"}]}]}, {'description':
    'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) '
    , 'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "not hasattr(X.dtypes, '__array__')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX':
    'not all((False for [np.float64, np.float32] in list(X.dtypes)))'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX':
    'np.result_type(*list(X.dtypes)) is None'}, {'XXX TODO XXX':
    'np.result_type(*list(X.dtypes)) not in [np.float64, np.float32]'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'dtype')"}, {
    'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, None).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, None).dtype, 'kind')"},
    {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind != 'c'"}]}, {
    'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'XXX TODO XXX': "not hasattr(np.asarray(X, None, None), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, None).dtype is None'}, {
    'XXX TODO XXX': "not hasattr(np.asarray(X, None, None).dtype, 'kind')"},
    {'XXX TODO XXX': "np.asarray(X, None, None).dtype.kind != 'c'"}]}]}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX':
    'np.result_type(*list(X.dtypes)) is not None'}, {'XXX TODO XXX':
    'np.result_type(*list(X.dtypes)) in [np.float64, np.float32]'}]}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind != 'c'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=dtype[0]).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=dtype[0]).dtype, 'kind')"}, {
    'XXX TODO XXX': "np.asarray(X, None, dtype=dtype[0]).dtype.kind != 'c'"
    }]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'all((False for [np.float64, np.float32] in list(X.dtypes)))'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind != 'c'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=dtype[0]).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=dtype[0]).dtype, 'kind')"}, {
    'XXX TODO XXX': "np.asarray(X, None, dtype=dtype[0]).dtype.kind != 'c'"
    }]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind != 'c'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=dtype[0]).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=dtype[0]).dtype, 'kind')"}, {
    'XXX TODO XXX': "np.asarray(X, None, dtype=dtype[0]).dtype.kind != 'c'"
    }]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': "not hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "not hasattr(X.dtypes, '__array__')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX':
    'not all((False for [np.float64, np.float32] in list(X.dtypes)))'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX':
    'np.result_type(*list(X.dtypes)) is None'}, {'XXX TODO XXX':
    'np.result_type(*list(X.dtypes)) not in [np.float64, np.float32]'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'dtype')"}, {
    'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, None).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, None).dtype, 'kind')"},
    {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind != 'c'"}]}, {
    'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'XXX TODO XXX': "not hasattr(np.asarray(X, None, None), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, None).dtype is None'}, {
    'XXX TODO XXX': "not hasattr(np.asarray(X, None, None).dtype, 'kind')"},
    {'XXX TODO XXX': "np.asarray(X, None, None).dtype.kind != 'c'"}]}]}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX':
    'np.result_type(*list(X.dtypes)) is not None'}, {'XXX TODO XXX':
    'np.result_type(*list(X.dtypes)) in [np.float64, np.float32]'}]}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind != 'c'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=dtype[0]).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=dtype[0]).dtype, 'kind')"}, {
    'XXX TODO XXX': "np.asarray(X, None, dtype=dtype[0]).dtype.kind != 'c'"
    }]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'all((False for [np.float64, np.float32] in list(X.dtypes)))'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX':
    "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) not in [np.float64, np.float32]"}, {'allOf':
    [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'dtype')"}, {
    'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, None).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, None).dtype, 'kind')"},
    {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind != 'c'"}]}, {
    'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'XXX TODO XXX': "not hasattr(np.asarray(X, None, None), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, None).dtype is None'}, {
    'XXX TODO XXX': "not hasattr(np.asarray(X, None, None).dtype, 'kind')"},
    {'XXX TODO XXX': "np.asarray(X, None, None).dtype.kind != 'c'"}]}]}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "getattr(X, 'dtype', None) is not None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) in [np.float64, np.float32]"}]}, {'allOf': [
    {'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind != 'c'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=dtype[0]).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=dtype[0]).dtype, 'kind')"}, {
    'XXX TODO XXX': "np.asarray(X, None, dtype=dtype[0]).dtype.kind != 'c'"
    }]}]}]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) not in [np.float64, np.float32]"}, {'allOf':
    [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'dtype')"}, {
    'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, None).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, None).dtype, 'kind')"},
    {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind != 'c'"}]}, {
    'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'XXX TODO XXX': "not hasattr(np.asarray(X, None, None), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, None).dtype is None'}, {
    'XXX TODO XXX': "not hasattr(np.asarray(X, None, None).dtype, 'kind')"},
    {'XXX TODO XXX': "np.asarray(X, None, None).dtype.kind != 'c'"}]}]}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "getattr(X, 'dtype', None) is not None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) in [np.float64, np.float32]"}]}, {'allOf': [
    {'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind != 'c'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=dtype[0]).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=dtype[0]).dtype, 'kind')"}, {
    'XXX TODO XXX': "np.asarray(X, None, dtype=dtype[0]).dtype.kind != 'c'"
    }]}]}]}]}]}]}]}]}]}]}, {'description':
    'From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) '
    , 'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=dtype[0], False, True, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=dtype[0], False, True, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).fit)"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).fit)'
    }]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse='csr', dtype=dtype[0], False, True, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse='csr', dtype=dtype[0], False, True, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).fit)"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'fit')"}, {
    'XXX TODO XXX': 'not callable(np.asarray(X, None, dtype=dtype[0]).fit)'
    }]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) not in [np.float64, np.float32]"}, {'allOf':
    [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object',
    'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', None, False, True, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', None, False, True, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'fit')"}, {
    'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, None).fit)'}]}]}]}, {
    'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse='csr', None, False, True, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse='csr', None, False, True, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, None), 'fit')"}, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, None).fit)'}]}]}]}]}]}, {'anyOf': [{
    'allOf': [{'XXX TODO XXX': "getattr(X, 'dtype', None) is not None"}, {
    'XXX TODO XXX': "getattr(X, 'dtype', None) in [np.float64, np.float32]"
    }]}, {'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=dtype[0], False, True, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=dtype[0], False, True, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).fit)"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).fit)'
    }]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse='csr', dtype=dtype[0], False, True, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse='csr', dtype=dtype[0], False, True, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).fit)"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'fit')"}, {
    'XXX TODO XXX': 'not callable(np.asarray(X, None, dtype=dtype[0]).fit)'
    }]}]}]}]}]}]}]}]}]}]}, {'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Pandas DataFrame with mixed sparse extension arrays generated a sparse matrix with object dtype which can not be converted to a scipy sparse matrix.Sparse extension arrays should all have the same numeric type.'     ) "
    , 'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) not in [np.float64, np.float32]"}, {
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}, {'anyOf': [{
    'allOf': [{'XXX TODO XXX': "getattr(X, 'dtype', None) is not None"}, {
    'XXX TODO XXX': "getattr(X, 'dtype', None) in [np.float64, np.float32]"
    }]}, {'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}]}]}]}, {
    'description':
    'From /utils/validation.py:None:check_array, Exception: raise ValueError("""Complex data not supported {} """.format(array)     ) from complex_warning '
    , 'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}]}, {'anyOf': [{'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}
    ]}, {'XXX TODO XXX': 'sp.issparse(X)'}]}]}, {'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError('Found array with dim %d. %s expected <= 2.' % (array.ndim,     estimator_name)) "
    , 'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).ndim < 3"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).ndim < 3'}]}]}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).ndim < 3"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    'np.asarray(X, None, dtype=dtype[0]).ndim < 3'}]}]}]}]}]}, {'anyOf': [{
    'XXX TODO XXX': "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {
    'allOf': [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) not in [np.float64, np.float32]"}, {'allOf':
    [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, None).ndim < 3'}]}, {'anyOf': [{
    'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {'XXX TODO XXX':
    'np.asarray(X, None, None).ndim < 3'}]}]}]}, {'anyOf': [{'allOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is not None"}, {
    'XXX TODO XXX': "getattr(X, 'dtype', None) in [np.float64, np.float32]"
    }]}, {'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).ndim < 3"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).ndim < 3'}]}]}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).ndim < 3"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    'np.asarray(X, None, dtype=dtype[0]).ndim < 3'}]}]}]}]}]}]}]}]}, {
    'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Found array with %d sample(s) (shape=%s) while a minimum of %d is required%s.'      % (n_samples, array.shape, ensure_min_samples, context)) "
    , 'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=dtype[0], False, True, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0])) >= 1'
    }]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse='csr', dtype=dtype[0], False, True, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "_num_samples(np.asarray(X, None).astype(dtype[0], casting='unsafe', False)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=dtype[0])) >= 1'}]}]}]}]}]}]}]},
    {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) not in [np.float64, np.float32]"}, {'allOf':
    [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object',
    'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', None, False, True, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, None)) >= 1'}]}]}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse='csr', None, False, True, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, None)) >= 1'}]}]}]}]}]}, {'anyOf': [{
    'allOf': [{'XXX TODO XXX': "getattr(X, 'dtype', None) is not None"}, {
    'XXX TODO XXX': "getattr(X, 'dtype', None) in [np.float64, np.float32]"
    }]}, {'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=dtype[0], False, True, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0])) >= 1'
    }]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse='csr', dtype=dtype[0], False, True, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "_num_samples(np.asarray(X, None).astype(dtype[0], casting='unsafe', False)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=dtype[0])) >= 1'}]}]}]}]}]}]}]}
    ]}]}]}, {'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Found array with %d feature(s) (shape=%s) while a minimum of %d is required%s.'      % (n_features, array.shape, ensure_min_features, context)) "
    , 'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=dtype[0], False, True, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'XXX TODO XXX': 'dtype[0] is not None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}, {'anyOf': [{'allOf':
    [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse='csr', dtype=dtype[0], False, True, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'XXX TODO XXX': 'dtype[0] is not None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    'np.asarray(X, None, dtype=dtype[0]).ndim != 2'}, {'XXX TODO XXX':
    'array.shape[1] >= 1'}]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) not in [np.float64, np.float32]"}, {'allOf':
    [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object',
    'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', None, False, True, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, None).ndim != 2'}, {'XXX TODO XXX':
    'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse='csr', None, False, True, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'XXX TODO XXX':
    'np.asarray(X, None, None).ndim != 2'}, {'XXX TODO XXX':
    'array.shape[1] >= 1'}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "getattr(X, 'dtype', None) is not None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) in [np.float64, np.float32]"}]}, {'allOf': [
    {'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object',
    'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=dtype[0], False, True, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'XXX TODO XXX': 'dtype[0] is not None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}, {'anyOf': [{'allOf':
    [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse='csr', dtype=dtype[0], False, True, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'XXX TODO XXX': 'dtype[0] is not None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    'np.asarray(X, None, dtype=dtype[0]).ndim != 2'}, {'XXX TODO XXX':
    'array.shape[1] >= 1'}]}]}]}]}]}]}]}]}]}]}, {'description':
    "From /utils/validation.py:None:check_random_state, Exception: raise ValueError(     '%r cannot be used to seed a numpy.random.RandomState instance' % seed) "
    , 'anyOf': [{'type': 'object', 'properties': {'random_state': {'enum':
    [None]}}}, {'XXX TODO XXX': 'self.random_state is np.random'}, {
    'XXX TODO XXX': 'isinstance(self.random_state, np.random.RandomState)'}
    ]}, {'description':
    "From /utils/__init__.py:None:gen_even_slices, Exception: raise ValueError('gen_even_slices got n_packs=%s, must be >=1' % n_packs) "
    , 'XXX TODO XXX':
    'int(np.ceil(float(X.shape[0]) / self.batch_size)) >= 1'}, {
    'description':
    "From /utils/validation.py:None:check_random_state, Exception: raise ValueError(     '%r cannot be used to seed a numpy.random.RandomState instance' % seed) "
    , 'anyOf': [{'XXX TODO XXX':
    'iteration not in range(1, self.n_iter + 1)'}, {'type': 'object',
    'properties': {'verbose': {'enum': [False]}}}, {'type': 'object',
    'properties': {'random_state': {'enum': [None]}}}, {'XXX TODO XXX':
    'self.random_state is np.random'}, {'XXX TODO XXX':
    'isinstance(self.random_state, np.random.RandomState)'}]}, {
    'description':
    'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) '
    , 'anyOf': [{'XXX TODO XXX':
    'iteration not in range(1, self.n_iter + 1)'}, {'type': 'object',
    'properties': {'verbose': {'enum': [False]}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'type': 'object', 'laleNot': 'X/isSparse'}, {
    'XXX TODO XXX': "not hasattr(X.sparse.to_coo(), 'dtype')"}, {
    'XXX TODO XXX': 'X.sparse.to_coo().dtype is None'}, {'XXX TODO XXX':
    "not hasattr(X.sparse.to_coo().dtype, 'kind')"}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype.kind != 'c'"}]}, {'anyOf': [{'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}
    ]}, {'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(X, 'dtype')"}, {'XXX TODO XXX': 'X.dtype is None'}, {
    'XXX TODO XXX': "not hasattr(X.dtype, 'kind')"}, {'XXX TODO XXX':
    "X.dtype.kind != 'c'"}]}]}]}, {'description':
    'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) '
    , 'anyOf': [{'XXX TODO XXX':
    'iteration not in range(1, self.n_iter + 1)'}, {'type': 'object',
    'properties': {'verbose': {'enum': [False]}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf':
    [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'dtypes')"}, {
    'XXX TODO XXX': "not hasattr(X.dtypes, '__array__')"}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX':
    "not all((False for 'numeric' in list(X.dtypes)))"}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype is None'},
    {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=np.float64), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=np.float64).dtype is None'},
    {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=np.float64).dtype, 'kind')"}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind != 'c'"}]}]}]}, {
    'anyOf': [{'XXX TODO XXX':
    "all((False for 'numeric' in list(X.dtypes)))"}, {'allOf': [{'anyOf': [
    {'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype is None'},
    {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=np.float64), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=np.float64).dtype is None'},
    {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=np.float64).dtype, 'kind')"}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind != 'c'"}]}]}]}]}]}, {
    'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {
    'XXX TODO XXX': "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype is None'},
    {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=np.float64), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=np.float64).dtype is None'},
    {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=np.float64).dtype, 'kind')"}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind != 'c'"}]}]}]}]}]}, {
    'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': "not hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "not hasattr(X.dtypes, '__array__')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not all((False for 'numeric' in list(X.dtypes)))"}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype is None'},
    {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=np.float64), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=np.float64).dtype is None'},
    {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=np.float64).dtype, 'kind')"}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind != 'c'"}]}]}]}, {
    'anyOf': [{'XXX TODO XXX':
    "all((False for 'numeric' in list(X.dtypes)))"}, {'allOf': [{'anyOf': [
    {'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype is None'},
    {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=np.float64), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=np.float64).dtype is None'},
    {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=np.float64).dtype, 'kind')"}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind != 'c'"}]}]}]}]}]}, {
    'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {
    'XXX TODO XXX': "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype is None'},
    {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=np.float64), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=np.float64).dtype is None'},
    {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=np.float64).dtype, 'kind')"}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind != 'c'"}]}]}]}]}]}]}]
    }, {'description':
    'From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) '
    , 'anyOf': [{'XXX TODO XXX':
    'iteration not in range(1, self.n_iter + 1)'}, {'type': 'object',
    'properties': {'verbose': {'enum': [False]}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf':
    [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).fit)'
    }]}, {'anyOf': [{'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).fit)'
    }]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=np.float64).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, dtype=np.float64).astype(np.float64).fit)'
    }]}, {'anyOf': [{'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=np.float64), 'fit')"}, {
    'XXX TODO XXX':
    'not callable(np.asarray(X, None, dtype=np.float64).fit)'}]}]}]}]}]}]}]
    }, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).fit)'
    }]}, {'anyOf': [{'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).fit)'
    }]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=np.float64).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, dtype=np.float64).astype(np.float64).fit)'
    }]}, {'anyOf': [{'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=np.float64), 'fit')"}, {
    'XXX TODO XXX':
    'not callable(np.asarray(X, None, dtype=np.float64).fit)'}]}]}]}]}]}]}]
    }]}]}, {'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Pandas DataFrame with mixed sparse extension arrays generated a sparse matrix with object dtype which can not be converted to a scipy sparse matrix.Sparse extension arrays should all have the same numeric type.'     ) "
    , 'anyOf': [{'XXX TODO XXX':
    'iteration not in range(1, self.n_iter + 1)'}, {'type': 'object',
    'properties': {'verbose': {'enum': [False]}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf':
    [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None).kind != 'O'"}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "getattr(X, 'dtype', None) is not None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None).kind == 'O'"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }]}]}]}]}, {'description':
    'From /utils/validation.py:None:check_array, Exception: raise ValueError("""Complex data not supported {} """.format(array)     ) from complex_warning '
    , 'anyOf': [{'XXX TODO XXX':
    'iteration not in range(1, self.n_iter + 1)'}, {'type': 'object',
    'properties': {'verbose': {'enum': [False]}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}]}, {
    'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}]}]}
    ]}, {'description':
    'From /utils/validation.py:None:check_array, Exception: raise ValueError(     "Unable to convert array of bytes/strings into decimal numbers with dtype=\'numeric\'"     ) from e '
    , 'anyOf': [{'XXX TODO XXX':
    'iteration not in range(1, self.n_iter + 1)'}, {'type': 'object',
    'properties': {'verbose': {'enum': [False]}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf':
    [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'dtypes')"}, {
    'XXX TODO XXX': "not hasattr(X.dtypes, '__array__')"}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX':
    "not all((False for 'numeric' in list(X.dtypes)))"}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}]}]}]},
    {'anyOf': [{'XXX TODO XXX':
    "all((False for 'numeric' in list(X.dtypes)))"}, {'allOf': [{'anyOf': [
    {'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}]}]}]}
    ]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {
    'XXX TODO XXX': "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}]}]}]}
    ]}]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': "not hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "not hasattr(X.dtypes, '__array__')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not all((False for 'numeric' in list(X.dtypes)))"}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}]}]}]},
    {'anyOf': [{'XXX TODO XXX':
    "all((False for 'numeric' in list(X.dtypes)))"}, {'allOf': [{'anyOf': [
    {'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}]}]}]}
    ]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {
    'XXX TODO XXX': "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}]}]}]}
    ]}]}]}]}, {'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError('Found array with dim %d. %s expected <= 2.' % (array.ndim,     estimator_name)) "
    , 'anyOf': [{'XXX TODO XXX':
    'iteration not in range(1, self.n_iter + 1)'}, {'type': 'object',
    'properties': {'verbose': {'enum': [False]}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf':
    [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).ndim < 3'
    }]}, {'anyOf': [{'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=np.float64).ndim < 3'}]}]}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    'np.asarray(X, None, dtype=np.float64).astype(np.float64).ndim < 3'}]},
    {'anyOf': [{'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=np.float64).ndim < 3'}]}]}]}
    ]}]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).ndim < 3'
    }]}, {'anyOf': [{'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=np.float64).ndim < 3'}]}]}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    'np.asarray(X, None, dtype=np.float64).astype(np.float64).ndim < 3'}]},
    {'anyOf': [{'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=np.float64).ndim < 3'}]}]}]}
    ]}]}]}]}, {'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Found array with %d sample(s) (shape=%s) while a minimum of %d is required%s.'      % (n_samples, array.shape, ensure_min_samples, context)) "
    , 'anyOf': [{'XXX TODO XXX':
    'iteration not in range(1, self.n_iter + 1)'}, {'type': 'object',
    'properties': {'verbose': {'enum': [False]}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf':
    [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
    }, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=np.float64)) >= 1'
    }]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=np.float64).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=np.float64)) >= 1'}]}]}]}]}]}]}
    ]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
    }, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=np.float64)) >= 1'
    }]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=np.float64).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=np.float64)) >= 1'}]}]}]}]}]}]}
    ]}]}]}, {'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Found array with %d feature(s) (shape=%s) while a minimum of %d is required%s.'      % (n_features, array.shape, ensure_min_features, context)) "
    , 'anyOf': [{'XXX TODO XXX':
    'iteration not in range(1, self.n_iter + 1)'}, {'type': 'object',
    'properties': {'verbose': {'enum': [False]}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf':
    [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).ndim != 2'
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}, {'anyOf': [{'allOf':
    [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    'np.asarray(X, None, dtype=np.float64).astype(np.float64).ndim != 2'},
    {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}, {'anyOf': [{
    'XXX TODO XXX': "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {
    'allOf': [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse='csr', dtype=np.float64, False, True, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).ndim != 2'
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}, {'anyOf': [{'allOf':
    [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse='csr', dtype=np.float64, False, True, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    'np.asarray(X, None, dtype=np.float64).astype(np.float64).ndim != 2'},
    {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}]}]}, {
    'description':
    "From /utils/validation.py:None:check_is_fitted, Exception: raise TypeError('{} is a class, not an instance.'.format(estimator)) "
    , 'anyOf': [{'XXX TODO XXX':
    'iteration not in range(1, self.n_iter + 1)'}, {'type': 'object',
    'properties': {'verbose': {'enum': [False]}}}, {'XXX TODO XXX':
    'not isclass(self)'}]}, {'description':
    "From /utils/validation.py:None:check_is_fitted, Exception: raise TypeError('%s is not an estimator instance.' % estimator) "
    , 'anyOf': [{'XXX TODO XXX':
    'iteration not in range(1, self.n_iter + 1)'}, {'type': 'object',
    'properties': {'verbose': {'enum': [False]}}}, {'XXX TODO XXX':
    "hasattr(self, 'fit')"}]}]

