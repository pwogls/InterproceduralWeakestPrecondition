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
    "np.asarray(X, None, dtype=np.float64).dtype.kind != 'c'"}]}]}]}]}]}]},
    {'description':
    'From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) '
    , 'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc'], dtype=np.float64, False, True, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc'], dtype=np.float64, False, True, True).fit)"
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
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csc'], dtype=np.float64, False, True, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csc'], dtype=np.float64, False, True, True).fit)"
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
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc'], dtype=np.float64, False, True, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc'], dtype=np.float64, False, True, True).fit)"
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
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csc'], dtype=np.float64, False, True, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csc'], dtype=np.float64, False, True, True).fit)"
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
    }]}, {'description':
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
    }]}]}]}, {'description':
    'From /utils/validation.py:None:check_array, Exception: raise ValueError("""Complex data not supported {} """.format(array)     ) from complex_warning '
    , 'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}]}, {'anyOf': [{'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}
    ]}, {'XXX TODO XXX': 'sp.issparse(X)'}]}]}, {'description':
    'From /utils/validation.py:None:check_array, Exception: raise ValueError(     "Unable to convert array of bytes/strings into decimal numbers with dtype=\'numeric\'"     ) from e '
    , 'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
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
    ]}]}]}, {'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError('Found array with dim %d. %s expected <= 2.' % (array.ndim,     estimator_name)) "
    , 'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
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
    ]}]}]}, {'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Found array with %d sample(s) (shape=%s) while a minimum of %d is required%s.'      % (n_samples, array.shape, ensure_min_samples, context)) "
    , 'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc'], dtype=np.float64, False, True, True)) >= 1"
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
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csc'], dtype=np.float64, False, True, True)) >= 1"
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
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc'], dtype=np.float64, False, True, True)) >= 1"
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
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csc'], dtype=np.float64, False, True, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=np.float64).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=np.float64)) >= 1'}]}]}]}]}]}]}
    ]}]}, {'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Found array with %d feature(s) (shape=%s) while a minimum of %d is required%s.'      % (n_features, array.shape, ensure_min_features, context)) "
    , 'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc'], dtype=np.float64, False, True, True).ndim != 2"
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
    "_ensure_sparse_format(X, accept_sparse=['csc'], dtype=np.float64, False, True, True).ndim != 2"
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
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc'], dtype=np.float64, False, True, True).ndim != 2"
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
    "_ensure_sparse_format(X, accept_sparse=['csc'], dtype=np.float64, False, True, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    'np.asarray(X, None, dtype=np.float64).astype(np.float64).ndim != 2'},
    {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}]}, {'description':
    "From /utils/validation.py:None:check_random_state, Exception: raise ValueError(     '%r cannot be used to seed a numpy.random.RandomState instance' % seed) "
    , 'anyOf': [{'type': 'object', 'properties': {'random_state': {'enum':
    [None]}}}, {'XXX TODO XXX': 'self.random_state is np.random'}, {
    'XXX TODO XXX': 'isinstance(self.random_state, np.random.RandomState)'}
    ]}, {'description':
    "From /utils/validation.py:None:check_random_state, Exception: raise ValueError(     '%r cannot be used to seed a numpy.random.RandomState instance' % seed) "
    , 'anyOf': [{'type': 'object', 'properties': {'random_state': {'enum':
    [None]}}}, {'XXX TODO XXX': 'self.random_state is np.random'}, {
    'XXX TODO XXX': 'isinstance(self.random_state, np.random.RandomState)'}
    ]}, {'description':
    'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) '
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'not': {'enum': [
    None]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(X.sparse.to_coo(), 'dtype')"}, {'XXX TODO XXX':
    'X.sparse.to_coo().dtype is None'}, {'XXX TODO XXX':
    "not hasattr(X.sparse.to_coo().dtype, 'kind')"}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype.kind != 'c'"}]}, {'anyOf': [{'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}
    ]}, {'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(X, 'dtype')"}, {'XXX TODO XXX': 'X.dtype is None'}, {
    'XXX TODO XXX': "not hasattr(X.dtype, 'kind')"}, {'XXX TODO XXX':
    "X.dtype.kind != 'c'"}]}]}]}, {'description':
    'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) '
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'not': {'enum': [
    None]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "not hasattr(X.dtypes, '__array__')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'not all((False for None in list(X.dtypes)))'}, {
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
    {'anyOf': [{'XXX TODO XXX': 'all((False for None in list(X.dtypes)))'},
    {'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
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
    {'XXX TODO XXX': "np.asarray(X, None, None).dtype.kind != 'c'"}]}]}]}]}
    ]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {
    'XXX TODO XXX': "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
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
    {'XXX TODO XXX': "np.asarray(X, None, None).dtype.kind != 'c'"}]}]}]}]}
    ]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': "not hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "not hasattr(X.dtypes, '__array__')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'not all((False for None in list(X.dtypes)))'}, {
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
    {'anyOf': [{'XXX TODO XXX': 'all((False for None in list(X.dtypes)))'},
    {'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
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
    {'XXX TODO XXX': "np.asarray(X, None, None).dtype.kind != 'c'"}]}]}]}]}
    ]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {
    'XXX TODO XXX': "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
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
    {'XXX TODO XXX': "np.asarray(X, None, None).dtype.kind != 'c'"}]}]}]}]}
    ]}]}]}, {'description':
    'From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) '
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'not': {'enum': [
    None]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'fit')"}, {
    'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, None).fit)'}]}]}]}, {
    'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, None), 'fit')"}, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, None).fit)'}]}]}]}]}]}, {'anyOf': [{
    'XXX TODO XXX': "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {
    'allOf': [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'fit')"}, {
    'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, None).fit)'}]}]}]}, {
    'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, None), 'fit')"}, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, None).fit)'}]}]}]}]}]}]}]}, {
    'description':
    'From /utils/validation.py:None:check_array, Exception: raise ValueError("""Complex data not supported {} """.format(array)     ) from complex_warning '
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'not': {'enum': [
    None]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}]}, {'anyOf': [{
    'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}]}]}]}, {
    'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError('Found array with dim %d. %s expected <= 2.' % (array.ndim,     estimator_name)) "
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'not': {'enum': [
    None]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX': 'np.asarray(X.sparse.to_coo(), None, None).ndim < 3'}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'XXX TODO XXX': 'np.asarray(X, None, None).ndim < 3'}]}]}]}, {'anyOf':
    [{'XXX TODO XXX': "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {
    'allOf': [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX': 'np.asarray(X.sparse.to_coo(), None, None).ndim < 3'}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'XXX TODO XXX': 'np.asarray(X, None, None).ndim < 3'}]}]}]}]}]}, {
    'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Found array with %d sample(s) (shape=%s) while a minimum of %d is required%s.'      % (n_samples, array.shape, ensure_min_samples, context)) "
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'not': {'enum': [
    None]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, None)) >= 1'}]}]}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, None)) >= 1'}]}]}]}]}]}, {'anyOf': [{
    'XXX TODO XXX': "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {
    'allOf': [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, None)) >= 1'}]}]}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, None)) >= 1'}]}]}]}]}]}]}]}, {
    'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Found array with %d feature(s) (shape=%s) while a minimum of %d is required%s.'      % (n_features, array.shape, ensure_min_features, context)) "
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'not': {'enum': [
    None]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, None).ndim != 2'}, {'XXX TODO XXX':
    'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'XXX TODO XXX':
    'np.asarray(X, None, None).ndim != 2'}, {'XXX TODO XXX':
    'array.shape[1] >= 1'}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, None).ndim != 2'}, {'XXX TODO XXX':
    'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'XXX TODO XXX':
    'np.asarray(X, None, None).ndim != 2'}, {'XXX TODO XXX':
    'array.shape[1] >= 1'}]}]}]}]}]}]}]}, {'description':
    'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) '
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}}},
    {'type': 'object', 'properties': {'y': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'y': {'not': {'enum': ['no_validation'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(X.sparse.to_coo(), 'dtype')"}, {'XXX TODO XXX':
    'X.sparse.to_coo().dtype is None'}, {'XXX TODO XXX':
    "not hasattr(X.sparse.to_coo().dtype, 'kind')"}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype.kind != 'c'"}]}, {'anyOf': [{'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}
    ]}, {'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(X, 'dtype')"}, {'XXX TODO XXX': 'X.dtype is None'}, {
    'XXX TODO XXX': "not hasattr(X.dtype, 'kind')"}, {'XXX TODO XXX':
    "X.dtype.kind != 'c'"}]}]}]}, {'description':
    'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) '
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}}},
    {'type': 'object', 'properties': {'y': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'y': {'not': {'enum': ['no_validation'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "not hasattr(X.dtypes, '__array__')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'not all((False for None in list(X.dtypes)))'}, {
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
    {'anyOf': [{'XXX TODO XXX': 'all((False for None in list(X.dtypes)))'},
    {'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
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
    {'XXX TODO XXX': "np.asarray(X, None, None).dtype.kind != 'c'"}]}]}]}]}
    ]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {
    'XXX TODO XXX': "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
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
    {'XXX TODO XXX': "np.asarray(X, None, None).dtype.kind != 'c'"}]}]}]}]}
    ]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': "not hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "not hasattr(X.dtypes, '__array__')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'not all((False for None in list(X.dtypes)))'}, {
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
    {'anyOf': [{'XXX TODO XXX': 'all((False for None in list(X.dtypes)))'},
    {'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
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
    {'XXX TODO XXX': "np.asarray(X, None, None).dtype.kind != 'c'"}]}]}]}]}
    ]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {
    'XXX TODO XXX': "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
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
    {'XXX TODO XXX': "np.asarray(X, None, None).dtype.kind != 'c'"}]}]}]}]}
    ]}]}]}, {'description':
    'From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) '
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}}},
    {'type': 'object', 'properties': {'y': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'y': {'not': {'enum': ['no_validation'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'fit')"}, {
    'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, None).fit)'}]}]}]}, {
    'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, None), 'fit')"}, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, None).fit)'}]}]}]}]}]}, {'anyOf': [{
    'XXX TODO XXX': "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {
    'allOf': [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'fit')"}, {
    'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, None).fit)'}]}]}]}, {
    'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, None), 'fit')"}, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, None).fit)'}]}]}]}]}]}]}]}, {
    'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Pandas DataFrame with mixed sparse extension arrays generated a sparse matrix with object dtype which can not be converted to a scipy sparse matrix.Sparse extension arrays should all have the same numeric type.'     ) "
    , 'allOf': [{'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'max_samples': {
    'not': {'type': 'string'}}}}, {'allOf': [{'anyOf': [{'type': 'object',
    'properties': {'max_samples': {'not': {'enum': ['auto']}}}}, {'type':
    'object', 'properties': {'y': {'enum': [None]}}}, {'type': 'object',
    'properties': {'y': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'y': {'not': {'enum': ['no_validation']}}}}, {'allOf': [
    {'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }]}]}, {'anyOf': [{'type': 'object', 'properties': {'max_samples': {
    'enum': ['auto']}}}, {'type': 'object', 'properties': {'y': {'enum': [
    None]}}}, {'type': 'object', 'properties': {'y': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'y': {'not': {'enum': [
    'no_validation']}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }]}]}]}]}, {'anyOf': [{'type': 'object', 'properties': {'max_samples':
    {'type': 'string'}}}, {'allOf': [{'anyOf': [{'type': 'object',
    'properties': {'max_samples': {'not': {'type': 'integer'}}}}, {'allOf':
    [{'anyOf': [{'type': 'object', 'properties': {'max_samples': {
    'laleMaximum': 'X/maxItems'}}}, {'type': 'object', 'properties': {'y':
    {'enum': [None]}}}, {'type': 'object', 'properties': {'y': {'not': {
    'type': 'string'}}}}, {'type': 'object', 'properties': {'y': {'not': {
    'enum': ['no_validation']}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }]}]}, {'anyOf': [{'type': 'object', 'properties': {'max_samples': {
    'laleMinimum': 'X/maxItems'}}}, {'type': 'object', 'properties': {'y':
    {'enum': [None]}}}, {'type': 'object', 'properties': {'y': {'not': {
    'type': 'string'}}}}, {'type': 'object', 'properties': {'y': {'not': {
    'enum': ['no_validation']}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }]}]}]}]}, {'anyOf': [{'type': 'object', 'properties': {'max_samples':
    {'type': 'integer'}}}, {'allOf': [{'anyOf': [{'allOf': [{'type':
    'object', 'properties': {'max_samples': {'type': 'number', 'minimum': 
    0.0, 'exclusiveMinimum': True}}}, {'type': 'object', 'properties': {
    'max_samples': {'type': 'number', 'maximum': 1.0}}}]}, {'type':
    'object', 'properties': {'y': {'enum': [None]}}}, {'type': 'object',
    'properties': {'y': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'y': {'not': {'enum': ['no_validation']}}}}, {'allOf': [
    {'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }]}]}, {'anyOf': [{'type': 'object', 'properties': {'max_samples': {
    'type': 'number', 'maximum': 0.0}}}, {'type': 'object', 'properties': {
    'max_samples': {'type': 'number', 'minimum': 1.0, 'exclusiveMinimum': 
    True}}}, {'type': 'object', 'properties': {'y': {'enum': [None]}}}, {
    'type': 'object', 'properties': {'y': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'y': {'not': {'enum': ['no_validation'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }]}]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX': 'issparse(X)'}, {'allOf':
    [{'anyOf': [{'type': 'object', 'properties': {'max_samples': {'not': {
    'type': 'string'}}}}, {'allOf': [{'anyOf': [{'type': 'object',
    'properties': {'max_samples': {'not': {'enum': ['auto']}}}}, {'type':
    'object', 'properties': {'y': {'enum': [None]}}}, {'type': 'object',
    'properties': {'y': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'y': {'not': {'enum': ['no_validation']}}}}, {'allOf': [
    {'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }]}]}, {'anyOf': [{'type': 'object', 'properties': {'max_samples': {
    'enum': ['auto']}}}, {'type': 'object', 'properties': {'y': {'enum': [
    None]}}}, {'type': 'object', 'properties': {'y': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'y': {'not': {'enum': [
    'no_validation']}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }]}]}]}]}, {'anyOf': [{'type': 'object', 'properties': {'max_samples':
    {'type': 'string'}}}, {'allOf': [{'anyOf': [{'type': 'object',
    'properties': {'max_samples': {'not': {'type': 'integer'}}}}, {'allOf':
    [{'anyOf': [{'type': 'object', 'properties': {'max_samples': {
    'laleMaximum': 'X/maxItems'}}}, {'type': 'object', 'properties': {'y':
    {'enum': [None]}}}, {'type': 'object', 'properties': {'y': {'not': {
    'type': 'string'}}}}, {'type': 'object', 'properties': {'y': {'not': {
    'enum': ['no_validation']}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }]}]}, {'anyOf': [{'type': 'object', 'properties': {'max_samples': {
    'laleMinimum': 'X/maxItems'}}}, {'type': 'object', 'properties': {'y':
    {'enum': [None]}}}, {'type': 'object', 'properties': {'y': {'not': {
    'type': 'string'}}}}, {'type': 'object', 'properties': {'y': {'not': {
    'enum': ['no_validation']}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }]}]}]}]}, {'anyOf': [{'type': 'object', 'properties': {'max_samples':
    {'type': 'integer'}}}, {'allOf': [{'anyOf': [{'allOf': [{'type':
    'object', 'properties': {'max_samples': {'type': 'number', 'minimum': 
    0.0, 'exclusiveMinimum': True}}}, {'type': 'object', 'properties': {
    'max_samples': {'type': 'number', 'maximum': 1.0}}}]}, {'type':
    'object', 'properties': {'y': {'enum': [None]}}}, {'type': 'object',
    'properties': {'y': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'y': {'not': {'enum': ['no_validation']}}}}, {'allOf': [
    {'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }]}]}, {'anyOf': [{'type': 'object', 'properties': {'max_samples': {
    'type': 'number', 'maximum': 0.0}}}, {'type': 'object', 'properties': {
    'max_samples': {'type': 'number', 'minimum': 1.0, 'exclusiveMinimum': 
    True}}}, {'type': 'object', 'properties': {'y': {'enum': [None]}}}, {
    'type': 'object', 'properties': {'y': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'y': {'not': {'enum': ['no_validation'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }]}]}]}]}]}]}]}]}]}, {'description':
    'From /utils/validation.py:None:check_array, Exception: raise ValueError("""Complex data not supported {} """.format(array)     ) from complex_warning '
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}}},
    {'type': 'object', 'properties': {'y': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'y': {'not': {'enum': ['no_validation'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}]}, {'anyOf': [{
    'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}]}]}]}, {
    'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError('Found array with dim %d. %s expected <= 2.' % (array.ndim,     estimator_name)) "
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}}},
    {'type': 'object', 'properties': {'y': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'y': {'not': {'enum': ['no_validation'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX': 'np.asarray(X.sparse.to_coo(), None, None).ndim < 3'}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'XXX TODO XXX': 'np.asarray(X, None, None).ndim < 3'}]}]}]}, {'anyOf':
    [{'XXX TODO XXX': "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {
    'allOf': [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX': 'np.asarray(X.sparse.to_coo(), None, None).ndim < 3'}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'XXX TODO XXX': 'np.asarray(X, None, None).ndim < 3'}]}]}]}]}]}, {
    'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Found array with %d sample(s) (shape=%s) while a minimum of %d is required%s.'      % (n_samples, array.shape, ensure_min_samples, context)) "
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}}},
    {'type': 'object', 'properties': {'y': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'y': {'not': {'enum': ['no_validation'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, None)) >= 1'}]}]}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, None)) >= 1'}]}]}]}]}]}, {'anyOf': [{
    'XXX TODO XXX': "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {
    'allOf': [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, None)) >= 1'}]}]}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, None)) >= 1'}]}]}]}]}]}]}]}, {
    'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Found array with %d feature(s) (shape=%s) while a minimum of %d is required%s.'      % (n_features, array.shape, ensure_min_features, context)) "
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}}},
    {'type': 'object', 'properties': {'y': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'y': {'not': {'enum': ['no_validation'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, None).ndim != 2'}, {'XXX TODO XXX':
    'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'XXX TODO XXX':
    'np.asarray(X, None, None).ndim != 2'}, {'XXX TODO XXX':
    'array.shape[1] >= 1'}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, None).ndim != 2'}, {'XXX TODO XXX':
    'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'XXX TODO XXX':
    'np.asarray(X, None, None).ndim != 2'}, {'XXX TODO XXX':
    'array.shape[1] >= 1'}]}]}]}]}]}]}]}, {'description':
    'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) '
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}}},
    {'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
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
    "X.dtype.kind != 'c'"}]}]}]}, {'description':
    'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) '
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}}},
    {'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "not hasattr(X.dtypes, '__array__')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'not all((False for None in list(X.dtypes)))'}, {
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
    {'anyOf': [{'XXX TODO XXX': 'all((False for None in list(X.dtypes)))'},
    {'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
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
    {'XXX TODO XXX': "np.asarray(X, None, None).dtype.kind != 'c'"}]}]}]}]}
    ]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {
    'XXX TODO XXX': "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
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
    {'XXX TODO XXX': "np.asarray(X, None, None).dtype.kind != 'c'"}]}]}]}]}
    ]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': "not hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "not hasattr(X.dtypes, '__array__')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'not all((False for None in list(X.dtypes)))'}, {
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
    {'anyOf': [{'XXX TODO XXX': 'all((False for None in list(X.dtypes)))'},
    {'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
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
    {'XXX TODO XXX': "np.asarray(X, None, None).dtype.kind != 'c'"}]}]}]}]}
    ]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {
    'XXX TODO XXX': "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
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
    {'XXX TODO XXX': "np.asarray(X, None, None).dtype.kind != 'c'"}]}]}]}]}
    ]}]}]}, {'description':
    'From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) '
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}}},
    {'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'fit')"}, {
    'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, None).fit)'}]}]}]}, {
    'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, None), 'fit')"}, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, None).fit)'}]}]}]}]}]}, {'anyOf': [{
    'XXX TODO XXX': "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {
    'allOf': [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'fit')"}, {
    'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, None).fit)'}]}]}]}, {
    'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, None), 'fit')"}, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, None).fit)'}]}]}]}]}]}]}]}, {
    'description':
    'From /utils/validation.py:None:check_array, Exception: raise ValueError("""Complex data not supported {} """.format(array)     ) from complex_warning '
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}}},
    {'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}]}, {'anyOf': [{'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}
    ]}, {'XXX TODO XXX': 'sp.issparse(X)'}]}]}]}, {'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError('Found array with dim %d. %s expected <= 2.' % (array.ndim,     estimator_name)) "
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}}},
    {'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX': 'np.asarray(X.sparse.to_coo(), None, None).ndim < 3'}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'XXX TODO XXX': 'np.asarray(X, None, None).ndim < 3'}]}]}]}, {'anyOf':
    [{'XXX TODO XXX': "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {
    'allOf': [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX': 'np.asarray(X.sparse.to_coo(), None, None).ndim < 3'}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'XXX TODO XXX': 'np.asarray(X, None, None).ndim < 3'}]}]}]}]}]}, {
    'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Found array with %d sample(s) (shape=%s) while a minimum of %d is required%s.'      % (n_samples, array.shape, ensure_min_samples, context)) "
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}}},
    {'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, None)) >= 1'}]}]}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, None)) >= 1'}]}]}]}]}]}, {'anyOf': [{
    'XXX TODO XXX': "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {
    'allOf': [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, None)) >= 1'}]}]}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, None)) >= 1'}]}]}]}]}]}]}]}, {
    'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Found array with %d feature(s) (shape=%s) while a minimum of %d is required%s.'      % (n_features, array.shape, ensure_min_features, context)) "
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}}},
    {'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, None).ndim != 2'}, {'XXX TODO XXX':
    'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'XXX TODO XXX':
    'np.asarray(X, None, None).ndim != 2'}, {'XXX TODO XXX':
    'array.shape[1] >= 1'}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csr', 'csc'], None, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, None).ndim != 2'}, {'XXX TODO XXX':
    'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse=['csr', 'csc'], None, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'XXX TODO XXX':
    'np.asarray(X, None, None).ndim != 2'}, {'XXX TODO XXX':
    'array.shape[1] >= 1'}]}]}]}]}]}]}]}, {'description':
    'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) '
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}}},
    {'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(y, 'sparse')"}, {
    'XXX TODO XXX': 'y.ndim <= 1'}, {'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(y.sparse.to_coo(), 'dtype')"}, {'XXX TODO XXX':
    'y.sparse.to_coo().dtype is None'}, {'XXX TODO XXX':
    "not hasattr(y.sparse.to_coo().dtype, 'kind')"}, {'XXX TODO XXX':
    "y.sparse.to_coo().dtype.kind != 'c'"}]}, {'anyOf': [{'allOf': [{
    'XXX TODO XXX': "hasattr(y, 'sparse')"}, {'XXX TODO XXX': 'y.ndim > 1'}
    ]}, {'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(y, 'dtype')"}, {'XXX TODO XXX': 'y.dtype is None'}, {
    'XXX TODO XXX': "not hasattr(y.dtype, 'kind')"}, {'XXX TODO XXX':
    "y.dtype.kind != 'c'"}]}]}]}, {'description':
    'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) '
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}}},
    {'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(y, 'dtype', None), 'kind')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(y, 'dtypes')"}, {'XXX TODO XXX':
    "not hasattr(y.dtypes, '__array__')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'not all((False for None in list(y.dtypes)))'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(y, 'sparse')"}, {
    'XXX TODO XXX': 'y.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(y.sparse.to_coo())'}, {'XXX TODO XXX':
    "not hasattr(np.asarray(y.sparse.to_coo(), None, None), 'dtype')"}, {
    'XXX TODO XXX':
    'np.asarray(y.sparse.to_coo(), None, None).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(y.sparse.to_coo(), None, None).dtype, 'kind')"},
    {'XXX TODO XXX':
    "np.asarray(y.sparse.to_coo(), None, None).dtype.kind != 'c'"}]}, {
    'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(y, 'sparse')"}, {
    'XXX TODO XXX': 'y.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(y)'}, {
    'XXX TODO XXX': "not hasattr(np.asarray(y, None, None), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(y, None, None).dtype is None'}, {
    'XXX TODO XXX': "not hasattr(np.asarray(y, None, None).dtype, 'kind')"},
    {'XXX TODO XXX': "np.asarray(y, None, None).dtype.kind != 'c'"}]}]}]},
    {'anyOf': [{'XXX TODO XXX': 'all((False for None in list(y.dtypes)))'},
    {'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(y, 'sparse')"}, {
    'XXX TODO XXX': 'y.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(y.sparse.to_coo())'}, {'XXX TODO XXX':
    "not hasattr(np.asarray(y.sparse.to_coo(), None, None), 'dtype')"}, {
    'XXX TODO XXX':
    'np.asarray(y.sparse.to_coo(), None, None).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(y.sparse.to_coo(), None, None).dtype, 'kind')"},
    {'XXX TODO XXX':
    "np.asarray(y.sparse.to_coo(), None, None).dtype.kind != 'c'"}]}, {
    'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(y, 'sparse')"}, {
    'XXX TODO XXX': 'y.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(y)'}, {
    'XXX TODO XXX': "not hasattr(np.asarray(y, None, None), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(y, None, None).dtype is None'}, {
    'XXX TODO XXX': "not hasattr(np.asarray(y, None, None).dtype, 'kind')"},
    {'XXX TODO XXX': "np.asarray(y, None, None).dtype.kind != 'c'"}]}]}]}]}
    ]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(y, 'dtypes')"}, {
    'XXX TODO XXX': "hasattr(y.dtypes, '__array__')"}]}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "not hasattr(y, 'sparse')"}, {'XXX TODO XXX':
    'y.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(y.sparse.to_coo())'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(y.sparse.to_coo(), None, None), 'dtype')"}, {
    'XXX TODO XXX':
    'np.asarray(y.sparse.to_coo(), None, None).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(y.sparse.to_coo(), None, None).dtype, 'kind')"},
    {'XXX TODO XXX':
    "np.asarray(y.sparse.to_coo(), None, None).dtype.kind != 'c'"}]}, {
    'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(y, 'sparse')"}, {
    'XXX TODO XXX': 'y.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(y)'}, {
    'XXX TODO XXX': "not hasattr(np.asarray(y, None, None), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(y, None, None).dtype is None'}, {
    'XXX TODO XXX': "not hasattr(np.asarray(y, None, None).dtype, 'kind')"},
    {'XXX TODO XXX': "np.asarray(y, None, None).dtype.kind != 'c'"}]}]}]}]}
    ]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(y, 'dtype', None), 'kind')"}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': "not hasattr(y, 'dtypes')"}, {'XXX TODO XXX':
    "not hasattr(y.dtypes, '__array__')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'not all((False for None in list(y.dtypes)))'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(y, 'sparse')"}, {
    'XXX TODO XXX': 'y.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(y.sparse.to_coo())'}, {'XXX TODO XXX':
    "not hasattr(np.asarray(y.sparse.to_coo(), None, None), 'dtype')"}, {
    'XXX TODO XXX':
    'np.asarray(y.sparse.to_coo(), None, None).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(y.sparse.to_coo(), None, None).dtype, 'kind')"},
    {'XXX TODO XXX':
    "np.asarray(y.sparse.to_coo(), None, None).dtype.kind != 'c'"}]}, {
    'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(y, 'sparse')"}, {
    'XXX TODO XXX': 'y.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(y)'}, {
    'XXX TODO XXX': "not hasattr(np.asarray(y, None, None), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(y, None, None).dtype is None'}, {
    'XXX TODO XXX': "not hasattr(np.asarray(y, None, None).dtype, 'kind')"},
    {'XXX TODO XXX': "np.asarray(y, None, None).dtype.kind != 'c'"}]}]}]},
    {'anyOf': [{'XXX TODO XXX': 'all((False for None in list(y.dtypes)))'},
    {'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(y, 'sparse')"}, {
    'XXX TODO XXX': 'y.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(y.sparse.to_coo())'}, {'XXX TODO XXX':
    "not hasattr(np.asarray(y.sparse.to_coo(), None, None), 'dtype')"}, {
    'XXX TODO XXX':
    'np.asarray(y.sparse.to_coo(), None, None).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(y.sparse.to_coo(), None, None).dtype, 'kind')"},
    {'XXX TODO XXX':
    "np.asarray(y.sparse.to_coo(), None, None).dtype.kind != 'c'"}]}, {
    'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(y, 'sparse')"}, {
    'XXX TODO XXX': 'y.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(y)'}, {
    'XXX TODO XXX': "not hasattr(np.asarray(y, None, None), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(y, None, None).dtype is None'}, {
    'XXX TODO XXX': "not hasattr(np.asarray(y, None, None).dtype, 'kind')"},
    {'XXX TODO XXX': "np.asarray(y, None, None).dtype.kind != 'c'"}]}]}]}]}
    ]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(y, 'dtypes')"}, {
    'XXX TODO XXX': "hasattr(y.dtypes, '__array__')"}]}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "not hasattr(y, 'sparse')"}, {'XXX TODO XXX':
    'y.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(y.sparse.to_coo())'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(y.sparse.to_coo(), None, None), 'dtype')"}, {
    'XXX TODO XXX':
    'np.asarray(y.sparse.to_coo(), None, None).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(y.sparse.to_coo(), None, None).dtype, 'kind')"},
    {'XXX TODO XXX':
    "np.asarray(y.sparse.to_coo(), None, None).dtype.kind != 'c'"}]}, {
    'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(y, 'sparse')"}, {
    'XXX TODO XXX': 'y.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(y)'}, {
    'XXX TODO XXX': "not hasattr(np.asarray(y, None, None), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(y, None, None).dtype is None'}, {
    'XXX TODO XXX': "not hasattr(np.asarray(y, None, None).dtype, 'kind')"},
    {'XXX TODO XXX': "np.asarray(y, None, None).dtype.kind != 'c'"}]}]}]}]}
    ]}]}]}, {'description':
    'From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) '
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}}},
    {'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(y, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(y, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(y.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(y, 'sparse')"}, {'XXX TODO XXX':
    'y.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(y.sparse.to_coo(), accept_sparse='csr', None, False, True, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(y.sparse.to_coo(), accept_sparse='csr', None, False, True, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(y.sparse.to_coo())'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(y.sparse.to_coo(), None, None), 'fit')"}, {
    'XXX TODO XXX':
    'not callable(np.asarray(y.sparse.to_coo(), None, None).fit)'}]}]}]}, {
    'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(y, 'sparse')"}, {
    'XXX TODO XXX': 'y.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(y, accept_sparse='csr', None, False, True, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(y, accept_sparse='csr', None, False, True, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(y)'}, {'XXX TODO XXX':
    "not hasattr(np.asarray(y, None, None), 'fit')"}, {'XXX TODO XXX':
    'not callable(np.asarray(y, None, None).fit)'}]}]}]}]}]}, {'anyOf': [{
    'XXX TODO XXX': "not hasattr(getattr(y, 'dtype', None), 'kind')"}, {
    'allOf': [{'XXX TODO XXX': "hasattr(y, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(y.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(y, 'sparse')"}, {'XXX TODO XXX':
    'y.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(y.sparse.to_coo(), accept_sparse='csr', None, False, True, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(y.sparse.to_coo(), accept_sparse='csr', None, False, True, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(y.sparse.to_coo())'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(y.sparse.to_coo(), None, None), 'fit')"}, {
    'XXX TODO XXX':
    'not callable(np.asarray(y.sparse.to_coo(), None, None).fit)'}]}]}]}, {
    'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(y, 'sparse')"}, {
    'XXX TODO XXX': 'y.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(y, accept_sparse='csr', None, False, True, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(y, accept_sparse='csr', None, False, True, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(y)'}, {'XXX TODO XXX':
    "not hasattr(np.asarray(y, None, None), 'fit')"}, {'XXX TODO XXX':
    'not callable(np.asarray(y, None, None).fit)'}]}]}]}]}]}]}]}, {
    'description':
    'From /utils/validation.py:None:check_array, Exception: raise ValueError("""Complex data not supported {} """.format(array)     ) from complex_warning '
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}}},
    {'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(y, 'sparse')"}, {
    'XXX TODO XXX': 'y.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(y.sparse.to_coo())'}]}, {'anyOf': [{'allOf': [{
    'XXX TODO XXX': "hasattr(y, 'sparse')"}, {'XXX TODO XXX': 'y.ndim > 1'}
    ]}, {'XXX TODO XXX': 'sp.issparse(y)'}]}]}]}, {'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError('Found array with dim %d. %s expected <= 2.' % (array.ndim,     estimator_name)) "
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}}},
    {'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(y, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(y, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(y.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(y, 'sparse')"}, {'XXX TODO XXX':
    'y.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(y.sparse.to_coo())'}, {
    'XXX TODO XXX': 'np.asarray(y.sparse.to_coo(), None, None).ndim < 3'}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(y, 'sparse')"}, {
    'XXX TODO XXX': 'y.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(y)'}, {
    'XXX TODO XXX': 'np.asarray(y, None, None).ndim < 3'}]}]}]}, {'anyOf':
    [{'XXX TODO XXX': "not hasattr(getattr(y, 'dtype', None), 'kind')"}, {
    'allOf': [{'XXX TODO XXX': "hasattr(y, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(y.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(y, 'sparse')"}, {'XXX TODO XXX':
    'y.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(y.sparse.to_coo())'}, {
    'XXX TODO XXX': 'np.asarray(y.sparse.to_coo(), None, None).ndim < 3'}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(y, 'sparse')"}, {
    'XXX TODO XXX': 'y.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(y)'}, {
    'XXX TODO XXX': 'np.asarray(y, None, None).ndim < 3'}]}]}]}]}]}, {
    'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Found array with %d sample(s) (shape=%s) while a minimum of %d is required%s.'      % (n_samples, array.shape, ensure_min_samples, context)) "
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}}},
    {'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(y, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(y, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(y.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(y, 'sparse')"}, {'XXX TODO XXX':
    'y.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(y.sparse.to_coo(), accept_sparse='csr', None, False, True, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(y.sparse.to_coo())'}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(y.sparse.to_coo(), None, None)) >= 1'}]}]}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(y, 'sparse')"}, {
    'XXX TODO XXX': 'y.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(y, accept_sparse='csr', None, False, True, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(y)'}, {'XXX TODO XXX':
    '_num_samples(np.asarray(y, None, None)) >= 1'}]}]}]}]}]}, {'anyOf': [{
    'XXX TODO XXX': "not hasattr(getattr(y, 'dtype', None), 'kind')"}, {
    'allOf': [{'XXX TODO XXX': "hasattr(y, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(y.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(y, 'sparse')"}, {'XXX TODO XXX':
    'y.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(y.sparse.to_coo(), accept_sparse='csr', None, False, True, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(y.sparse.to_coo())'}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(y.sparse.to_coo(), None, None)) >= 1'}]}]}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(y, 'sparse')"}, {
    'XXX TODO XXX': 'y.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(y, accept_sparse='csr', None, False, True, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(y)'}, {'XXX TODO XXX':
    '_num_samples(np.asarray(y, None, None)) >= 1'}]}]}]}]}]}]}]}, {
    'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Found array with %d feature(s) (shape=%s) while a minimum of %d is required%s.'      % (n_features, array.shape, ensure_min_features, context)) "
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}}},
    {'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(y, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(y, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(y.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(y, 'sparse')"}, {'XXX TODO XXX':
    'y.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(y.sparse.to_coo(), accept_sparse='csr', None, False, True, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(y.sparse.to_coo())'}, {'XXX TODO XXX':
    'np.asarray(y.sparse.to_coo(), None, None).ndim != 2'}, {'XXX TODO XXX':
    'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(y, 'sparse')"}, {'XXX TODO XXX': 'y.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(y, accept_sparse='csr', None, False, True, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(y)'}, {'XXX TODO XXX':
    'np.asarray(y, None, None).ndim != 2'}, {'XXX TODO XXX':
    'array.shape[1] >= 1'}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(y, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(y, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(y.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(y, 'sparse')"}, {'XXX TODO XXX':
    'y.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(y.sparse.to_coo(), accept_sparse='csr', None, False, True, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(y.sparse.to_coo())'}, {'XXX TODO XXX':
    'np.asarray(y.sparse.to_coo(), None, None).ndim != 2'}, {'XXX TODO XXX':
    'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(y, 'sparse')"}, {'XXX TODO XXX': 'y.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(y, accept_sparse='csr', None, False, True, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(y)'}, {'XXX TODO XXX':
    'np.asarray(y, None, None).ndim != 2'}, {'XXX TODO XXX':
    'array.shape[1] >= 1'}]}]}]}]}]}]}]}, {'description':
    'From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) '
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}}},
    {'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'XXX TODO XXX': "not hasattr(X, 'fit')"}, {'XXX TODO XXX':
    'not callable(X.fit)'}]}, {'description':
    'From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) '
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}}},
    {'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'XXX TODO XXX': "hasattr(X, '__len__')"}, {'XXX TODO XXX':
    "hasattr(X, 'shape')"}, {'XXX TODO XXX': "hasattr(X, '__array__')"}]},
    {'description':
    "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(     'Singleton array %r cannot be considered a valid collection.' % x) "
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}}},
    {'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'allOf': [{'anyOf': [{'XXX TODO XXX': "hasattr(X, '__len__')"}, {
    'XXX TODO XXX': "hasattr(X, 'shape')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, '__array__')"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X), 'shape')"}, {'XXX TODO XXX':
    'np.asarray(X).shape is None'}, {'XXX TODO XXX':
    'len(np.asarray(X).shape) != 0'}]}, {'anyOf': [{'XXX TODO XXX':
    "hasattr(X, '__array__')"}, {'XXX TODO XXX': "not hasattr(X, 'shape')"},
    {'XXX TODO XXX': 'X.shape is None'}, {'XXX TODO XXX':
    'len(X.shape) != 0'}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "not hasattr(X, '__len__')"}, {'XXX TODO XXX':
    "not hasattr(X, 'shape')"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'shape')"}, {'XXX TODO XXX': 'X.shape is None'}, {
    'XXX TODO XXX': 'len(X.shape) != 0'}]}]}]}, {'description':
    'From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) from type_error '
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}}},
    {'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'allOf': [{'anyOf': [{'XXX TODO XXX': "hasattr(X, '__len__')"}, {
    'XXX TODO XXX': "hasattr(X, 'shape')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, '__array__')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(np.asarray(X), 'shape')"}, {'XXX TODO XXX':
    'np.asarray(X).shape is not None'}]}]}, {'anyOf': [{'XXX TODO XXX':
    "hasattr(X, '__array__')"}, {'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'shape')"}, {'XXX TODO XXX': 'X.shape is not None'}]}]}]}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "not hasattr(X, '__len__')"}, {
    'XXX TODO XXX': "not hasattr(X, 'shape')"}]}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'shape')"}, {'XXX TODO XXX':
    'X.shape is not None'}]}]}, {'XXX TODO XXX':
    'isinstance(x.shape[0], numbers.Integral)'}]}]}, {'description':
    "From /utils/validation.py:None:check_consistent_length, Exception: raise ValueError(     'Found input variables with inconsistent numbers of samples: %r' % [int     (l) for l in lengths]) "
    , 'allOf': [{'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'max_samples': {
    'not': {'type': 'string'}}}}, {'allOf': [{'anyOf': [{'type': 'object',
    'properties': {'max_samples': {'not': {'enum': ['auto']}}}}, {'type':
    'object', 'properties': {'y': {'enum': [None]}}}, {'allOf': [{'type':
    'object', 'properties': {'y': {'type': 'string'}}}, {'type': 'object',
    'properties': {'y': {'enum': ['no_validation']}}}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'y': {'not': {'enum': [None
    ]}}}}, {'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }]}, {'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}
    }}, {'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }]}]}]}, {'anyOf': [{'type': 'object', 'properties': {'max_samples': {
    'enum': ['auto']}}}, {'type': 'object', 'properties': {'y': {'enum': [
    None]}}}, {'allOf': [{'type': 'object', 'properties': {'y': {'type':
    'string'}}}, {'type': 'object', 'properties': {'y': {'enum': [
    'no_validation']}}}]}, {'allOf': [{'anyOf': [{'type': 'object',
    'properties': {'y': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }]}, {'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}
    }}, {'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }]}]}]}]}]}, {'anyOf': [{'type': 'object', 'properties': {'max_samples':
    {'type': 'string'}}}, {'allOf': [{'anyOf': [{'type': 'object',
    'properties': {'max_samples': {'not': {'type': 'integer'}}}}, {'allOf':
    [{'anyOf': [{'type': 'object', 'properties': {'max_samples': {
    'laleMaximum': 'X/maxItems'}}}, {'type': 'object', 'properties': {'y':
    {'enum': [None]}}}, {'allOf': [{'type': 'object', 'properties': {'y': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'y': {'enum': [
    'no_validation']}}}]}, {'allOf': [{'anyOf': [{'type': 'object',
    'properties': {'y': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }]}, {'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}
    }}, {'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }]}]}]}, {'anyOf': [{'type': 'object', 'properties': {'max_samples': {
    'laleMinimum': 'X/maxItems'}}}, {'type': 'object', 'properties': {'y':
    {'enum': [None]}}}, {'allOf': [{'type': 'object', 'properties': {'y': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'y': {'enum': [
    'no_validation']}}}]}, {'allOf': [{'anyOf': [{'type': 'object',
    'properties': {'y': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }]}, {'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}
    }}, {'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }]}]}]}]}]}, {'anyOf': [{'type': 'object', 'properties': {'max_samples':
    {'type': 'integer'}}}, {'allOf': [{'anyOf': [{'allOf': [{'type':
    'object', 'properties': {'max_samples': {'type': 'number', 'minimum': 
    0.0, 'exclusiveMinimum': True}}}, {'type': 'object', 'properties': {
    'max_samples': {'type': 'number', 'maximum': 1.0}}}]}, {'type':
    'object', 'properties': {'y': {'enum': [None]}}}, {'allOf': [{'type':
    'object', 'properties': {'y': {'type': 'string'}}}, {'type': 'object',
    'properties': {'y': {'enum': ['no_validation']}}}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'y': {'not': {'enum': [None
    ]}}}}, {'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }]}, {'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}
    }}, {'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }]}]}]}, {'anyOf': [{'type': 'object', 'properties': {'max_samples': {
    'type': 'number', 'maximum': 0.0}}}, {'type': 'object', 'properties': {
    'max_samples': {'type': 'number', 'minimum': 1.0, 'exclusiveMinimum': 
    True}}}, {'type': 'object', 'properties': {'y': {'enum': [None]}}}, {
    'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'y': {'not': {
    'enum': [None]}}}}, {'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }]}, {'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}
    }}, {'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }]}]}]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX': 'issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'max_samples': {
    'not': {'type': 'string'}}}}, {'allOf': [{'anyOf': [{'type': 'object',
    'properties': {'max_samples': {'not': {'enum': ['auto']}}}}, {'type':
    'object', 'properties': {'y': {'enum': [None]}}}, {'allOf': [{'type':
    'object', 'properties': {'y': {'type': 'string'}}}, {'type': 'object',
    'properties': {'y': {'enum': ['no_validation']}}}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'y': {'not': {'enum': [None
    ]}}}}, {'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }]}, {'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}
    }}, {'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }]}]}]}, {'anyOf': [{'type': 'object', 'properties': {'max_samples': {
    'enum': ['auto']}}}, {'type': 'object', 'properties': {'y': {'enum': [
    None]}}}, {'allOf': [{'type': 'object', 'properties': {'y': {'type':
    'string'}}}, {'type': 'object', 'properties': {'y': {'enum': [
    'no_validation']}}}]}, {'allOf': [{'anyOf': [{'type': 'object',
    'properties': {'y': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }]}, {'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}
    }}, {'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }]}]}]}]}]}, {'anyOf': [{'type': 'object', 'properties': {'max_samples':
    {'type': 'string'}}}, {'allOf': [{'anyOf': [{'type': 'object',
    'properties': {'max_samples': {'not': {'type': 'integer'}}}}, {'allOf':
    [{'anyOf': [{'type': 'object', 'properties': {'max_samples': {
    'laleMaximum': 'X/maxItems'}}}, {'type': 'object', 'properties': {'y':
    {'enum': [None]}}}, {'allOf': [{'type': 'object', 'properties': {'y': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'y': {'enum': [
    'no_validation']}}}]}, {'allOf': [{'anyOf': [{'type': 'object',
    'properties': {'y': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }]}, {'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}
    }}, {'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }]}]}]}, {'anyOf': [{'type': 'object', 'properties': {'max_samples': {
    'laleMinimum': 'X/maxItems'}}}, {'type': 'object', 'properties': {'y':
    {'enum': [None]}}}, {'allOf': [{'type': 'object', 'properties': {'y': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'y': {'enum': [
    'no_validation']}}}]}, {'allOf': [{'anyOf': [{'type': 'object',
    'properties': {'y': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }]}, {'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}
    }}, {'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }]}]}]}]}]}, {'anyOf': [{'type': 'object', 'properties': {'max_samples':
    {'type': 'integer'}}}, {'allOf': [{'anyOf': [{'allOf': [{'type':
    'object', 'properties': {'max_samples': {'type': 'number', 'minimum': 
    0.0, 'exclusiveMinimum': True}}}, {'type': 'object', 'properties': {
    'max_samples': {'type': 'number', 'maximum': 1.0}}}]}, {'type':
    'object', 'properties': {'y': {'enum': [None]}}}, {'allOf': [{'type':
    'object', 'properties': {'y': {'type': 'string'}}}, {'type': 'object',
    'properties': {'y': {'enum': ['no_validation']}}}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'y': {'not': {'enum': [None
    ]}}}}, {'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }]}, {'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}
    }}, {'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }]}]}]}, {'anyOf': [{'type': 'object', 'properties': {'max_samples': {
    'type': 'number', 'maximum': 0.0}}}, {'type': 'object', 'properties': {
    'max_samples': {'type': 'number', 'minimum': 1.0, 'exclusiveMinimum': 
    True}}}, {'type': 'object', 'properties': {'y': {'enum': [None]}}}, {
    'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'y': {'not': {
    'enum': [None]}}}}, {'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }]}, {'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}
    }}, {'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }]}]}]}]}]}]}]}]}]}]}, {'description':
    "From /utils/validation.py:None:check_X_y, Exception: raise ValueError('y cannot be None') "
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}}},
    {'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'type': 'object', 'properties': {'y': {'not': {'enum': [None]}}}}]}, {
    'description':
    "From /base.py:BaseEstimator:_validate_data, Exception: raise ValueError(     f'This {self.__class__.__name__} estimator requires y to be passed, but the target y is None.'     ) "
    , 'anyOf': [{'type': 'object', 'properties': {'y': {'not': {'enum': [
    None]}}}}, {'XXX TODO XXX': "not self._get_tags()['requires_y']"}]}, {
    'description':
    'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) '
    , 'anyOf': [{'type': 'object', 'properties': {'sample_weight': {'enum':
    [None]}}}, {'type': 'object', 'properties': {'sample_weight': {'enum':
    [None]}}}, {'type': 'object', 'properties': {'sample_weight': {'type':
    'number'}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(sample_weight, 'sparse')"}, {'XXX TODO XXX':
    'sample_weight.ndim <= 1'}, {'type': 'object', 'laleNot': 'X/isSparse'},
    {'XXX TODO XXX': "not hasattr(sample_weight.sparse.to_coo(), 'dtype')"},
    {'XXX TODO XXX': 'sample_weight.sparse.to_coo().dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(sample_weight.sparse.to_coo().dtype, 'kind')"}, {
    'XXX TODO XXX': "sample_weight.sparse.to_coo().dtype.kind != 'c'"}]}, {
    'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(sample_weight, 'sparse')"}, {'XXX TODO XXX':
    'sample_weight.ndim > 1'}]}, {'type': 'object', 'laleNot': 'X/isSparse'
    }, {'XXX TODO XXX': "not hasattr(sample_weight, 'dtype')"}, {
    'XXX TODO XXX': 'sample_weight.dtype is None'}, {'XXX TODO XXX':
    "not hasattr(sample_weight.dtype, 'kind')"}, {'XXX TODO XXX':
    "sample_weight.dtype.kind != 'c'"}]}]}]}, {'description':
    "From /utils/validation.py:None:_ensure_sparse_format, Exception: raise TypeError(     'A sparse matrix was passed, but dense data is required. Use X.toarray() to convert to a dense numpy array.'     ) "
    , 'anyOf': [{'type': 'object', 'properties': {'sample_weight': {'enum':
    [None]}}}, {'type': 'object', 'properties': {'sample_weight': {'enum':
    [None]}}}, {'type': 'object', 'properties': {'sample_weight': {'type':
    'number'}}}, {'type': 'object', 'laleNot': 'X/isSparse'}]}, {
    'description':
    'From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) '
    , 'anyOf': [{'type': 'object', 'properties': {'sample_weight': {'enum':
    [None]}}}, {'type': 'object', 'properties': {'sample_weight': {'enum':
    [None]}}}, {'type': 'object', 'properties': {'sample_weight': {'type':
    'number'}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(sample_weight, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(sample_weight, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(sample_weight.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [
    {'XXX TODO XXX': "not hasattr(sample_weight, 'sparse')"}, {
    'XXX TODO XXX': 'sample_weight.ndim <= 1'}, {'allOf': [{'anyOf': [{
    'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(sample_weight.sparse.to_coo(), False, dtype=dtype[0], False, True, True), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(_ensure_sparse_format(sample_weight.sparse.to_coo(), False, dtype=dtype[0], False, True, True).fit)'
    }]}, {'anyOf': [{'XXX TODO XXX':
    'sp.issparse(sample_weight.sparse.to_coo())'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(sample_weight.sparse.to_coo(), order='C').astype(dtype[0], casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(sample_weight.sparse.to_coo(), order='C').astype(dtype[0], casting='unsafe', False).fit)"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(sample_weight.sparse.to_coo(), order='C', dtype=dtype[0]), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(sample_weight.sparse.to_coo(), order='C', dtype=dtype[0]).fit)"
    }]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(sample_weight, 'sparse')"}, {'XXX TODO XXX':
    'sample_weight.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object',
    'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(sample_weight, False, dtype=dtype[0], False, True, True), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(_ensure_sparse_format(sample_weight, False, dtype=dtype[0], False, True, True).fit)'
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(sample_weight)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(sample_weight, order='C').astype(dtype[0], casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(sample_weight, order='C').astype(dtype[0], casting='unsafe', False).fit)"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(sample_weight, order='C', dtype=dtype[0]), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(sample_weight, order='C', dtype=dtype[0]).fit)"
    }]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(sample_weight, 'dtype', None), 'kind')"}, {'allOf':
    [{'XXX TODO XXX': "hasattr(sample_weight, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(sample_weight.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [
    {'XXX TODO XXX': "getattr(sample_weight, 'dtype', None) is None"}, {
    'XXX TODO XXX':
    "getattr(sample_weight, 'dtype', None) not in [np.float64, np.float32]"
    }, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(sample_weight, 'sparse')"}, {'XXX TODO XXX':
    'sample_weight.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object',
    'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(sample_weight.sparse.to_coo(), False, None, False, True, True), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(_ensure_sparse_format(sample_weight.sparse.to_coo(), False, None, False, True, True).fit)'
    }]}, {'anyOf': [{'XXX TODO XXX':
    'sp.issparse(sample_weight.sparse.to_coo())'}, {'XXX TODO XXX':
    "not hasattr(np.asarray(sample_weight.sparse.to_coo(), order='C', None), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(sample_weight.sparse.to_coo(), order='C', None).fit)"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(sample_weight, 'sparse')"}, {'XXX TODO XXX':
    'sample_weight.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object',
    'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(sample_weight, False, None, False, True, True), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(_ensure_sparse_format(sample_weight, False, None, False, True, True).fit)'
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(sample_weight)'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(sample_weight, order='C', None), 'fit')"}, {
    'XXX TODO XXX':
    "not callable(np.asarray(sample_weight, order='C', None).fit)"}]}]}]}]}
    ]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "getattr(sample_weight, 'dtype', None) is not None"}, {'XXX TODO XXX':
    "getattr(sample_weight, 'dtype', None) in [np.float64, np.float32]"}]},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(sample_weight, 'sparse')"}, {'XXX TODO XXX':
    'sample_weight.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object',
    'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(sample_weight.sparse.to_coo(), False, dtype=dtype[0], False, True, True), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(_ensure_sparse_format(sample_weight.sparse.to_coo(), False, dtype=dtype[0], False, True, True).fit)'
    }]}, {'anyOf': [{'XXX TODO XXX':
    'sp.issparse(sample_weight.sparse.to_coo())'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(sample_weight.sparse.to_coo(), order='C').astype(dtype[0], casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(sample_weight.sparse.to_coo(), order='C').astype(dtype[0], casting='unsafe', False).fit)"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(sample_weight.sparse.to_coo(), order='C', dtype=dtype[0]), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(sample_weight.sparse.to_coo(), order='C', dtype=dtype[0]).fit)"
    }]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(sample_weight, 'sparse')"}, {'XXX TODO XXX':
    'sample_weight.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object',
    'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(sample_weight, False, dtype=dtype[0], False, True, True), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(_ensure_sparse_format(sample_weight, False, dtype=dtype[0], False, True, True).fit)'
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(sample_weight)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(sample_weight, order='C').astype(dtype[0], casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(sample_weight, order='C').astype(dtype[0], casting='unsafe', False).fit)"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(sample_weight, order='C', dtype=dtype[0]), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(sample_weight, order='C', dtype=dtype[0]).fit)"
    }]}]}]}]}]}]}]}]}]}]}]}, {'description':
    'From /utils/validation.py:None:check_array, Exception: raise ValueError("""Complex data not supported {} """.format(array)     ) from complex_warning '
    , 'anyOf': [{'type': 'object', 'properties': {'sample_weight': {'enum':
    [None]}}}, {'type': 'object', 'properties': {'sample_weight': {'enum':
    [None]}}}, {'type': 'object', 'properties': {'sample_weight': {'type':
    'number'}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(sample_weight, 'sparse')"}, {'XXX TODO XXX':
    'sample_weight.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(sample_weight.sparse.to_coo())'}]}, {'anyOf': [{'allOf': [
    {'XXX TODO XXX': "hasattr(sample_weight, 'sparse')"}, {'XXX TODO XXX':
    'sample_weight.ndim > 1'}]}, {'XXX TODO XXX':
    'sp.issparse(sample_weight)'}]}]}]}, {'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError('Found array with dim %d. %s expected <= 2.' % (array.ndim,     estimator_name)) "
    , 'anyOf': [{'type': 'object', 'properties': {'sample_weight': {'enum':
    [None]}}}, {'type': 'object', 'properties': {'sample_weight': {'enum':
    [None]}}}, {'type': 'object', 'properties': {'sample_weight': {'type':
    'number'}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(sample_weight, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(sample_weight, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(sample_weight.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [
    {'XXX TODO XXX': "not hasattr(sample_weight, 'sparse')"}, {
    'XXX TODO XXX': 'sample_weight.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(sample_weight.sparse.to_coo())'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "np.asarray(sample_weight.sparse.to_coo(), order='C').astype(dtype[0], casting='unsafe', False).ndim < 3"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    "np.asarray(sample_weight.sparse.to_coo(), order='C', dtype=dtype[0]).ndim < 3"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(sample_weight, 'sparse')"}, {'XXX TODO XXX':
    'sample_weight.ndim > 1'}]}, {'XXX TODO XXX':
    'sp.issparse(sample_weight)'}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "np.asarray(sample_weight, order='C').astype(dtype[0], casting='unsafe', False).ndim < 3"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    "np.asarray(sample_weight, order='C', dtype=dtype[0]).ndim < 3"}]}]}]}]
    }]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(sample_weight, 'dtype', None), 'kind')"}, {'allOf':
    [{'XXX TODO XXX': "hasattr(sample_weight, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(sample_weight.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [
    {'XXX TODO XXX': "getattr(sample_weight, 'dtype', None) is None"}, {
    'XXX TODO XXX':
    "getattr(sample_weight, 'dtype', None) not in [np.float64, np.float32]"
    }, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(sample_weight, 'sparse')"}, {'XXX TODO XXX':
    'sample_weight.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(sample_weight.sparse.to_coo())'}, {'XXX TODO XXX':
    "np.asarray(sample_weight.sparse.to_coo(), order='C', None).ndim < 3"}]
    }, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(sample_weight, 'sparse')"}, {'XXX TODO XXX':
    'sample_weight.ndim > 1'}]}, {'XXX TODO XXX':
    'sp.issparse(sample_weight)'}, {'XXX TODO XXX':
    "np.asarray(sample_weight, order='C', None).ndim < 3"}]}]}]}, {'anyOf':
    [{'allOf': [{'XXX TODO XXX':
    "getattr(sample_weight, 'dtype', None) is not None"}, {'XXX TODO XXX':
    "getattr(sample_weight, 'dtype', None) in [np.float64, np.float32]"}]},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(sample_weight, 'sparse')"}, {'XXX TODO XXX':
    'sample_weight.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(sample_weight.sparse.to_coo())'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "np.asarray(sample_weight.sparse.to_coo(), order='C').astype(dtype[0], casting='unsafe', False).ndim < 3"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    "np.asarray(sample_weight.sparse.to_coo(), order='C', dtype=dtype[0]).ndim < 3"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(sample_weight, 'sparse')"}, {'XXX TODO XXX':
    'sample_weight.ndim > 1'}]}, {'XXX TODO XXX':
    'sp.issparse(sample_weight)'}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "np.asarray(sample_weight, order='C').astype(dtype[0], casting='unsafe', False).ndim < 3"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    "np.asarray(sample_weight, order='C', dtype=dtype[0]).ndim < 3"}]}]}]}]
    }]}]}]}]}]}, {'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Found array with %d sample(s) (shape=%s) while a minimum of %d is required%s.'      % (n_samples, array.shape, ensure_min_samples, context)) "
    , 'anyOf': [{'type': 'object', 'properties': {'sample_weight': {'enum':
    [None]}}}, {'type': 'object', 'properties': {'sample_weight': {'enum':
    [None]}}}, {'type': 'object', 'properties': {'sample_weight': {'type':
    'number'}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(sample_weight, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(sample_weight, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(sample_weight.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [
    {'XXX TODO XXX': "not hasattr(sample_weight, 'sparse')"}, {
    'XXX TODO XXX': 'sample_weight.ndim <= 1'}, {'allOf': [{'anyOf': [{
    'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    '_num_samples(_ensure_sparse_format(sample_weight.sparse.to_coo(), False, dtype=dtype[0], False, True, True)) >= 1'
    }]}, {'anyOf': [{'XXX TODO XXX':
    'sp.issparse(sample_weight.sparse.to_coo())'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "_num_samples(np.asarray(sample_weight.sparse.to_coo(), order='C').astype(dtype[0], casting='unsafe', False)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    "_num_samples(np.asarray(sample_weight.sparse.to_coo(), order='C', dtype=dtype[0])) >= 1"
    }]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(sample_weight, 'sparse')"}, {'XXX TODO XXX':
    'sample_weight.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object',
    'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    '_num_samples(_ensure_sparse_format(sample_weight, False, dtype=dtype[0], False, True, True)) >= 1'
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(sample_weight)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "_num_samples(np.asarray(sample_weight, order='C').astype(dtype[0], casting='unsafe', False)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    "_num_samples(np.asarray(sample_weight, order='C', dtype=dtype[0])) >= 1"
    }]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(sample_weight, 'dtype', None), 'kind')"}, {'allOf':
    [{'XXX TODO XXX': "hasattr(sample_weight, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(sample_weight.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [
    {'XXX TODO XXX': "getattr(sample_weight, 'dtype', None) is None"}, {
    'XXX TODO XXX':
    "getattr(sample_weight, 'dtype', None) not in [np.float64, np.float32]"
    }, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(sample_weight, 'sparse')"}, {'XXX TODO XXX':
    'sample_weight.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object',
    'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    '_num_samples(_ensure_sparse_format(sample_weight.sparse.to_coo(), False, None, False, True, True)) >= 1'
    }]}, {'anyOf': [{'XXX TODO XXX':
    'sp.issparse(sample_weight.sparse.to_coo())'}, {'XXX TODO XXX':
    "_num_samples(np.asarray(sample_weight.sparse.to_coo(), order='C', None)) >= 1"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(sample_weight, 'sparse')"}, {'XXX TODO XXX':
    'sample_weight.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object',
    'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    '_num_samples(_ensure_sparse_format(sample_weight, False, None, False, True, True)) >= 1'
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(sample_weight)'}, {
    'XXX TODO XXX':
    "_num_samples(np.asarray(sample_weight, order='C', None)) >= 1"}]}]}]}]
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "getattr(sample_weight, 'dtype', None) is not None"}, {'XXX TODO XXX':
    "getattr(sample_weight, 'dtype', None) in [np.float64, np.float32]"}]},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(sample_weight, 'sparse')"}, {'XXX TODO XXX':
    'sample_weight.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object',
    'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    '_num_samples(_ensure_sparse_format(sample_weight.sparse.to_coo(), False, dtype=dtype[0], False, True, True)) >= 1'
    }]}, {'anyOf': [{'XXX TODO XXX':
    'sp.issparse(sample_weight.sparse.to_coo())'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "_num_samples(np.asarray(sample_weight.sparse.to_coo(), order='C').astype(dtype[0], casting='unsafe', False)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    "_num_samples(np.asarray(sample_weight.sparse.to_coo(), order='C', dtype=dtype[0])) >= 1"
    }]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(sample_weight, 'sparse')"}, {'XXX TODO XXX':
    'sample_weight.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object',
    'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    '_num_samples(_ensure_sparse_format(sample_weight, False, dtype=dtype[0], False, True, True)) >= 1'
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(sample_weight)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'XXX TODO XXX':
    "_num_samples(np.asarray(sample_weight, order='C').astype(dtype[0], casting='unsafe', False)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'XXX TODO XXX':
    "_num_samples(np.asarray(sample_weight, order='C', dtype=dtype[0])) >= 1"
    }]}]}]}]}]}]}]}]}]}]}]}, {'description':
    'From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) '
    , 'anyOf': [{'type': 'object', 'properties': {'sample_weight': {'enum':
    [None]}}}, {'XXX TODO XXX': "not hasattr(X, 'fit')"}, {'XXX TODO XXX':
    'not callable(X.fit)'}]}, {'description':
    'From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) '
    , 'anyOf': [{'type': 'object', 'properties': {'sample_weight': {'enum':
    [None]}}}, {'XXX TODO XXX': "hasattr(X, '__len__')"}, {'XXX TODO XXX':
    "hasattr(X, 'shape')"}, {'XXX TODO XXX': "hasattr(X, '__array__')"}]},
    {'description':
    "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(     'Singleton array %r cannot be considered a valid collection.' % x) "
    , 'anyOf': [{'type': 'object', 'properties': {'sample_weight': {'enum':
    [None]}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(X, '__len__')"}, {'XXX TODO XXX': "hasattr(X, 'shape')"}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, '__array__')"}, {
    'XXX TODO XXX': "not hasattr(np.asarray(X), 'shape')"}, {'XXX TODO XXX':
    'np.asarray(X).shape is None'}, {'XXX TODO XXX':
    'len(np.asarray(X).shape) != 0'}]}, {'anyOf': [{'XXX TODO XXX':
    "hasattr(X, '__array__')"}, {'XXX TODO XXX': "not hasattr(X, 'shape')"},
    {'XXX TODO XXX': 'X.shape is None'}, {'XXX TODO XXX':
    'len(X.shape) != 0'}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "not hasattr(X, '__len__')"}, {'XXX TODO XXX':
    "not hasattr(X, 'shape')"}]}, {'XXX TODO XXX':
    "not hasattr(X, 'shape')"}, {'XXX TODO XXX': 'X.shape is None'}, {
    'XXX TODO XXX': 'len(X.shape) != 0'}]}]}]}, {'description':
    'From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) from type_error '
    , 'anyOf': [{'type': 'object', 'properties': {'sample_weight': {'enum':
    [None]}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(X, '__len__')"}, {'XXX TODO XXX': "hasattr(X, 'shape')"}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, '__array__')"}, {
    'allOf': [{'XXX TODO XXX': "hasattr(np.asarray(X), 'shape')"}, {
    'XXX TODO XXX': 'np.asarray(X).shape is not None'}]}]}, {'anyOf': [{
    'XXX TODO XXX': "hasattr(X, '__array__')"}, {'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'shape')"}, {'XXX TODO XXX': 'X.shape is not None'}]}]}]}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "not hasattr(X, '__len__')"}, {
    'XXX TODO XXX': "not hasattr(X, 'shape')"}]}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'shape')"}, {'XXX TODO XXX':
    'X.shape is not None'}]}]}, {'XXX TODO XXX':
    'isinstance(x.shape[0], numbers.Integral)'}]}]}, {'description':
    "From /utils/validation.py:None:_check_sample_weight, Exception: raise ValueError('Sample weights must be 1D array or scalar') "
    , 'anyOf': [{'type': 'object', 'properties': {'sample_weight': {'enum':
    [None]}}}, {'type': 'object', 'properties': {'sample_weight': {'enum':
    [None]}}}, {'type': 'object', 'properties': {'sample_weight': {'type':
    'number'}}}, {'XXX TODO XXX':
    "check_array(sample_weight, False, False, dtype=[np.float64, np.float32], order='C', False).ndim == 1"
    }]}, {'description':
    "From /utils/validation.py:None:_check_sample_weight, Exception: raise ValueError('sample_weight.shape == {}, expected {}!'.format(     sample_weight.shape, (n_samples,))) "
    , 'anyOf': [{'type': 'object', 'properties': {'sample_weight': {'enum':
    [None]}}}, {'type': 'object', 'properties': {'sample_weight': {'enum':
    [None]}}}, {'type': 'object', 'properties': {'sample_weight': {'type':
    'number'}}}, {'XXX TODO XXX':
    "check_array(sample_weight, False, False, dtype=[np.float64, np.float32], order='C', False).shape == [_num_samples(X)]"
    }]}, {'description':
    "From /utils/validation.py:None:column_or_1d, Exception: raise ValueError('y should be a 1d array, got an array of shape {} instead.'     .format(shape)) "
    , 'allOf': [{'XXX TODO XXX': 'len(y.shape) != 1'}, {'XXX TODO XXX':
    'y.shape[1] != 1'}]}, {'description':
    "From /ensemble/_base.py:BaseEnsemble:_validate_estimator, Exception: raise ValueError('n_estimators must be an integer, got {0}.'.format(type(     self.n_estimators))) "
    , 'type': 'object', 'properties': {'n_estimators': {'type': 'integer'}}
    }, {'description':
    "From /ensemble/_base.py:BaseEnsemble:_validate_estimator, Exception: raise ValueError('n_estimators must be greater than zero, got {0}.'.format(     self.n_estimators)) "
    , 'type': 'object', 'properties': {'n_estimators': {'type': 'number',
    'minimum': 0, 'exclusiveMinimum': True}}}, {'description':
    "From /ensemble/_base.py:BaseEnsemble:_validate_estimator, Exception: raise ValueError('base_estimator cannot be None') "
    , 'allOf': [{'anyOf': [{'type': 'object', 'properties': {
    'base_estimator': {'enum': [None]}}}, {'type': 'object', 'properties':
    {'base_estimator': {'not': {'enum': [None]}}}}]}, {'type': 'object',
    'properties': {'base_estimator': {'not': {'enum': [None]}}}}]}, {
    'description':
    "From /utils/fixes.py:None:_joblib_parallel_args, Exception: raise ValueError('prefer=%s is not supported' % prefer) "
    , 'allOf': [{'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'warm_start': {'enum': [True]}}}, {'XXX TODO XXX':
    "hasattr(self, 'estimators_')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'n_estimators': {'type': 'number', 'minimum': 
    0}}}, {'XXX TODO XXX':
    "parse_version(joblib.__version__) >= parse_version('0.12')"}, {
    'XXX TODO XXX': "kwargs['prefer'] in ['threads', 'processes', None]"}]},
    {'anyOf': [{'type': 'object', 'properties': {'n_estimators': {'type':
    'number', 'maximum': 0, 'exclusiveMaximum': True}}}, {'type': 'object',
    'properties': {'n_estimators': {'enum': [0]}}}, {'XXX TODO XXX':
    "parse_version(joblib.__version__) >= parse_version('0.12')"}, {
    'XXX TODO XXX': "kwargs['prefer'] in ['threads', 'processes', None]"}]}
    ]}]}, {'anyOf': [{'type': 'object', 'properties': {'warm_start': {
    'enum': [False]}}}, {'XXX TODO XXX': "not hasattr(self, 'estimators_')"
    }, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'self.n_estimators - len(self.estimators_) >= 0'}, {'XXX TODO XXX':
    "parse_version(joblib.__version__) >= parse_version('0.12')"}, {
    'XXX TODO XXX': "kwargs['prefer'] in ['threads', 'processes', None]"}]},
    {'anyOf': [{'XXX TODO XXX':
    'self.n_estimators - len(self.estimators_) < 0'}, {'XXX TODO XXX':
    'self.n_estimators - len(self.estimators_) == 0'}, {'XXX TODO XXX':
    "parse_version(joblib.__version__) >= parse_version('0.12')"}, {
    'XXX TODO XXX': "kwargs['prefer'] in ['threads', 'processes', None]"}]}
    ]}]}]}, {'description':
    "From /ensemble/_iforest.py:IsolationForest:_set_oob_score, Exception: raise NotImplementedError('OOB score not supported by iforest') "
    , 'allOf': [{'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'warm_start': {'enum': [True]}}}, {'XXX TODO XXX':
    "hasattr(self, 'estimators_')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'n_estimators': {'type': 'number', 'minimum': 
    0}}}, {'type': 'object', 'properties': {'oob_score': {'enum': [False]}}
    }]}, {'anyOf': [{'type': 'object', 'properties': {'n_estimators': {
    'type': 'number', 'maximum': 0, 'exclusiveMaximum': True}}}, {'type':
    'object', 'properties': {'n_estimators': {'enum': [0]}}}, {'type':
    'object', 'properties': {'oob_score': {'enum': [False]}}}]}]}]}, {
    'anyOf': [{'type': 'object', 'properties': {'warm_start': {'enum': [
    False]}}}, {'XXX TODO XXX': "not hasattr(self, 'estimators_')"}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX':
    'self.n_estimators - len(self.estimators_) >= 0'}, {'type': 'object',
    'properties': {'oob_score': {'enum': [False]}}}]}, {'anyOf': [{
    'XXX TODO XXX': 'self.n_estimators - len(self.estimators_) < 0'}, {
    'XXX TODO XXX': 'self.n_estimators - len(self.estimators_) == 0'}, {
    'type': 'object', 'properties': {'oob_score': {'enum': [False]}}}]}]}]}
    ]}, {'description':
    "From /ensemble/_bagging.py:BaseBagging:_fit, Exception: raise ValueError('max_samples must be in (0, n_samples]') "
    , 'allOf': [{'anyOf': [{'type': 'object', 'properties': {'max_samples':
    {'not': {'type': 'string'}}}}, {'allOf': [{'anyOf': [{'type': 'object',
    'properties': {'max_samples': {'not': {'enum': ['auto']}}}}, {'allOf':
    [{'anyOf': [{'XXX TODO XXX': 'min(256, X.shape[0]) is not None'}, {
    'allOf': [{'type': 'object', 'properties': {'max_samples': {'type':
    'number', 'minimum': 0, 'exclusiveMinimum': True}}}, {'type': 'object',
    'properties': {'max_samples': {'laleMaximum': 'X/maxItems'}}}]}]}, {
    'anyOf': [{'XXX TODO XXX': 'min(256, X.shape[0]) is None'}, {'allOf': [
    {'anyOf': [{'XXX TODO XXX':
    'isinstance(min(256, X.shape[0]), numbers.Integral)'}, {'allOf': [{
    'XXX TODO XXX': '0 < int(min(256, X.shape[0]) * X.shape[0])'}, {
    'XXX TODO XXX': 'int(min(256, X.shape[0]) * X.shape[0]) <= X.shape[0]'}
    ]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(min(256, X.shape[0]), numbers.Integral)'}, {'allOf': [{
    'XXX TODO XXX': '0 < 256'}, {'XXX TODO XXX': '0 < X.shape[0]'}, {
    'XXX TODO XXX': 'min(256, X.shape[0]) <= X.shape[0]'}]}]}]}]}]}]}, {
    'anyOf': [{'type': 'object', 'properties': {'max_samples': {'enum': [
    'auto']}}}, {'allOf': [{'anyOf': [{'type': 'object', 'properties': {
    'max_samples': {'not': {'enum': [None]}}}}, {'allOf': [{'type':
    'object', 'properties': {'max_samples': {'type': 'number', 'minimum': 0,
    'exclusiveMinimum': True}}}, {'type': 'object', 'properties': {
    'max_samples': {'laleMaximum': 'X/maxItems'}}}]}]}, {'anyOf': [{'type':
    'object', 'properties': {'max_samples': {'enum': [None]}}}, {'allOf': [
    {'anyOf': [{'type': 'object', 'properties': {'max_samples': {'type':
    'integer'}}}, {'allOf': [{'XXX TODO XXX':
    '0 < int(max_samples * X.shape[0])'}, {'XXX TODO XXX':
    'int(max_samples * X.shape[0]) <= X.shape[0]'}]}]}, {'anyOf': [{'type':
    'object', 'properties': {'max_samples': {'not': {'type': 'integer'}}}},
    {'allOf': [{'type': 'object', 'properties': {'max_samples': {'type':
    'number', 'minimum': 0, 'exclusiveMinimum': True}}}, {'type': 'object',
    'properties': {'max_samples': {'laleMaximum': 'X/maxItems'}}}]}]}]}]}]}
    ]}]}]}, {'anyOf': [{'type': 'object', 'properties': {'max_samples': {
    'type': 'string'}}}, {'allOf': [{'anyOf': [{'type': 'object',
    'properties': {'max_samples': {'not': {'type': 'integer'}}}}, {'allOf':
    [{'anyOf': [{'type': 'object', 'properties': {'max_samples': {
    'laleMaximum': 'X/maxItems'}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'X.shape[0] is not None'}, {'allOf': [{'type': 'object', 'properties':
    {'max_samples': {'type': 'number', 'minimum': 0, 'exclusiveMinimum': 
    True}}}, {'type': 'object', 'properties': {'max_samples': {
    'laleMaximum': 'X/maxItems'}}}]}]}, {'anyOf': [{'XXX TODO XXX':
    'X.shape[0] is None'}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(X.shape[0], numbers.Integral)'}, {'allOf': [{'XXX TODO XXX':
    '0 < int(X.shape[0] * X.shape[0])'}, {'XXX TODO XXX':
    'int(X.shape[0] * X.shape[0]) <= X.shape[0]'}]}]}, {'anyOf': [{
    'XXX TODO XXX': 'isinstance(X.shape[0], numbers.Integral)'}, {'allOf':
    [{'XXX TODO XXX': '0 < X.shape[0]'}, {'XXX TODO XXX':
    'X.shape[0] <= X.shape[0]'}]}]}]}]}]}]}, {'anyOf': [{'type': 'object',
    'properties': {'max_samples': {'laleMinimum': 'X/maxItems'}}}, {'allOf':
    [{'anyOf': [{'type': 'object', 'properties': {'max_samples': {'not': {
    'enum': [None]}}}}, {'allOf': [{'type': 'object', 'properties': {
    'max_samples': {'type': 'number', 'minimum': 0, 'exclusiveMinimum': 
    True}}}, {'type': 'object', 'properties': {'max_samples': {
    'laleMaximum': 'X/maxItems'}}}]}]}, {'anyOf': [{'type': 'object',
    'properties': {'max_samples': {'enum': [None]}}}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'max_samples': {'type': 'integer'}}},
    {'allOf': [{'XXX TODO XXX': '0 < int(self.max_samples * X.shape[0])'},
    {'XXX TODO XXX': 'int(self.max_samples * X.shape[0]) <= X.shape[0]'}]}]
    }, {'anyOf': [{'type': 'object', 'properties': {'max_samples': {'not':
    {'type': 'integer'}}}}, {'allOf': [{'type': 'object', 'properties': {
    'max_samples': {'type': 'number', 'minimum': 0, 'exclusiveMinimum': 
    True}}}, {'type': 'object', 'properties': {'max_samples': {
    'laleMaximum': 'X/maxItems'}}}]}]}]}]}]}]}]}]}, {'anyOf': [{'type':
    'object', 'properties': {'max_samples': {'type': 'integer'}}}, {'allOf':
    [{'anyOf': [{'XXX TODO XXX':
    'int(self.max_samples * X.shape[0]) is not None'}, {'allOf': [{'type':
    'object', 'properties': {'max_samples': {'type': 'number', 'minimum': 0,
    'exclusiveMinimum': True}}}, {'type': 'object', 'properties': {
    'max_samples': {'laleMaximum': 'X/maxItems'}}}]}]}, {'anyOf': [{
    'XXX TODO XXX': 'int(self.max_samples * X.shape[0]) is None'}, {'allOf':
    [{'anyOf': [{'XXX TODO XXX':
    'isinstance(int(self.max_samples * X.shape[0]), numbers.Integral)'}, {
    'allOf': [{'XXX TODO XXX':
    '0 < int(int(self.max_samples * X.shape[0]) * X.shape[0])'}, {
    'XXX TODO XXX':
    'int(int(self.max_samples * X.shape[0]) * X.shape[0]) <= X.shape[0]'}]}
    ]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(int(self.max_samples * X.shape[0]), numbers.Integral)'}, {
    'allOf': [{'XXX TODO XXX': '0 < int(self.max_samples * X.shape[0])'}, {
    'XXX TODO XXX': 'int(self.max_samples * X.shape[0]) <= X.shape[0]'}]}]}
    ]}]}]}]}]}]}]}, {'description':
    "From /ensemble/_bagging.py:BaseBagging:_fit, Exception: raise ValueError('max_features must be int or float') "
    , 'anyOf': [{'type': 'object', 'properties': {'max_features': {'type':
    'integer'}}}, {'type': 'object', 'properties': {'max_features': {'type':
    'number'}}}]}, {'description':
    "From /ensemble/_bagging.py:BaseBagging:_fit, Exception: raise ValueError('max_features must be in (0, n_features]') "
    , 'allOf': [{'anyOf': [{'type': 'object', 'properties': {'max_features':
    {'not': {'type': 'integer'}}}}, {'allOf': [{'type': 'object',
    'properties': {'max_features': {'type': 'number', 'minimum': 0,
    'exclusiveMinimum': True}}}, {'type': 'object', 'properties': {
    'max_features': {'laleMaximum': 'X/items/maxItems'}}}]}]}, {'anyOf': [{
    'type': 'object', 'properties': {'max_features': {'type': 'integer'}}},
    {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'max_features':
    {'not': {'type': 'number'}}}}, {'allOf': [{'XXX TODO XXX':
    '0 < self.max_features * X.shape[1]'}, {'XXX TODO XXX':
    'self.max_features * X.shape[1] <= X.shape[1]'}]}]}, {'anyOf': [{'type':
    'object', 'properties': {'max_features': {'type': 'number'}}}, {'allOf':
    [{'type': 'object', 'properties': {'max_features': {'type': 'number',
    'minimum': 0, 'exclusiveMinimum': True}}}, {'type': 'object',
    'properties': {'max_features': {'laleMaximum': 'X/items/maxItems'}}}]}]
    }]}]}]}, {'description':
    "From /ensemble/_bagging.py:BaseBagging:_fit, Exception: raise ValueError('Out of bag estimation only available if bootstrap=True') "
    , 'anyOf': [{'type': 'object', 'properties': {'bootstrap': {'enum': [
    True]}}}, {'type': 'object', 'properties': {'oob_score': {'enum': [
    False]}}}]}, {'description':
    "From /ensemble/_bagging.py:BaseBagging:_fit, Exception: raise ValueError('Out of bag estimate only available if warm_start=False') "
    , 'anyOf': [{'type': 'object', 'properties': {'warm_start': {'enum': [
    False]}}}, {'type': 'object', 'properties': {'oob_score': {'enum': [
    False]}}}]}, {'description':
    "From /ensemble/_bagging.py:BaseBagging:_fit, Exception: raise ValueError(     'n_estimators=%d must be larger or equal to len(estimators_)=%d when warm_start==True'      % (self.n_estimators, len(self.estimators_))) "
    , 'allOf': [{'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'warm_start': {'enum': [True]}}}, {'XXX TODO XXX':
    "hasattr(self, 'estimators_')"}]}, {'type': 'object', 'properties': {
    'n_estimators': {'type': 'number', 'minimum': 0}}}]}, {'anyOf': [{
    'type': 'object', 'properties': {'warm_start': {'enum': [False]}}}, {
    'XXX TODO XXX': "not hasattr(self, 'estimators_')"}, {'XXX TODO XXX':
    'self.n_estimators - len(self.estimators_) >= 0'}]}]}, {'description':
    'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) '
    , 'anyOf': [{'type': 'object', 'properties': {'contamination': {'enum':
    ['auto']}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(X.sparse.to_coo(), 'dtype')"}, {'XXX TODO XXX':
    'X.sparse.to_coo().dtype is None'}, {'XXX TODO XXX':
    "not hasattr(X.sparse.to_coo().dtype, 'kind')"}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype.kind != 'c'"}]}, {'anyOf': [{'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}
    ]}, {'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(X, 'dtype')"}, {'XXX TODO XXX': 'X.dtype is None'}, {
    'XXX TODO XXX': "not hasattr(X.dtype, 'kind')"}, {'XXX TODO XXX':
    "X.dtype.kind != 'c'"}]}]}]}, {'description':
    'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) '
    , 'anyOf': [{'type': 'object', 'properties': {'contamination': {'enum':
    ['auto']}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
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
    , 'anyOf': [{'type': 'object', 'properties': {'contamination': {'enum':
    ['auto']}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
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
    , 'allOf': [{'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'max_samples': {
    'not': {'type': 'string'}}}}, {'allOf': [{'anyOf': [{'type': 'object',
    'properties': {'max_samples': {'not': {'enum': ['auto']}}}}, {'type':
    'object', 'properties': {'contamination': {'enum': ['auto']}}}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX':
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
    }]}]}]}]}, {'anyOf': [{'type': 'object', 'properties': {'max_samples':
    {'enum': ['auto']}}}, {'type': 'object', 'properties': {'contamination':
    {'enum': ['auto']}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
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
    }]}]}]}]}]}]}, {'anyOf': [{'type': 'object', 'properties': {
    'max_samples': {'type': 'string'}}}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'max_samples': {'not': {'type': 'integer'}}}},
    {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'max_samples':
    {'laleMaximum': 'X/maxItems'}}}, {'type': 'object', 'properties': {
    'contamination': {'enum': ['auto']}}}, {'allOf': [{'anyOf': [{
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
    }]}]}]}]}, {'anyOf': [{'type': 'object', 'properties': {'max_samples':
    {'laleMinimum': 'X/maxItems'}}}, {'type': 'object', 'properties': {
    'contamination': {'enum': ['auto']}}}, {'allOf': [{'anyOf': [{
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
    }]}]}]}]}]}]}, {'anyOf': [{'type': 'object', 'properties': {
    'max_samples': {'type': 'integer'}}}, {'allOf': [{'anyOf': [{'allOf': [
    {'type': 'object', 'properties': {'max_samples': {'type': 'number',
    'minimum': 0.0, 'exclusiveMinimum': True}}}, {'type': 'object',
    'properties': {'max_samples': {'type': 'number', 'maximum': 1.0}}}]}, {
    'type': 'object', 'properties': {'contamination': {'enum': ['auto']}}},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
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
    }]}]}]}]}, {'anyOf': [{'type': 'object', 'properties': {'max_samples':
    {'type': 'number', 'maximum': 0.0}}}, {'type': 'object', 'properties':
    {'max_samples': {'type': 'number', 'minimum': 1.0, 'exclusiveMinimum': 
    True}}}, {'type': 'object', 'properties': {'contamination': {'enum': [
    'auto']}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
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
    }]}]}]}]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX': 'issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'max_samples': {
    'not': {'type': 'string'}}}}, {'allOf': [{'anyOf': [{'type': 'object',
    'properties': {'max_samples': {'not': {'enum': ['auto']}}}}, {'type':
    'object', 'properties': {'contamination': {'enum': ['auto']}}}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX':
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
    }]}]}]}]}, {'anyOf': [{'type': 'object', 'properties': {'max_samples':
    {'enum': ['auto']}}}, {'type': 'object', 'properties': {'contamination':
    {'enum': ['auto']}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
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
    }]}]}]}]}]}]}, {'anyOf': [{'type': 'object', 'properties': {
    'max_samples': {'type': 'string'}}}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'max_samples': {'not': {'type': 'integer'}}}},
    {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'max_samples':
    {'laleMaximum': 'X/maxItems'}}}, {'type': 'object', 'properties': {
    'contamination': {'enum': ['auto']}}}, {'allOf': [{'anyOf': [{
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
    }]}]}]}]}, {'anyOf': [{'type': 'object', 'properties': {'max_samples':
    {'laleMinimum': 'X/maxItems'}}}, {'type': 'object', 'properties': {
    'contamination': {'enum': ['auto']}}}, {'allOf': [{'anyOf': [{
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
    }]}]}]}]}]}]}, {'anyOf': [{'type': 'object', 'properties': {
    'max_samples': {'type': 'integer'}}}, {'allOf': [{'anyOf': [{'allOf': [
    {'type': 'object', 'properties': {'max_samples': {'type': 'number',
    'minimum': 0.0, 'exclusiveMinimum': True}}}, {'type': 'object',
    'properties': {'max_samples': {'type': 'number', 'maximum': 1.0}}}]}, {
    'type': 'object', 'properties': {'contamination': {'enum': ['auto']}}},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
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
    }]}]}]}]}, {'anyOf': [{'type': 'object', 'properties': {'max_samples':
    {'type': 'number', 'maximum': 0.0}}}, {'type': 'object', 'properties':
    {'max_samples': {'type': 'number', 'minimum': 1.0, 'exclusiveMinimum': 
    True}}}, {'type': 'object', 'properties': {'contamination': {'enum': [
    'auto']}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
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
    }]}]}]}]}]}]}]}]}]}]}]}, {'description':
    'From /utils/validation.py:None:check_array, Exception: raise ValueError("""Complex data not supported {} """.format(array)     ) from complex_warning '
    , 'anyOf': [{'type': 'object', 'properties': {'contamination': {'enum':
    ['auto']}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}]}, {'anyOf': [{
    'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}]}]}]}, {
    'description':
    'From /utils/validation.py:None:check_array, Exception: raise ValueError(     "Unable to convert array of bytes/strings into decimal numbers with dtype=\'numeric\'"     ) from e '
    , 'anyOf': [{'type': 'object', 'properties': {'contamination': {'enum':
    ['auto']}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
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
    , 'anyOf': [{'type': 'object', 'properties': {'contamination': {'enum':
    ['auto']}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
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
    , 'anyOf': [{'type': 'object', 'properties': {'contamination': {'enum':
    ['auto']}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
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
    , 'anyOf': [{'type': 'object', 'properties': {'contamination': {'enum':
    ['auto']}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
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
    , 'anyOf': [{'type': 'object', 'properties': {'contamination': {'enum':
    ['auto']}}}, {'XXX TODO XXX': 'not isclass(self)'}]}, {'description':
    "From /utils/validation.py:None:check_is_fitted, Exception: raise TypeError('%s is not an estimator instance.' % estimator) "
    , 'anyOf': [{'type': 'object', 'properties': {'contamination': {'enum':
    ['auto']}}}, {'XXX TODO XXX': "hasattr(self, 'fit')"}]}, {'description':
    "From /ensemble/_iforest.py:IsolationForest:score_samples, Exception: raise ValueError(     'Number of features of the model must match the input. Model n_features is {0} and input n_features is {1}.'     .format(self.n_features_, X.shape[1])) "
    , 'anyOf': [{'type': 'object', 'properties': {'contamination': {'enum':
    ['auto']}}}, {'XXX TODO XXX': 'self.n_features_ == X.shape[1]'}]}, {
    'description':
    'From /ensemble/_iforest.py:IsolationForest:fit, Exception: raise ValueError(     \'max_samples (%s) is not supported.Valid choices are: "auto", int orfloat\'      % self.max_samples) '
    , 'anyOf': [{'type': 'object', 'properties': {'max_samples': {'not': {
    'type': 'string'}}}}, {'type': 'object', 'properties': {'max_samples':
    {'enum': ['auto']}}}]}, {'description':
    "From /ensemble/_iforest.py:IsolationForest:fit, Exception: raise ValueError('max_samples must be in (0, 1], got %r' % self.max_samples) "
    , 'anyOf': [{'type': 'object', 'properties': {'max_samples': {'type':
    'string'}}}, {'type': 'object', 'properties': {'max_samples': {'type':
    'integer'}}}, {'allOf': [{'type': 'object', 'properties': {
    'max_samples': {'type': 'number', 'minimum': 0.0, 'exclusiveMinimum': 
    True}}}, {'type': 'object', 'properties': {'max_samples': {'type':
    'number', 'maximum': 1.0}}}]}]}]

