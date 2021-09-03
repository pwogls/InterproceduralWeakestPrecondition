[{'description':
    'From /utils/validation.py:None:_assert_all_finite, Exception: raise ValueError(msg_err.format(type_err, msg_dtype if msg_dtype is not     None else X.dtype)) '
    , 'anyOf': [{'XXX TODO XXX': 'is_multilabel(y)'}, {'XXX TODO XXX':
    'y.ndim > 2'}, {'allOf': [{'XXX TODO XXX': 'y.dtype == object'}, {
    'XXX TODO XXX': 'len(y)'}, {'XXX TODO XXX':
    'isinstance(y.flat[0], str)'}]}, {'allOf': [{'XXX TODO XXX':
    'y.ndim == 2'}, {'XXX TODO XXX': 'y.shape[1] == 0'}]}, {'XXX TODO XXX':
    "y.dtype.kind != 'f'"}, {'XXX TODO XXX':
    'not np.any(y != y.astype(int))'}, {'XXX TODO XXX':
    "_get_config()['assume_finite']"}, {'allOf': [{'XXX TODO XXX':
    "y.dtype.kind in 'fc'"}, {'XXX TODO XXX':
    'np.isfinite(_safe_accumulator_op(np.sum, y))'}]}, {'XXX TODO XXX':
    "y.dtype.kind not in 'fc'"}, {'XXX TODO XXX': 'np.isfinite(y).all()'}]},
    {'description':
    "From /utils/validation.py:None:_assert_all_finite, Exception: raise ValueError('Input contains NaN') "
    , 'anyOf': [{'XXX TODO XXX': 'is_multilabel(y)'}, {'XXX TODO XXX':
    'y.ndim > 2'}, {'allOf': [{'XXX TODO XXX': 'y.dtype == object'}, {
    'XXX TODO XXX': 'len(y)'}, {'XXX TODO XXX':
    'isinstance(y.flat[0], str)'}]}, {'allOf': [{'XXX TODO XXX':
    'y.ndim == 2'}, {'XXX TODO XXX': 'y.shape[1] == 0'}]}, {'XXX TODO XXX':
    "y.dtype.kind != 'f'"}, {'XXX TODO XXX':
    'not np.any(y != y.astype(int))'}, {'XXX TODO XXX':
    "_get_config()['assume_finite']"}, {'allOf': [{'XXX TODO XXX':
    "y.dtype.kind in 'fc'"}, {'XXX TODO XXX':
    'np.isfinite(_safe_accumulator_op(np.sum, y))'}]}, {'XXX TODO XXX':
    "y.dtype.kind in 'fc'"}, {'XXX TODO XXX':
    "y.dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'not _object_dtype_isnan(y).any()'}]}, {'description':
    "From /utils/multiclass.py:None:type_of_target, Exception: raise ValueError(     'Expected array-like (array or non-string sequence), got %r' % y) "
    , 'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(y, [Sequence, spmatrix])'}, {'XXX TODO XXX':
    "hasattr(y, '__array__')"}]}, {'type': 'object', 'properties': {'y': {
    'not': {'type': 'string'}}}}]}, {'description':
    'From /utils/multiclass.py:None:type_of_target, Exception: raise ValueError("y cannot be class \'SparseSeries\' or \'SparseArray\'") '
    , 'XXX TODO XXX':
    "y.__class__.__name__ not in ['SparseSeries', 'SparseArray']"}, {
    'description':
    "From /utils/multiclass.py:None:type_of_target, Exception: raise ValueError(     'You appear to be using a legacy multi-label data representation. Sequence of sequences are no longer supported; use a binary array or sparse matrix instead - the MultiLabelBinarizer transformer can convert to this format.'     ) "
    , 'anyOf': [{'XXX TODO XXX': 'is_multilabel(y)'}, {'XXX TODO XXX':
    "hasattr(y[0], '__array__')"}, {'XXX TODO XXX':
    'isinstance(y[0], Sequence)'}, {'XXX TODO XXX': 'isinstance(y[0], str)'
    }]}, {'description':
    "From /utils/multiclass.py:None:check_classification_targets, Exception: raise ValueError('Unknown label type: %r' % y_type) "
    , 'XXX TODO XXX':
    "type_of_target(y) in ['binary', 'multiclass', 'multiclass-multioutput', 'multilabel-indicator', 'multilabel-sequences']"
    }, {'description':
    'From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) '
    , 'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'fit')"}, {'XXX TODO XXX':
    'not callable(X.fit)'}]}, {'description':
    'From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) '
    , 'anyOf': [{'XXX TODO XXX': "hasattr(X, '__len__')"}, {'XXX TODO XXX':
    "hasattr(X, 'shape')"}, {'XXX TODO XXX': "hasattr(X, '__array__')"}]},
    {'description':
    "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(     'Singleton array %r cannot be considered a valid collection.' % x) "
    , 'allOf': [{'anyOf': [{'XXX TODO XXX': "hasattr(X, '__len__')"}, {
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
    'XXX TODO XXX': 'len(X.shape) != 0'}]}]}, {'description':
    'From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) from type_error '
    , 'allOf': [{'anyOf': [{'XXX TODO XXX': "hasattr(X, '__len__')"}, {
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
    'isinstance(x.shape[0], numbers.Integral)'}]}, {'description':
    "From /utils/validation.py:None:check_consistent_length, Exception: raise ValueError(     'Found input variables with inconsistent numbers of samples: %r' % [int     (l) for l in lengths]) "
    , 'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }, {'description':
    "From /utils/validation.py:None:check_is_fitted, Exception: raise TypeError('{} is a class, not an instance.'.format(estimator)) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'not': {'enum': [
    'prefit']}}}}, {'XXX TODO XXX':
    'isinstance(self.base_estimator, Pipeline)'}, {'XXX TODO XXX':
    'not isclass(self.base_estimator[-1])'}]}, {'description':
    "From /utils/validation.py:None:check_is_fitted, Exception: raise TypeError('%s is not an estimator instance.' % estimator) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'not': {'enum': [
    'prefit']}}}}, {'XXX TODO XXX':
    'isinstance(self.base_estimator, Pipeline)'}, {'XXX TODO XXX':
    "hasattr(self.base_estimator[-1], 'fit')"}]},{'description':
    "From /utils/validation.py:None:check_is_fitted, Exception: raise TypeError('{} is a class, not an instance.'.format(estimator)) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'not': {'enum': [
    'prefit']}}}}, {'XXX TODO XXX':
    'isinstance(self.base_estimator, Pipeline)'}, {'XXX TODO XXX':
    'not isclass(self.base_estimator)'}]}, {'description':
    "From /utils/validation.py:None:check_is_fitted, Exception: raise TypeError('%s is not an estimator instance.' % estimator) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'not': {'enum': [
    'prefit']}}}}, {'XXX TODO XXX':
    'isinstance(self.base_estimator, Pipeline)'}, {'XXX TODO XXX':
    "hasattr(self.base_estimator, 'fit')"}]}, {'description':
    'From /calibration.py:None:_get_prediction_method, Exception: raise RuntimeError(     "\'base_estimator\' has no \'decision_function\' or \'predict_proba\' method.") '
    , 'allOf': [{'anyOf': [{'type': 'object', 'properties': {
    'base_estimator': {'not': {'enum': [None]}}}}, {'type': 'object',
    'properties': {'cv': {'not': {'enum': ['prefit']}}}}, {'XXX TODO XXX':
    "hasattr(LinearSVC(random_state=0), 'decision_function')"}, {
    'XXX TODO XXX': "hasattr(LinearSVC(random_state=0), 'predict_proba')"}]
    }, {'anyOf': [{'type': 'object', 'properties': {'base_estimator': {
    'enum': [None]}}}, {'type': 'object', 'properties': {'cv': {'not': {
    'enum': ['prefit']}}}}, {'XXX TODO XXX':
    "hasattr(self.base_estimator, 'decision_function')"}, {'XXX TODO XXX':
    "hasattr(self.base_estimator, 'predict_proba')"}]}]}, {'description':
    'From /calibration.py:None:_get_prediction_method, Exception: raise RuntimeError(     "\'base_estimator\' has no \'decision_function\' or \'predict_proba\' method.") '
    , 'allOf': [{'anyOf': [{'type': 'object', 'properties': {
    'base_estimator': {'not': {'enum': [None]}}}}, {'type': 'object',
    'properties': {'cv': {'enum': ['prefit']}}}, {'type': 'object',
    'properties': {'ensemble': {'enum': [True]}}}, {'XXX TODO XXX':
    "hasattr(clone(LinearSVC(random_state=0)), 'decision_function')"}, {
    'XXX TODO XXX':
    "hasattr(clone(LinearSVC(random_state=0)), 'predict_proba')"}]}, {
    'anyOf': [{'type': 'object', 'properties': {'base_estimator': {'enum':
    [None]}}}, {'type': 'object', 'properties': {'cv': {'enum': ['prefit']}
    }}, {'type': 'object', 'properties': {'ensemble': {'enum': [True]}}}, {
    'XXX TODO XXX':
    "hasattr(clone(self.base_estimator), 'decision_function')"}, {
    'XXX TODO XXX': "hasattr(clone(self.base_estimator), 'predict_proba')"}
    ]}]}, {'description':
    "From /calibration.py:None:_compute_predictions, Exception: raise ValueError(f'Invalid prediction method: {method_name}') "
    , 'allOf': [{'anyOf': [{'type': 'object', 'properties': {
    'base_estimator': {'not': {'enum': [None]}}}}, {'type': 'object',
    'properties': {'cv': {'not': {'enum': ['prefit']}}}}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX':
    "not hasattr(_get_prediction_method(LinearSVC(random_state=0)), '__name__')"
    }, {'XXX TODO XXX':
    "_get_prediction_method(LinearSVC(random_state=0)).__name__ == 'decision_function'"
    }, {'XXX TODO XXX':
    "_get_prediction_method(LinearSVC(random_state=0)).__name__ == 'predict_proba'"
    }]}, {'anyOf': [{'XXX TODO XXX':
    "hasattr(_get_prediction_method(LinearSVC(random_state=0)), '__name__')"
    }, {'XXX TODO XXX':
    "signature(pred_method).parameters['method'].default == 'decision_function'"
    }, {'XXX TODO XXX':
    "signature(pred_method).parameters['method'].default == 'predict_proba'"
    }]}]}]}, {'anyOf': [{'type': 'object', 'properties': {'base_estimator':
    {'enum': [None]}}}, {'type': 'object', 'properties': {'cv': {'not': {
    'enum': ['prefit']}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(_get_prediction_method(self.base_estimator), '__name__')"},
    {'XXX TODO XXX':
    "_get_prediction_method(self.base_estimator).__name__ == 'decision_function'"
    }, {'XXX TODO XXX':
    "_get_prediction_method(self.base_estimator).__name__ == 'predict_proba'"
    }]}, {'anyOf': [{'XXX TODO XXX':
    "hasattr(_get_prediction_method(self.base_estimator), '__name__')"}, {
    'XXX TODO XXX':
    "signature(pred_method).parameters['method'].default == 'decision_function'"
    }, {'XXX TODO XXX':
    "signature(pred_method).parameters['method'].default == 'predict_proba'"
    }]}]}]}]}, {'description':
    "From /calibration.py:None:_compute_predictions, Exception: raise ValueError(f'Invalid prediction method: {method_name}') "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'ensemble': {'enum': [True]}}},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(partial(cross_val_predict, estimator=clone(LinearSVC(random_state=0)), X=X, y=y, cv=check_cv(self.cv, y, True), method=_get_prediction_method(clone(LinearSVC(random_state=0))).__name__, n_jobs=self.n_jobs), '__name__')"
    }, {'XXX TODO XXX':
    "partial(cross_val_predict, estimator=clone(LinearSVC(random_state=0)), X=X, y=y, cv=check_cv(self.cv, y, True), method=_get_prediction_method(clone(LinearSVC(random_state=0))).__name__, n_jobs=self.n_jobs).__name__ == 'decision_function'"
    }, {'XXX TODO XXX':
    "partial(cross_val_predict, estimator=clone(LinearSVC(random_state=0)), X=X, y=y, cv=check_cv(self.cv, y, True), method=_get_prediction_method(clone(LinearSVC(random_state=0))).__name__, n_jobs=self.n_jobs).__name__ == 'predict_proba'"
    }]}, {'anyOf': [{'XXX TODO XXX':
    "hasattr(partial(cross_val_predict, estimator=clone(LinearSVC(random_state=0)), X=X, y=y, cv=check_cv(self.cv, y, True), method=_get_prediction_method(clone(LinearSVC(random_state=0))).__name__, n_jobs=self.n_jobs), '__name__')"
    }, {'XXX TODO XXX':
    "signature(pred_method).parameters['method'].default == 'decision_function'"
    }, {'XXX TODO XXX':
    "signature(pred_method).parameters['method'].default == 'predict_proba'"
    }]}]}]}, {'description':
    'From /utils/validation.py:None:_assert_all_finite, Exception: raise ValueError(msg_err.format(type_err, msg_dtype if msg_dtype is not     None else X.dtype)) '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'not': {'enum': [
    'prefit']}}}}, {'XXX TODO XXX': 'is_multilabel(y)'}, {'XXX TODO XXX':
    'y.ndim > 2'}, {'allOf': [{'XXX TODO XXX': 'y.dtype == object'}, {
    'XXX TODO XXX': 'len(y)'}, {'XXX TODO XXX':
    'isinstance(y.flat[0], str)'}]}, {'allOf': [{'XXX TODO XXX':
    'y.ndim == 2'}, {'XXX TODO XXX': 'y.shape[1] == 0'}]}, {'XXX TODO XXX':
    "y.dtype.kind != 'f'"}, {'XXX TODO XXX':
    'not np.any(y != y.astype(int))'}, {'XXX TODO XXX':
    "_get_config()['assume_finite']"}, {'allOf': [{'XXX TODO XXX':
    "y.dtype.kind in 'fc'"}, {'XXX TODO XXX':
    'np.isfinite(_safe_accumulator_op(np.sum, y))'}]}, {'XXX TODO XXX':
    "y.dtype.kind not in 'fc'"}, {'XXX TODO XXX': 'np.isfinite(y).all()'}]},
    {'description':
    "From /utils/validation.py:None:_assert_all_finite, Exception: raise ValueError('Input contains NaN') "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'not': {'enum': [
    'prefit']}}}}, {'XXX TODO XXX': 'is_multilabel(y)'}, {'XXX TODO XXX':
    'y.ndim > 2'}, {'allOf': [{'XXX TODO XXX': 'y.dtype == object'}, {
    'XXX TODO XXX': 'len(y)'}, {'XXX TODO XXX':
    'isinstance(y.flat[0], str)'}]}, {'allOf': [{'XXX TODO XXX':
    'y.ndim == 2'}, {'XXX TODO XXX': 'y.shape[1] == 0'}]}, {'XXX TODO XXX':
    "y.dtype.kind != 'f'"}, {'XXX TODO XXX':
    'not np.any(y != y.astype(int))'}, {'XXX TODO XXX':
    "_get_config()['assume_finite']"}, {'allOf': [{'XXX TODO XXX':
    "y.dtype.kind in 'fc'"}, {'XXX TODO XXX':
    'np.isfinite(_safe_accumulator_op(np.sum, y))'}]}, {'XXX TODO XXX':
    "y.dtype.kind in 'fc'"}, {'XXX TODO XXX':
    "y.dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'not _object_dtype_isnan(y).any()'}]}, {'description':
    "From /utils/multiclass.py:None:type_of_target, Exception: raise ValueError(     'Expected array-like (array or non-string sequence), got %r' % y) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'not': {'enum': [
    'prefit']}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(y, [Sequence, spmatrix])'}, {'XXX TODO XXX':
    "hasattr(y, '__array__')"}]}, {'type': 'object', 'properties': {'y': {
    'not': {'type': 'string'}}}}]}]}, {'description':
    'From /utils/multiclass.py:None:type_of_target, Exception: raise ValueError("y cannot be class \'SparseSeries\' or \'SparseArray\'") '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'not': {'enum': [
    'prefit']}}}}, {'XXX TODO XXX':
    "y.__class__.__name__ not in ['SparseSeries', 'SparseArray']"}]}, {
    'description':
    "From /utils/multiclass.py:None:type_of_target, Exception: raise ValueError(     'You appear to be using a legacy multi-label data representation. Sequence of sequences are no longer supported; use a binary array or sparse matrix instead - the MultiLabelBinarizer transformer can convert to this format.'     ) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'not': {'enum': [
    'prefit']}}}}, {'XXX TODO XXX': 'is_multilabel(y)'}, {'XXX TODO XXX':
    "hasattr(y[0], '__array__')"}, {'XXX TODO XXX':
    'isinstance(y[0], Sequence)'}, {'XXX TODO XXX': 'isinstance(y[0], str)'
    }]}, {'description':
    'From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'not': {'enum': [
    'prefit']}}}}, {'XXX TODO XXX': 'isinstance(y, list)'}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "hasattr(getattr(y, 'dtype', None), 'kind')"
    }, {'allOf': [{'XXX TODO XXX': "hasattr(y, 'dtypes')"}, {'XXX TODO XXX':
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
    'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'not': {'enum': [
    'prefit']}}}}, {'XXX TODO XXX': 'isinstance(y, list)'}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "not hasattr(y, 'sparse')"}, {'XXX TODO XXX':
    'y.ndim <= 1'}, {'type': 'object', 'laleNot': 'X/isSparse'}, {
    'XXX TODO XXX': "not hasattr(y.sparse.to_coo(), 'dtype')"}, {
    'XXX TODO XXX': 'y.sparse.to_coo().dtype is None'}, {'XXX TODO XXX':
    "not hasattr(y.sparse.to_coo().dtype, 'kind')"}, {'XXX TODO XXX':
    "y.sparse.to_coo().dtype.kind != 'c'"}]}, {'anyOf': [{'allOf': [{
    'XXX TODO XXX': "hasattr(y, 'sparse')"}, {'XXX TODO XXX': 'y.ndim > 1'}
    ]}, {'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(y, 'dtype')"}, {'XXX TODO XXX': 'y.dtype is None'}, {
    'XXX TODO XXX': "not hasattr(y.dtype, 'kind')"}, {'XXX TODO XXX':
    "y.dtype.kind != 'c'"}]}]}]}, {'description':
    'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'not': {'enum': [
    'prefit']}}}}, {'XXX TODO XXX': 'isinstance(y, list)'}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "hasattr(getattr(y, 'dtype', None), 'kind')"
    }, {'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(y, 'dtypes')"},
    {'XXX TODO XXX': "not hasattr(y.dtypes, '__array__')"}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX':
    'not all((False for None in list(y.dtypes)))'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(y, 'sparse')"}, {'XXX TODO XXX':
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
    "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Pandas DataFrame with mixed sparse extension arrays generated a sparse matrix with object dtype which can not be converted to a scipy sparse matrix.Sparse extension arrays should all have the same numeric type.'     ) "
    , 'allOf': [{'anyOf': [{'type': 'object', 'properties': {
    'base_estimator': {'not': {'enum': [None]}}}}, {'type': 'object',
    'properties': {'cv': {'not': {'enum': ['prefit']}}}}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': 'isinstance(self.base_estimator, Pipeline)'},
    {'XXX TODO XXX': 'isinstance(y, list)'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "hasattr(getattr(y, 'dtype', None), 'kind')"}, {'allOf':
    [{'XXX TODO XXX': "hasattr(y, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(y.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(y, 'sparse')"}, {'XXX TODO XXX': 'y.ndim <= 1'}, {
    'XXX TODO XXX': "y.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in y.dtypes])) <= 1'}]
    }, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(y, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(y, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(y.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(y, 'sparse')"}, {'XXX TODO XXX': 'y.ndim <= 1'}, {
    'XXX TODO XXX': "y.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in y.dtypes])) <= 1'}]
    }]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(self.base_estimator, Pipeline)'}, {'XXX TODO XXX':
    'isinstance(y, list)'}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(y, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(y, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(y.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(y, 'sparse')"}, {'XXX TODO XXX': 'y.ndim <= 1'}, {
    'XXX TODO XXX': "y.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in y.dtypes])) <= 1'}]
    }, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(y, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(y, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(y.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(y, 'sparse')"}, {'XXX TODO XXX': 'y.ndim <= 1'}, {
    'XXX TODO XXX': "y.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in y.dtypes])) <= 1'}]
    }]}]}]}]}, {'anyOf': [{'type': 'object', 'properties': {
    'base_estimator': {'enum': [None]}}}, {'type': 'object', 'properties':
    {'cv': {'not': {'enum': ['prefit']}}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'isinstance(self.base_estimator, Pipeline)'}, {
    'XXX TODO XXX': 'isinstance(y, list)'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "hasattr(getattr(y, 'dtype', None), 'kind')"}, {'allOf':
    [{'XXX TODO XXX': "hasattr(y, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(y.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(y, 'sparse')"}, {'XXX TODO XXX': 'y.ndim <= 1'}, {
    'XXX TODO XXX': "y.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in y.dtypes])) <= 1'}]
    }, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(y, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(y, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(y.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(y, 'sparse')"}, {'XXX TODO XXX': 'y.ndim <= 1'}, {
    'XXX TODO XXX': "y.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in y.dtypes])) <= 1'}]
    }]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(self.base_estimator, Pipeline)'}, {'XXX TODO XXX':
    'isinstance(y, list)'}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(y, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(y, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(y.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(y, 'sparse')"}, {'XXX TODO XXX': 'y.ndim <= 1'}, {
    'XXX TODO XXX': "y.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in y.dtypes])) <= 1'}]
    }, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(y, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(y, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(y.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(y, 'sparse')"}, {'XXX TODO XXX': 'y.ndim <= 1'}, {
    'XXX TODO XXX': "y.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in y.dtypes])) <= 1'}]
    }]}]}]}]}]}, {'description':
    'From /utils/validation.py:None:check_array, Exception: raise ValueError("""Complex data not supported {} """.format(array)     ) from complex_warning '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'not': {'enum': [
    'prefit']}}}}, {'XXX TODO XXX': 'isinstance(y, list)'}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "not hasattr(y, 'sparse')"}, {'XXX TODO XXX':
    'y.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(y.sparse.to_coo())'}]}, {
    'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(y, 'sparse')"}, {
    'XXX TODO XXX': 'y.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(y)'}]}]}
    ]}, {'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError('Found array with dim %d. %s expected <= 2.' % (array.ndim,     estimator_name)) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'not': {'enum': [
    'prefit']}}}}, {'XXX TODO XXX': 'isinstance(y, list)'}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "hasattr(getattr(y, 'dtype', None), 'kind')"
    }, {'allOf': [{'XXX TODO XXX': "hasattr(y, 'dtypes')"}, {'XXX TODO XXX':
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
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'not': {'enum': [
    'prefit']}}}}, {'XXX TODO XXX': 'isinstance(y, list)'}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "hasattr(getattr(y, 'dtype', None), 'kind')"
    }, {'allOf': [{'XXX TODO XXX': "hasattr(y, 'dtypes')"}, {'XXX TODO XXX':
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
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'not': {'enum': [
    'prefit']}}}}, {'XXX TODO XXX': 'isinstance(y, list)'}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "hasattr(getattr(y, 'dtype', None), 'kind')"
    }, {'allOf': [{'XXX TODO XXX': "hasattr(y, 'dtypes')"}, {'XXX TODO XXX':
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
    "From /utils/validation.py:None:column_or_1d, Exception: raise ValueError('y should be a 1d array, got an array of shape {} instead.'     .format(shape)) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'not': {'enum': [
    'prefit']}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "type_of_target(y) != 'binary'"}, {'XXX TODO XXX':
    'len(self.base_estimator.classes_) == 1'}, {'allOf': [{'XXX TODO XXX':
    'len(np.asarray(self.base_estimator.classes_)) < 3'}, {'XXX TODO XXX':
    "type_of_target(y) not in ['binary', 'multiclass']"}]}]}, {'anyOf': [{
    'XXX TODO XXX': "type_of_target(y) == 'binary'"}, {'XXX TODO XXX':
    "type_of_target(y) not in ['binary', 'multiclass']"}]}]}]}, {
    'description':
    "From /preprocessing/_label.py:None:label_binarize, Exception: raise ValueError('y has 0 samples: %r' % y) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'not': {'enum': [
    'prefit']}}}}, {'XXX TODO XXX': 'isinstance(y, list)'}, {'XXX TODO XXX':
    '_num_samples(y) != 0'}]}, {'description':
    "From /preprocessing/_label.py:None:label_binarize, Exception: raise ValueError(     'Multioutput target data is not supported with label binarization') "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'not': {'enum': [
    'prefit']}}}}, {'XXX TODO XXX':
    "'multioutput' not in type_of_target(y)"}]}, {'description':
    "From /preprocessing/_label.py:None:label_binarize, Exception: raise ValueError('The type of target data is not known') "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'not': {'enum': [
    'prefit']}}}}, {'XXX TODO XXX': "type_of_target(y) != 'unknown'"}]}, {
    'description':
    "From /preprocessing/_label.py:None:label_binarize, Exception: raise ValueError('classes {0} mismatch with the labels {1} found in the data'     .format(classes, unique_labels(y))) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'not': {'enum': [
    'prefit']}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "type_of_target(y) != 'binary'"}, {'XXX TODO XXX':
    'len(self.base_estimator.classes_) == 1'}, {'XXX TODO XXX':
    'len(np.asarray(self.base_estimator.classes_)) >= 3'}, {'XXX TODO XXX':
    "type_of_target(y) != 'multilabel-indicator'"}, {'XXX TODO XXX':
    "np.asarray(self.base_estimator.classes_).size == (y.shape[1] if hasattr(y, 'shape') else len(y[0]))"
    }]}, {'anyOf': [{'XXX TODO XXX': "type_of_target(y) == 'binary'"}, {
    'XXX TODO XXX': "type_of_target(y) != 'multilabel-indicator'"}, {
    'XXX TODO XXX':
    "np.asarray(self.base_estimator.classes_).size == (y.shape[1] if hasattr(y, 'shape') else len(y[0]))"
    }]}]}]}, {'description':
    "From /preprocessing/_label.py:None:label_binarize, Exception: raise ValueError('%s target data is not supported with label binarization' %     y_type) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'not': {'enum': [
    'prefit']}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "type_of_target(y) != 'binary'"}, {'XXX TODO XXX':
    'len(self.base_estimator.classes_) == 1'}, {'XXX TODO XXX':
    'len(np.asarray(self.base_estimator.classes_)) >= 3'}, {'XXX TODO XXX':
    "type_of_target(y) in ['binary', 'multiclass']"}, {'XXX TODO XXX':
    "type_of_target(y) == 'multilabel-indicator'"}]}, {'anyOf': [{
    'XXX TODO XXX': "type_of_target(y) == 'binary'"}, {'XXX TODO XXX':
    "type_of_target(y) in ['binary', 'multiclass']"}, {'XXX TODO XXX':
    "type_of_target(y) == 'multilabel-indicator'"}]}]}]}, {'description':
    'From /calibration.py:None:_fit_calibrator, Exception: raise ValueError(     f"\'method\' should be one of: \'sigmoid\' or \'isotonic\'. Got {method}.") '
    , 'allOf': [{'anyOf': [{'type': 'object', 'properties': {
    'base_estimator': {'not': {'enum': [None]}}}}, {'type': 'object',
    'properties': {'cv': {'not': {'enum': ['prefit']}}}}, {'XXX TODO XXX':
    '[class_idx, this_pred] not in zip(LabelEncoder().fit(self.base_estimator.classes_).transform(LinearSVC(random_state=0).classes_), _compute_predictions(_get_prediction_method(LinearSVC(random_state=0)), X, len(self.base_estimator.classes_)).T)'
    }, {'type': 'object', 'properties': {'method': {'enum': ['isotonic']}}},
    {'type': 'object', 'properties': {'method': {'enum': ['sigmoid']}}}]},
    {'anyOf': [{'type': 'object', 'properties': {'base_estimator': {'enum':
    [None]}}}, {'type': 'object', 'properties': {'cv': {'not': {'enum': [
    'prefit']}}}}, {'XXX TODO XXX':
    '[class_idx, this_pred] not in zip(LabelEncoder().fit(self.base_estimator.classes_).transform(self.base_estimator.classes_), _compute_predictions(_get_prediction_method(self.base_estimator), X, len(self.base_estimator.classes_)).T)'
    }, {'type': 'object', 'properties': {'method': {'enum': ['isotonic']}}},
    {'type': 'object', 'properties': {'method': {'enum': ['sigmoid']}}}]}]},
    {'description':
    'From /utils/validation.py:None:_assert_all_finite, Exception: raise ValueError(msg_err.format(type_err, msg_dtype if msg_dtype is not     None else X.dtype)) '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'ensemble': {'enum': [True]}}},
    {'XXX TODO XXX': 'is_multilabel(y)'}, {'XXX TODO XXX': 'y.ndim > 2'}, {
    'allOf': [{'XXX TODO XXX': 'y.dtype == object'}, {'XXX TODO XXX':
    'len(y)'}, {'XXX TODO XXX': 'isinstance(y.flat[0], str)'}]}, {'allOf':
    [{'XXX TODO XXX': 'y.ndim == 2'}, {'XXX TODO XXX': 'y.shape[1] == 0'}]},
    {'XXX TODO XXX': "y.dtype.kind != 'f'"}, {'XXX TODO XXX':
    'not np.any(y != y.astype(int))'}, {'XXX TODO XXX':
    "_get_config()['assume_finite']"}, {'allOf': [{'XXX TODO XXX':
    "y.dtype.kind in 'fc'"}, {'XXX TODO XXX':
    'np.isfinite(_safe_accumulator_op(np.sum, y))'}]}, {'XXX TODO XXX':
    "y.dtype.kind not in 'fc'"}, {'XXX TODO XXX': 'np.isfinite(y).all()'}]},
    {'description':
    "From /utils/validation.py:None:_assert_all_finite, Exception: raise ValueError('Input contains NaN') "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'ensemble': {'enum': [True]}}},
    {'XXX TODO XXX': 'is_multilabel(y)'}, {'XXX TODO XXX': 'y.ndim > 2'}, {
    'allOf': [{'XXX TODO XXX': 'y.dtype == object'}, {'XXX TODO XXX':
    'len(y)'}, {'XXX TODO XXX': 'isinstance(y.flat[0], str)'}]}, {'allOf':
    [{'XXX TODO XXX': 'y.ndim == 2'}, {'XXX TODO XXX': 'y.shape[1] == 0'}]},
    {'XXX TODO XXX': "y.dtype.kind != 'f'"}, {'XXX TODO XXX':
    'not np.any(y != y.astype(int))'}, {'XXX TODO XXX':
    "_get_config()['assume_finite']"}, {'allOf': [{'XXX TODO XXX':
    "y.dtype.kind in 'fc'"}, {'XXX TODO XXX':
    'np.isfinite(_safe_accumulator_op(np.sum, y))'}]}, {'XXX TODO XXX':
    "y.dtype.kind in 'fc'"}, {'XXX TODO XXX':
    "y.dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'not _object_dtype_isnan(y).any()'}]}, {'description':
    "From /utils/multiclass.py:None:type_of_target, Exception: raise ValueError(     'Expected array-like (array or non-string sequence), got %r' % y) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'ensemble': {'enum': [True]}}},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(y, [Sequence, spmatrix])'}, {'XXX TODO XXX':
    "hasattr(y, '__array__')"}]}, {'type': 'object', 'properties': {'y': {
    'not': {'type': 'string'}}}}]}]}, {'description':
    'From /utils/multiclass.py:None:type_of_target, Exception: raise ValueError("y cannot be class \'SparseSeries\' or \'SparseArray\'") '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'ensemble': {'enum': [True]}}},
    {'XXX TODO XXX':
    "y.__class__.__name__ not in ['SparseSeries', 'SparseArray']"}]}, {
    'description':
    "From /utils/multiclass.py:None:type_of_target, Exception: raise ValueError(     'You appear to be using a legacy multi-label data representation. Sequence of sequences are no longer supported; use a binary array or sparse matrix instead - the MultiLabelBinarizer transformer can convert to this format.'     ) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'ensemble': {'enum': [True]}}},
    {'XXX TODO XXX': 'is_multilabel(y)'}, {'XXX TODO XXX':
    "hasattr(y[0], '__array__')"}, {'XXX TODO XXX':
    'isinstance(y[0], Sequence)'}, {'XXX TODO XXX': 'isinstance(y[0], str)'
    }]}, {'description':
    'From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'ensemble': {'enum': [True]}}},
    {'XXX TODO XXX': 'isinstance(y, list)'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "hasattr(getattr(y, 'dtype', None), 'kind')"}, {'allOf':
    [{'XXX TODO XXX': "hasattr(y, 'dtypes')"}, {'XXX TODO XXX':
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
    'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'ensemble': {'enum': [True]}}},
    {'XXX TODO XXX': 'isinstance(y, list)'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(y, 'sparse')"}, {'XXX TODO XXX':
    'y.ndim <= 1'}, {'type': 'object', 'laleNot': 'X/isSparse'}, {
    'XXX TODO XXX': "not hasattr(y.sparse.to_coo(), 'dtype')"}, {
    'XXX TODO XXX': 'y.sparse.to_coo().dtype is None'}, {'XXX TODO XXX':
    "not hasattr(y.sparse.to_coo().dtype, 'kind')"}, {'XXX TODO XXX':
    "y.sparse.to_coo().dtype.kind != 'c'"}]}, {'anyOf': [{'allOf': [{
    'XXX TODO XXX': "hasattr(y, 'sparse')"}, {'XXX TODO XXX': 'y.ndim > 1'}
    ]}, {'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(y, 'dtype')"}, {'XXX TODO XXX': 'y.dtype is None'}, {
    'XXX TODO XXX': "not hasattr(y.dtype, 'kind')"}, {'XXX TODO XXX':
    "y.dtype.kind != 'c'"}]}]}]}, {'description':
    'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'ensemble': {'enum': [True]}}},
    {'XXX TODO XXX': 'isinstance(y, list)'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "hasattr(getattr(y, 'dtype', None), 'kind')"}, {'allOf':
    [{'anyOf': [{'XXX TODO XXX': "not hasattr(y, 'dtypes')"}, {
    'XXX TODO XXX': "not hasattr(y.dtypes, '__array__')"}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX':
    'not all((False for None in list(y.dtypes)))'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(y, 'sparse')"}, {'XXX TODO XXX':
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
    'From /utils/validation.py:None:check_array, Exception: raise ValueError("""Complex data not supported {} """.format(array)     ) from complex_warning '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'ensemble': {'enum': [True]}}},
    {'XXX TODO XXX': 'isinstance(y, list)'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(y, 'sparse')"}, {'XXX TODO XXX':
    'y.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(y.sparse.to_coo())'}]}, {
    'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(y, 'sparse')"}, {
    'XXX TODO XXX': 'y.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(y)'}]}]}
    ]}, {'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError('Found array with dim %d. %s expected <= 2.' % (array.ndim,     estimator_name)) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'ensemble': {'enum': [True]}}},
    {'XXX TODO XXX': 'isinstance(y, list)'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "hasattr(getattr(y, 'dtype', None), 'kind')"}, {'allOf':
    [{'XXX TODO XXX': "hasattr(y, 'dtypes')"}, {'XXX TODO XXX':
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
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'ensemble': {'enum': [True]}}},
    {'XXX TODO XXX': 'isinstance(y, list)'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "hasattr(getattr(y, 'dtype', None), 'kind')"}, {'allOf':
    [{'XXX TODO XXX': "hasattr(y, 'dtypes')"}, {'XXX TODO XXX':
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
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'ensemble': {'enum': [True]}}},
    {'XXX TODO XXX': 'isinstance(y, list)'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "hasattr(getattr(y, 'dtype', None), 'kind')"}, {'allOf':
    [{'XXX TODO XXX': "hasattr(y, 'dtypes')"}, {'XXX TODO XXX':
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
    "From /utils/validation.py:None:column_or_1d, Exception: raise ValueError('y should be a 1d array, got an array of shape {} instead.'     .format(shape)) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'ensemble': {'enum': [True]}}},
    {'allOf': [{'anyOf': [{'XXX TODO XXX': "type_of_target(y) != 'binary'"},
    {'XXX TODO XXX': 'len(LabelEncoder().fit(y).classes_) == 1'}, {'allOf':
    [{'XXX TODO XXX': 'len(np.asarray(LabelEncoder().fit(y).classes_)) < 3'
    }, {'XXX TODO XXX': "type_of_target(y) not in ['binary', 'multiclass']"
    }]}]}, {'anyOf': [{'XXX TODO XXX': "type_of_target(y) == 'binary'"}, {
    'XXX TODO XXX': "type_of_target(y) not in ['binary', 'multiclass']"}]}]
    }]}, {'description':
    "From /preprocessing/_label.py:None:label_binarize, Exception: raise ValueError('y has 0 samples: %r' % y) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'ensemble': {'enum': [True]}}},
    {'XXX TODO XXX': 'isinstance(y, list)'}, {'XXX TODO XXX':
    '_num_samples(y) != 0'}]}, {'description':
    "From /preprocessing/_label.py:None:label_binarize, Exception: raise ValueError(     'Multioutput target data is not supported with label binarization') "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'ensemble': {'enum': [True]}}},
    {'XXX TODO XXX': "'multioutput' not in type_of_target(y)"}]}, {
    'description':
    "From /preprocessing/_label.py:None:label_binarize, Exception: raise ValueError('The type of target data is not known') "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'ensemble': {'enum': [True]}}},
    {'XXX TODO XXX': "type_of_target(y) != 'unknown'"}]}, {'description':
    "From /preprocessing/_label.py:None:label_binarize, Exception: raise ValueError('classes {0} mismatch with the labels {1} found in the data'     .format(classes, unique_labels(y))) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'ensemble': {'enum': [True]}}},
    {'allOf': [{'anyOf': [{'XXX TODO XXX': "type_of_target(y) != 'binary'"},
    {'XXX TODO XXX': 'len(LabelEncoder().fit(y).classes_) == 1'}, {
    'XXX TODO XXX': 'len(np.asarray(LabelEncoder().fit(y).classes_)) >= 3'},
    {'XXX TODO XXX': "type_of_target(y) != 'multilabel-indicator'"}, {
    'XXX TODO XXX':
    "np.asarray(LabelEncoder().fit(y).classes_).size == (y.shape[1] if hasattr(y, 'shape') else len(y[0]))"
    }]}, {'anyOf': [{'XXX TODO XXX': "type_of_target(y) == 'binary'"}, {
    'XXX TODO XXX': "type_of_target(y) != 'multilabel-indicator'"}, {
    'XXX TODO XXX':
    "np.asarray(LabelEncoder().fit(y).classes_).size == (y.shape[1] if hasattr(y, 'shape') else len(y[0]))"
    }]}]}]}, {'description':
    "From /preprocessing/_label.py:None:label_binarize, Exception: raise ValueError('%s target data is not supported with label binarization' %     y_type) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'ensemble': {'enum': [True]}}},
    {'allOf': [{'anyOf': [{'XXX TODO XXX': "type_of_target(y) != 'binary'"},
    {'XXX TODO XXX': 'len(LabelEncoder().fit(y).classes_) == 1'}, {
    'XXX TODO XXX': 'len(np.asarray(LabelEncoder().fit(y).classes_)) >= 3'},
    {'XXX TODO XXX': "type_of_target(y) in ['binary', 'multiclass']"}, {
    'XXX TODO XXX': "type_of_target(y) == 'multilabel-indicator'"}]}, {
    'anyOf': [{'XXX TODO XXX': "type_of_target(y) == 'binary'"}, {
    'XXX TODO XXX': "type_of_target(y) in ['binary', 'multiclass']"}, {
    'XXX TODO XXX': "type_of_target(y) == 'multilabel-indicator'"}]}]}]}, {
    'description':
    'From /calibration.py:None:_fit_calibrator, Exception: raise ValueError(     f"\'method\' should be one of: \'sigmoid\' or \'isotonic\'. Got {method}.") '
    , 'allOf': [{'anyOf': [{'type': 'object', 'properties': {
    'base_estimator': {'not': {'enum': [None]}}}}, {'type': 'object',
    'properties': {'cv': {'enum': ['prefit']}}}, {'type': 'object',
    'properties': {'ensemble': {'enum': [True]}}}, {'XXX TODO XXX':
    '[class_idx, this_pred] not in zip(LabelEncoder().fit(LabelEncoder().fit(y).classes_).transform(clone(LinearSVC(random_state=0)).classes_), _compute_predictions(partial(cross_val_predict, estimator=clone(LinearSVC(random_state=0)), X=X, y=y, cv=check_cv(self.cv, y, True), method=_get_prediction_method(clone(LinearSVC(random_state=0))).__name__, n_jobs=self.n_jobs), X, len(LabelEncoder().fit(y).classes_)).T)'
    }, {'type': 'object', 'properties': {'method': {'enum': ['isotonic']}}},
    {'type': 'object', 'properties': {'method': {'enum': ['sigmoid']}}}]},
    {'anyOf': [{'type': 'object', 'properties': {'base_estimator': {'enum':
    [None]}}}, {'type': 'object', 'properties': {'cv': {'enum': ['prefit']}
    }}, {'type': 'object', 'properties': {'ensemble': {'enum': [True]}}}, {
    'XXX TODO XXX':
    '[class_idx, this_pred] not in zip(LabelEncoder().fit(LabelEncoder().fit(y).classes_).transform(clone(self.base_estimator).classes_), _compute_predictions(partial(cross_val_predict, estimator=clone(self.base_estimator), X=X, y=y, cv=check_cv(self.cv, y, True), method=_get_prediction_method(clone(self.base_estimator)).__name__, n_jobs=self.n_jobs), X, len(LabelEncoder().fit(y).classes_)).T)'
    }, {'type': 'object', 'properties': {'method': {'enum': ['isotonic']}}},
    {'type': 'object', 'properties': {'method': {'enum': ['sigmoid']}}}]}]},
    {'description':
    'From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'not': {'enum': [None]}}}},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf':
    [{'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {
    'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).fit)'
    }]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'
    }}}}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=np.float64).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, dtype=np.float64).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=np.float64), 'fit')"}, {
    'XXX TODO XXX':
    'not callable(np.asarray(X, None, dtype=np.float64).fit)'}]}]}]}]}]}]}]
    }, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).astype(np.float64).fit)"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).fit)"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'},
    {'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).fit)'
    }]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).astype(np.float64).fit)"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).fit)"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'},
    {'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=dtype[0]).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, dtype=dtype[0]).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'fit')"}, {
    'XXX TODO XXX': 'not callable(np.asarray(X, None, dtype=dtype[0]).fit)'
    }]}]}]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).astype(np.float64).fit)"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).fit)"
    }]}]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=numeric).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=numeric).fit)'}
    ]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'enum': [None]}}}, {
    'XXX TODO XXX': "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X, None).astype(numeric, casting='unsafe', False).astype(np.float64).fit)"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X, None).astype(numeric, casting='unsafe', False).fit)"
    }]}]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, dtype=numeric).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric), 'fit')"}, {
    'XXX TODO XXX': 'not callable(np.asarray(X, None, dtype=numeric).fit)'}
    ]}]}]}]}]}]}]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf':
    [{'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {
    'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).fit)'
    }]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'
    }}}}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=np.float64).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, dtype=np.float64).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=np.float64), 'fit')"}, {
    'XXX TODO XXX':
    'not callable(np.asarray(X, None, dtype=np.float64).fit)'}]}]}]}]}]}]}]
    }, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) not in numeric"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], None, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], None, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind not in 'OUSV'"},
    {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, None).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, None).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'fit')"}, {
    'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, None).fit)'}]}]}]}]}]
    }, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], None, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], None, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'
    }}}}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, None).dtype.kind not in 'OUSV'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, None).astype(np.float64), 'fit')"}, {
    'XXX TODO XXX':
    'not callable(np.asarray(X, None, None).astype(np.float64).fit)'}]}, {
    'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, None).dtype.kind in 'OUSV'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, None), 'fit')"}, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, None).fit)'}]}]}]}]}]}]}]}, {'anyOf':
    [{'allOf': [{'XXX TODO XXX': "getattr(X, 'dtype', None) is not None"},
    {'XXX TODO XXX': "getattr(X, 'dtype', None) in numeric"}]}, {'allOf': [
    {'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object',
    'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).astype(np.float64).fit)"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).fit)"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'},
    {'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).fit)'
    }]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).astype(np.float64).fit)"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).fit)"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'},
    {'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=dtype[0]).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, dtype=dtype[0]).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'fit')"}, {
    'XXX TODO XXX': 'not callable(np.asarray(X, None, dtype=dtype[0]).fit)'
    }]}]}]}]}]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).astype(np.float64).fit)"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).fit)"
    }]}]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=numeric).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=numeric).fit)'}
    ]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'enum': [None]}}}, {
    'XXX TODO XXX': "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X, None).astype(numeric, casting='unsafe', False).astype(np.float64).fit)"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X, None).astype(numeric, casting='unsafe', False).fit)"
    }]}]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, dtype=numeric).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric), 'fit')"}, {
    'XXX TODO XXX': 'not callable(np.asarray(X, None, dtype=numeric).fit)'}
    ]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}, {'description':
    'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'not': {'enum': [None]}}}},
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
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'not': {'enum': [None]}}}},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "not hasattr(X.dtypes, '__array__')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX':
    'not all((isinstance(numeric, np.dtype) for numeric in list(X.dtypes)))'
    }, {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
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
    'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'np.result_type(*list(X.dtypes)) is None'}, {
    'XXX TODO XXX': 'np.result_type(*list(X.dtypes)) not in numeric'}, {
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
    'np.result_type(*list(X.dtypes)) in numeric'}]}, {'allOf': [{'anyOf': [
    {'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
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
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric).dtype, 'kind')"}, {
    'XXX TODO XXX': "np.asarray(X, None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'all((isinstance(numeric, np.dtype) for numeric in list(X.dtypes)))'},
    {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
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
    'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
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
    }]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric).dtype, 'kind')"}, {
    'XXX TODO XXX': "np.asarray(X, None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}]}]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'XXX TODO XXX':
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
    'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
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
    }]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric).dtype, 'kind')"}, {
    'XXX TODO XXX': "np.asarray(X, None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}]}]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': "not hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "not hasattr(X.dtypes, '__array__')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX':
    'not all((isinstance(numeric, np.dtype) for numeric in list(X.dtypes)))'
    }, {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
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
    'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'np.result_type(*list(X.dtypes)) is None'}, {
    'XXX TODO XXX': 'np.result_type(*list(X.dtypes)) not in numeric'}, {
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
    'np.result_type(*list(X.dtypes)) in numeric'}]}, {'allOf': [{'anyOf': [
    {'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
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
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric).dtype, 'kind')"}, {
    'XXX TODO XXX': "np.asarray(X, None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'all((isinstance(numeric, np.dtype) for numeric in list(X.dtypes)))'},
    {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
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
    'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) not in numeric"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
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
    {'XXX TODO XXX': "np.asarray(X, None, None).dtype.kind != 'c'"}]}]}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "getattr(X, 'dtype', None) is not None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) in numeric"}]}, {'allOf': [{'anyOf': [{
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
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric).dtype, 'kind')"}, {
    'XXX TODO XXX': "np.asarray(X, None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}]}]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'XXX TODO XXX':
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
    'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) not in numeric"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
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
    {'XXX TODO XXX': "np.asarray(X, None, None).dtype.kind != 'c'"}]}]}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "getattr(X, 'dtype', None) is not None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) in numeric"}]}, {'allOf': [{'anyOf': [{
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
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric).dtype, 'kind')"}, {
    'XXX TODO XXX': "np.asarray(X, None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}]}]}]}]}]}]}]}]}]}]}, {'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Pandas DataFrame with mixed sparse extension arrays generated a sparse matrix with object dtype which can not be converted to a scipy sparse matrix.Sparse extension arrays should all have the same numeric type.'     ) "
    , 'allOf': [{'anyOf': [{'type': 'object', 'properties': {
    'base_estimator': {'not': {'enum': [None]}}}}, {'type': 'object',
    'properties': {'cv': {'enum': ['prefit']}}}, {'type': 'object',
    'properties': {'y': {'not': {'enum': [None]}}}}, {'allOf': [{'anyOf': [
    {'XXX TODO XXX': "not self._get_tags()['requires_y']"}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "hasattr(getattr(X, 'dtype', None), 'kind')"
    }, {'allOf': [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}, {'anyOf': [{
    'allOf': [{'type': 'object', 'properties': {'numeric': {'type':
    'string'}}}, {'type': 'object', 'properties': {'numeric': {'enum': [
    'numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }, {'anyOf': [{'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'}, {
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}]}]}]}]}, {
    'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
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
    }]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'type': 'string'}}}, {'type': 'object', 'properties': {
    'numeric': {'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {
    'XXX TODO XXX': "getattr(X, 'dtype', None) not in numeric"}, {
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}, {'anyOf': [{
    'allOf': [{'XXX TODO XXX': "getattr(X, 'dtype', None) is not None"}, {
    'XXX TODO XXX': "getattr(X, 'dtype', None) in numeric"}]}, {
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}]}]}, {'anyOf':
    [{'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'}, {
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}]}]}]}]}]}]}, {
    'anyOf': [{'XXX TODO XXX': "self._get_tags()['requires_y']"}, {'allOf':
    [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}, {'anyOf': [{
    'allOf': [{'type': 'object', 'properties': {'numeric': {'type':
    'string'}}}, {'type': 'object', 'properties': {'numeric': {'enum': [
    'numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }, {'anyOf': [{'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'}, {
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}]}]}]}]}, {
    'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
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
    }]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'type': 'string'}}}, {'type': 'object', 'properties': {
    'numeric': {'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {
    'XXX TODO XXX': "getattr(X, 'dtype', None) not in numeric"}, {
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}, {'anyOf': [{
    'allOf': [{'XXX TODO XXX': "getattr(X, 'dtype', None) is not None"}, {
    'XXX TODO XXX': "getattr(X, 'dtype', None) in numeric"}]}, {
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}]}]}, {'anyOf':
    [{'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'}, {
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}]}]}]}]}]}]}]}]
    }, {'anyOf': [{'type': 'object', 'properties': {'base_estimator': {
    'enum': [None]}}}, {'type': 'object', 'properties': {'cv': {'enum': [
    'prefit']}}}, {'type': 'object', 'properties': {'y': {'not': {'enum': [
    None]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not self._get_tags()['requires_y']"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf':
    [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}, {'anyOf': [{
    'allOf': [{'type': 'object', 'properties': {'numeric': {'type':
    'string'}}}, {'type': 'object', 'properties': {'numeric': {'enum': [
    'numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }, {'anyOf': [{'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'}, {
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}]}]}]}]}, {
    'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
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
    }]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'type': 'string'}}}, {'type': 'object', 'properties': {
    'numeric': {'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {
    'XXX TODO XXX': "getattr(X, 'dtype', None) not in numeric"}, {
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}, {'anyOf': [{
    'allOf': [{'XXX TODO XXX': "getattr(X, 'dtype', None) is not None"}, {
    'XXX TODO XXX': "getattr(X, 'dtype', None) in numeric"}]}, {
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}]}]}, {'anyOf':
    [{'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'}, {
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}]}]}]}]}]}]}, {
    'anyOf': [{'XXX TODO XXX': "self._get_tags()['requires_y']"}, {'allOf':
    [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}, {'anyOf': [{
    'allOf': [{'type': 'object', 'properties': {'numeric': {'type':
    'string'}}}, {'type': 'object', 'properties': {'numeric': {'enum': [
    'numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }, {'anyOf': [{'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'}, {
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}]}]}]}]}, {
    'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
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
    }]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'type': 'string'}}}, {'type': 'object', 'properties': {
    'numeric': {'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {
    'XXX TODO XXX': "getattr(X, 'dtype', None) not in numeric"}, {
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}, {'anyOf': [{
    'allOf': [{'XXX TODO XXX': "getattr(X, 'dtype', None) is not None"}, {
    'XXX TODO XXX': "getattr(X, 'dtype', None) in numeric"}]}, {
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}]}]}, {'anyOf':
    [{'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'}, {
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}]}]}]}]}]}]}]}]
    }]}, {'description':
    'From /utils/validation.py:None:check_array, Exception: raise ValueError("""Complex data not supported {} """.format(array)     ) from complex_warning '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'not': {'enum': [None]}}}},
    {'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}]}, {'anyOf': [{'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}
    ]}, {'XXX TODO XXX': 'sp.issparse(X)'}]}]}]}, {'description':
    'From /utils/validation.py:None:check_array, Exception: raise ValueError(     "Unable to convert array of bytes/strings into decimal numbers with dtype=\'numeric\'"     ) from e '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'not': {'enum': [None]}}}},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "not hasattr(X.dtypes, '__array__')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX':
    'not all((isinstance(numeric, np.dtype) for numeric in list(X.dtypes)))'
    }, {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}]}]}]},
    {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'np.result_type(*list(X.dtypes)) is None'}, {
    'XXX TODO XXX': 'np.result_type(*list(X.dtypes)) not in numeric'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind not in 'OUSV'"}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, None).dtype.kind not in 'OUSV'"}]}]}]}, {'anyOf':
    [{'allOf': [{'XXX TODO XXX':
    'np.result_type(*list(X.dtypes)) is not None'}, {'XXX TODO XXX':
    'np.result_type(*list(X.dtypes)) in numeric'}]}, {'allOf': [{'anyOf': [
    {'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}]}]}]}]}
    ]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}]}]}]}]}]
    }]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'all((isinstance(numeric, np.dtype) for numeric in list(X.dtypes)))'},
    {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}]}]}]},
    {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}]}]}]}]}
    ]}, {'anyOf': [{'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'},
    {'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}]}]}]}]}]
    }]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}]}]}]},
    {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}]}]}]}]}
    ]}, {'anyOf': [{'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'},
    {'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}]}]}]}]}]
    }]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': "not hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "not hasattr(X.dtypes, '__array__')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX':
    'not all((isinstance(numeric, np.dtype) for numeric in list(X.dtypes)))'
    }, {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}]}]}]},
    {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'np.result_type(*list(X.dtypes)) is None'}, {
    'XXX TODO XXX': 'np.result_type(*list(X.dtypes)) not in numeric'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind not in 'OUSV'"}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, None).dtype.kind not in 'OUSV'"}]}]}]}, {'anyOf':
    [{'allOf': [{'XXX TODO XXX':
    'np.result_type(*list(X.dtypes)) is not None'}, {'XXX TODO XXX':
    'np.result_type(*list(X.dtypes)) in numeric'}]}, {'allOf': [{'anyOf': [
    {'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}]}]}]}]}
    ]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}]}]}]}]}]
    }]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'all((isinstance(numeric, np.dtype) for numeric in list(X.dtypes)))'},
    {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}]}]}]},
    {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) not in numeric"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind not in 'OUSV'"}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, None).dtype.kind not in 'OUSV'"}]}]}]}, {'anyOf':
    [{'allOf': [{'XXX TODO XXX': "getattr(X, 'dtype', None) is not None"},
    {'XXX TODO XXX': "getattr(X, 'dtype', None) in numeric"}]}, {'allOf': [
    {'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}]}]}]}]}
    ]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}]}]}]}]}]
    }]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}]}]}]},
    {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) not in numeric"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind not in 'OUSV'"}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, None).dtype.kind not in 'OUSV'"}]}]}]}, {'anyOf':
    [{'allOf': [{'XXX TODO XXX': "getattr(X, 'dtype', None) is not None"},
    {'XXX TODO XXX': "getattr(X, 'dtype', None) in numeric"}]}, {'allOf': [
    {'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}]}]}]}]}
    ]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}]}]}]}]}]
    }]}]}]}]}]}]}]}]}, {'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Found array with %d sample(s) (shape=%s) while a minimum of %d is required%s.'      % (n_samples, array.shape, ensure_min_samples, context)) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'not': {'enum': [None]}}}},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf':
    [{'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {
    'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=np.float64)) >= 1'
    }]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'
    }}}}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=np.float64).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=np.float64)) >= 1'}]}]}]}]}]}]}
    ]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).astype(np.float64)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False)) >= 1"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'},
    {'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0])) >= 1'
    }]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "_num_samples(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).astype(np.float64)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "_num_samples(np.asarray(X, None).astype(dtype[0], casting='unsafe', False)) >= 1"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'},
    {'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=dtype[0]).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=dtype[0])) >= 1'}]}]}]}]}]}]}]}
    ]}]}, {'anyOf': [{'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'},
    {'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object',
    'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).astype(np.float64)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False)) >= 1"
    }]}]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=numeric).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=numeric)) >= 1'
    }]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'enum': [None]}}}, {
    'XXX TODO XXX': "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "_num_samples(np.asarray(X, None).astype(numeric, casting='unsafe', False).astype(np.float64)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "_num_samples(np.asarray(X, None).astype(numeric, casting='unsafe', False)) >= 1"
    }]}]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=numeric).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': '_num_samples(np.asarray(X, None, dtype=numeric)) >= 1'
    }]}]}]}]}]}]}]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf':
    [{'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {
    'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=np.float64)) >= 1'
    }]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'
    }}}}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=np.float64).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=np.float64)) >= 1'}]}]}]}]}]}]}
    ]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) not in numeric"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], None, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind not in 'OUSV'"},
    {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, None).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, None)) >= 1'}]}]}]}]}
    ]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], None, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'
    }}}}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, None).dtype.kind not in 'OUSV'"}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, None).astype(np.float64)) >= 1'}]}, {
    'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, None).dtype.kind in 'OUSV'"}]}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, None)) >= 1'}]}]}]}]}]}]}]}, {'anyOf':
    [{'allOf': [{'XXX TODO XXX': "getattr(X, 'dtype', None) is not None"},
    {'XXX TODO XXX': "getattr(X, 'dtype', None) in numeric"}]}, {'allOf': [
    {'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object',
    'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).astype(np.float64)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False)) >= 1"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'},
    {'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0])) >= 1'
    }]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "_num_samples(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).astype(np.float64)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "_num_samples(np.asarray(X, None).astype(dtype[0], casting='unsafe', False)) >= 1"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'},
    {'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=dtype[0]).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=dtype[0])) >= 1'}]}]}]}]}]}]}]}
    ]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).astype(np.float64)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False)) >= 1"
    }]}]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=numeric).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=numeric)) >= 1'
    }]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'enum': [None]}}}, {
    'XXX TODO XXX': "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "_num_samples(np.asarray(X, None).astype(numeric, casting='unsafe', False).astype(np.float64)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "_num_samples(np.asarray(X, None).astype(numeric, casting='unsafe', False)) >= 1"
    }]}]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=numeric).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': '_num_samples(np.asarray(X, None, dtype=numeric)) >= 1'
    }]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}, {'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Found array with %d feature(s) (shape=%s) while a minimum of %d is required%s.'      % (n_features, array.shape, ensure_min_features, context)) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'not': {'enum': [None]}}}},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf':
    [{'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {
    'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'
    }}}}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).ndim != 2'
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}, {'anyOf': [{'allOf':
    [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    'np.asarray(X, None, dtype=np.float64).astype(np.float64).ndim != 2'},
    {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}, {'anyOf': [{
    'allOf': [{'type': 'object', 'properties': {'numeric': {'type':
    'string'}}}, {'type': 'object', 'properties': {'numeric': {'enum': [
    'numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).astype(np.float64).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf':
    [{'XXX TODO XXX': 'dtype[0] is not None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).astype(np.float64).ndim != 2'
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}, {'anyOf': [{
    'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).astype(np.float64).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf':
    [{'XXX TODO XXX': 'dtype[0] is not None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    'np.asarray(X, None, dtype=dtype[0]).astype(np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{'type':
    'object', 'properties': {'numeric': {'type': 'string'}}}, {'type':
    'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=dtype[0]).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}]}]}, {'anyOf': [{
    'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'enum': [None]}}}, {
    'XXX TODO XXX': "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).astype(np.float64).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'enum': [None]}}
    }}, {'XXX TODO XXX': "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).astype(np.float64).ndim != 2'
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}, {'anyOf': [{
    'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).astype(np.float64).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'enum': [None]}}
    }}, {'XXX TODO XXX': "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    'np.asarray(X, None, dtype=numeric).astype(np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{'type':
    'object', 'properties': {'numeric': {'type': 'string'}}}, {'type':
    'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=numeric).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}]}]}]}]}]}]}, {
    'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf':
    [{'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {
    'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'
    }}}}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).ndim != 2'
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}, {'anyOf': [{'allOf':
    [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    'np.asarray(X, None, dtype=np.float64).astype(np.float64).ndim != 2'},
    {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}, {'anyOf': [{
    'allOf': [{'type': 'object', 'properties': {'numeric': {'type':
    'string'}}}, {'type': 'object', 'properties': {'numeric': {'enum': [
    'numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) not in numeric"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], None, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'
    }}}}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind not in 'OUSV'"},
    {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, None).astype(np.float64).ndim != 2'
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': 'np.asarray(X.sparse.to_coo(), None, None).ndim != 2'},
    {'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}, {'anyOf': [{'allOf':
    [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], None, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, None).dtype.kind not in 'OUSV'"}, {'XXX TODO XXX':
    'np.asarray(X, None, None).astype(np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{'type':
    'object', 'properties': {'numeric': {'type': 'string'}}}, {'type':
    'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX': "np.asarray(X, None, None).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': 'np.asarray(X, None, None).ndim != 2'}, {'XXX TODO XXX':
    'array.shape[1] >= 1'}]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is not None"}, {
    'XXX TODO XXX': "getattr(X, 'dtype', None) in numeric"}]}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).astype(np.float64).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf':
    [{'XXX TODO XXX': 'dtype[0] is not None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).astype(np.float64).ndim != 2'
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}, {'anyOf': [{
    'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).astype(np.float64).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf':
    [{'XXX TODO XXX': 'dtype[0] is not None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    'np.asarray(X, None, dtype=dtype[0]).astype(np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{'type':
    'object', 'properties': {'numeric': {'type': 'string'}}}, {'type':
    'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=dtype[0]).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}]}]}]}]}, {'anyOf':
    [{'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'enum': [None]}}}, {
    'XXX TODO XXX': "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).astype(np.float64).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'enum': [None]}}
    }}, {'XXX TODO XXX': "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).astype(np.float64).ndim != 2'
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}, {'anyOf': [{
    'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).astype(np.float64).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'enum': [None]}}
    }}, {'XXX TODO XXX': "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    'np.asarray(X, None, dtype=numeric).astype(np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{'type':
    'object', 'properties': {'numeric': {'type': 'string'}}}, {'type':
    'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=numeric).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}, {
    'description':
    'From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'enum': [None]}}}, {'type':
    'object', 'properties': {'y': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'y': {'not': {'enum': ['no_validation']}}}}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf':
    [{'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {
    'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).fit)'
    }]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'
    }}}}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=np.float64).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, dtype=np.float64).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=np.float64), 'fit')"}, {
    'XXX TODO XXX':
    'not callable(np.asarray(X, None, dtype=np.float64).fit)'}]}]}]}]}]}]}]
    }, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).astype(np.float64).fit)"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).fit)"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'},
    {'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).fit)'
    }]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).astype(np.float64).fit)"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).fit)"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'},
    {'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=dtype[0]).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, dtype=dtype[0]).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'fit')"}, {
    'XXX TODO XXX': 'not callable(np.asarray(X, None, dtype=dtype[0]).fit)'
    }]}]}]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).astype(np.float64).fit)"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).fit)"
    }]}]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=numeric).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=numeric).fit)'}
    ]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'enum': [None]}}}, {
    'XXX TODO XXX': "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X, None).astype(numeric, casting='unsafe', False).astype(np.float64).fit)"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X, None).astype(numeric, casting='unsafe', False).fit)"
    }]}]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, dtype=numeric).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric), 'fit')"}, {
    'XXX TODO XXX': 'not callable(np.asarray(X, None, dtype=numeric).fit)'}
    ]}]}]}]}]}]}]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf':
    [{'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {
    'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).fit)'
    }]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'
    }}}}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=np.float64).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, dtype=np.float64).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=np.float64), 'fit')"}, {
    'XXX TODO XXX':
    'not callable(np.asarray(X, None, dtype=np.float64).fit)'}]}]}]}]}]}]}]
    }, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) not in numeric"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], None, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], None, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind not in 'OUSV'"},
    {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, None).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, None).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'fit')"}, {
    'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, None).fit)'}]}]}]}]}]
    }, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], None, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], None, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'
    }}}}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, None).dtype.kind not in 'OUSV'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, None).astype(np.float64), 'fit')"}, {
    'XXX TODO XXX':
    'not callable(np.asarray(X, None, None).astype(np.float64).fit)'}]}, {
    'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, None).dtype.kind in 'OUSV'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, None), 'fit')"}, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, None).fit)'}]}]}]}]}]}]}]}, {'anyOf':
    [{'allOf': [{'XXX TODO XXX': "getattr(X, 'dtype', None) is not None"},
    {'XXX TODO XXX': "getattr(X, 'dtype', None) in numeric"}]}, {'allOf': [
    {'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object',
    'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).astype(np.float64).fit)"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).fit)"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'},
    {'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).fit)'
    }]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).astype(np.float64).fit)"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).fit)"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'},
    {'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=dtype[0]).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, dtype=dtype[0]).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'fit')"}, {
    'XXX TODO XXX': 'not callable(np.asarray(X, None, dtype=dtype[0]).fit)'
    }]}]}]}]}]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).astype(np.float64).fit)"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).fit)"
    }]}]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=numeric).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=numeric).fit)'}
    ]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'enum': [None]}}}, {
    'XXX TODO XXX': "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X, None).astype(numeric, casting='unsafe', False).astype(np.float64).fit)"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X, None).astype(numeric, casting='unsafe', False).fit)"
    }]}]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, dtype=numeric).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric), 'fit')"}, {
    'XXX TODO XXX': 'not callable(np.asarray(X, None, dtype=numeric).fit)'}
    ]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}, {'description':
    'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'enum': [None]}}}, {'type':
    'object', 'properties': {'y': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'y': {'not': {'enum': ['no_validation']}}}}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
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
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'enum': [None]}}}, {'type':
    'object', 'properties': {'y': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'y': {'not': {'enum': ['no_validation']}}}}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "not hasattr(X.dtypes, '__array__')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX':
    'not all((isinstance(numeric, np.dtype) for numeric in list(X.dtypes)))'
    }, {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
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
    'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'np.result_type(*list(X.dtypes)) is None'}, {
    'XXX TODO XXX': 'np.result_type(*list(X.dtypes)) not in numeric'}, {
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
    'np.result_type(*list(X.dtypes)) in numeric'}]}, {'allOf': [{'anyOf': [
    {'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
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
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric).dtype, 'kind')"}, {
    'XXX TODO XXX': "np.asarray(X, None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'all((isinstance(numeric, np.dtype) for numeric in list(X.dtypes)))'},
    {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
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
    'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
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
    }]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric).dtype, 'kind')"}, {
    'XXX TODO XXX': "np.asarray(X, None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}]}]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'XXX TODO XXX':
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
    'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
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
    }]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric).dtype, 'kind')"}, {
    'XXX TODO XXX': "np.asarray(X, None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}]}]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': "not hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "not hasattr(X.dtypes, '__array__')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX':
    'not all((isinstance(numeric, np.dtype) for numeric in list(X.dtypes)))'
    }, {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
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
    'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'np.result_type(*list(X.dtypes)) is None'}, {
    'XXX TODO XXX': 'np.result_type(*list(X.dtypes)) not in numeric'}, {
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
    'np.result_type(*list(X.dtypes)) in numeric'}]}, {'allOf': [{'anyOf': [
    {'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
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
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric).dtype, 'kind')"}, {
    'XXX TODO XXX': "np.asarray(X, None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'all((isinstance(numeric, np.dtype) for numeric in list(X.dtypes)))'},
    {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
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
    'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) not in numeric"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
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
    {'XXX TODO XXX': "np.asarray(X, None, None).dtype.kind != 'c'"}]}]}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "getattr(X, 'dtype', None) is not None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) in numeric"}]}, {'allOf': [{'anyOf': [{
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
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric).dtype, 'kind')"}, {
    'XXX TODO XXX': "np.asarray(X, None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}]}]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'XXX TODO XXX':
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
    'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) not in numeric"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
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
    {'XXX TODO XXX': "np.asarray(X, None, None).dtype.kind != 'c'"}]}]}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "getattr(X, 'dtype', None) is not None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) in numeric"}]}, {'allOf': [{'anyOf': [{
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
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric).dtype, 'kind')"}, {
    'XXX TODO XXX': "np.asarray(X, None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}]}]}]}]}]}]}]}]}]}]}, {'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Pandas DataFrame with mixed sparse extension arrays generated a sparse matrix with object dtype which can not be converted to a scipy sparse matrix.Sparse extension arrays should all have the same numeric type.'     ) "
    , 'allOf': [{'anyOf': [{'type': 'object', 'properties': {
    'base_estimator': {'not': {'enum': [None]}}}}, {'type': 'object',
    'properties': {'cv': {'enum': ['prefit']}}}, {'type': 'object',
    'properties': {'y': {'enum': [None]}}}, {'type': 'object', 'properties':
    {'y': {'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'y': {'not': {'enum': ['no_validation']}}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf':
    [{'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}, {'anyOf': [{
    'allOf': [{'type': 'object', 'properties': {'numeric': {'type':
    'string'}}}, {'type': 'object', 'properties': {'numeric': {'enum': [
    'numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }, {'anyOf': [{'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'}, {
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}]}]}]}]}, {
    'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
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
    }]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'type': 'string'}}}, {'type': 'object', 'properties': {
    'numeric': {'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {
    'XXX TODO XXX': "getattr(X, 'dtype', None) not in numeric"}, {
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}, {'anyOf': [{
    'allOf': [{'XXX TODO XXX': "getattr(X, 'dtype', None) is not None"}, {
    'XXX TODO XXX': "getattr(X, 'dtype', None) in numeric"}]}, {
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}]}]}, {'anyOf':
    [{'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'}, {
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}]}]}]}]}]}]}, {
    'anyOf': [{'type': 'object', 'properties': {'base_estimator': {'enum':
    [None]}}}, {'type': 'object', 'properties': {'cv': {'enum': ['prefit']}
    }}, {'type': 'object', 'properties': {'y': {'enum': [None]}}}, {'type':
    'object', 'properties': {'y': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'y': {'not': {'enum': ['no_validation']}}}}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}, {'anyOf': [{
    'allOf': [{'type': 'object', 'properties': {'numeric': {'type':
    'string'}}}, {'type': 'object', 'properties': {'numeric': {'enum': [
    'numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': "X.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX': 'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]
    }, {'anyOf': [{'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'}, {
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}]}]}]}]}, {
    'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
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
    }]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'type': 'string'}}}, {'type': 'object', 'properties': {
    'numeric': {'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {
    'XXX TODO XXX': "getattr(X, 'dtype', None) not in numeric"}, {
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}, {'anyOf': [{
    'allOf': [{'XXX TODO XXX': "getattr(X, 'dtype', None) is not None"}, {
    'XXX TODO XXX': "getattr(X, 'dtype', None) in numeric"}]}, {
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}]}]}, {'anyOf':
    [{'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'}, {
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX':
    "X.sparse.to_coo().dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in X.dtypes])) <= 1'}]}]}]}]}]}]}]}]},
    {'description':
    'From /utils/validation.py:None:check_array, Exception: raise ValueError("""Complex data not supported {} """.format(array)     ) from complex_warning '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'enum': [None]}}}, {'type':
    'object', 'properties': {'y': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'y': {'not': {'enum': ['no_validation']}}}}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}]}, {'anyOf': [{'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}
    ]}, {'XXX TODO XXX': 'sp.issparse(X)'}]}]}]}, {'description':
    'From /utils/validation.py:None:check_array, Exception: raise ValueError(     "Unable to convert array of bytes/strings into decimal numbers with dtype=\'numeric\'"     ) from e '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'enum': [None]}}}, {'type':
    'object', 'properties': {'y': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'y': {'not': {'enum': ['no_validation']}}}}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "not hasattr(X.dtypes, '__array__')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX':
    'not all((isinstance(numeric, np.dtype) for numeric in list(X.dtypes)))'
    }, {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}]}]}]},
    {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'np.result_type(*list(X.dtypes)) is None'}, {
    'XXX TODO XXX': 'np.result_type(*list(X.dtypes)) not in numeric'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind not in 'OUSV'"}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, None).dtype.kind not in 'OUSV'"}]}]}]}, {'anyOf':
    [{'allOf': [{'XXX TODO XXX':
    'np.result_type(*list(X.dtypes)) is not None'}, {'XXX TODO XXX':
    'np.result_type(*list(X.dtypes)) in numeric'}]}, {'allOf': [{'anyOf': [
    {'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}]}]}]}]}
    ]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}]}]}]}]}]
    }]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'all((isinstance(numeric, np.dtype) for numeric in list(X.dtypes)))'},
    {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}]}]}]},
    {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}]}]}]}]}
    ]}, {'anyOf': [{'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'},
    {'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}]}]}]}]}]
    }]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}]}]}]},
    {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}]}]}]}]}
    ]}, {'anyOf': [{'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'},
    {'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}]}]}]}]}]
    }]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': "not hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "not hasattr(X.dtypes, '__array__')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX':
    'not all((isinstance(numeric, np.dtype) for numeric in list(X.dtypes)))'
    }, {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}]}]}]},
    {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'np.result_type(*list(X.dtypes)) is None'}, {
    'XXX TODO XXX': 'np.result_type(*list(X.dtypes)) not in numeric'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind not in 'OUSV'"}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, None).dtype.kind not in 'OUSV'"}]}]}]}, {'anyOf':
    [{'allOf': [{'XXX TODO XXX':
    'np.result_type(*list(X.dtypes)) is not None'}, {'XXX TODO XXX':
    'np.result_type(*list(X.dtypes)) in numeric'}]}, {'allOf': [{'anyOf': [
    {'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}]}]}]}]}
    ]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}]}]}]}]}]
    }]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'all((isinstance(numeric, np.dtype) for numeric in list(X.dtypes)))'},
    {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}]}]}]},
    {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) not in numeric"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind not in 'OUSV'"}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, None).dtype.kind not in 'OUSV'"}]}]}]}, {'anyOf':
    [{'allOf': [{'XXX TODO XXX': "getattr(X, 'dtype', None) is not None"},
    {'XXX TODO XXX': "getattr(X, 'dtype', None) in numeric"}]}, {'allOf': [
    {'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}]}]}]}]}
    ]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}]}]}]}]}]
    }]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}]}]}]},
    {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) not in numeric"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind not in 'OUSV'"}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, None).dtype.kind not in 'OUSV'"}]}]}]}, {'anyOf':
    [{'allOf': [{'XXX TODO XXX': "getattr(X, 'dtype', None) is not None"},
    {'XXX TODO XXX': "getattr(X, 'dtype', None) in numeric"}]}, {'allOf': [
    {'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}]}]}]}]}
    ]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}]}]}]}]}]
    }]}]}]}]}]}]}]}]}, {'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Found array with %d sample(s) (shape=%s) while a minimum of %d is required%s.'      % (n_samples, array.shape, ensure_min_samples, context)) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'enum': [None]}}}, {'type':
    'object', 'properties': {'y': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'y': {'not': {'enum': ['no_validation']}}}}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf':
    [{'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {
    'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=np.float64)) >= 1'
    }]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'
    }}}}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=np.float64).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=np.float64)) >= 1'}]}]}]}]}]}]}
    ]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).astype(np.float64)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False)) >= 1"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'},
    {'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0])) >= 1'
    }]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "_num_samples(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).astype(np.float64)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "_num_samples(np.asarray(X, None).astype(dtype[0], casting='unsafe', False)) >= 1"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'},
    {'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=dtype[0]).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=dtype[0])) >= 1'}]}]}]}]}]}]}]}
    ]}]}, {'anyOf': [{'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'},
    {'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object',
    'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).astype(np.float64)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False)) >= 1"
    }]}]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=numeric).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=numeric)) >= 1'
    }]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'enum': [None]}}}, {
    'XXX TODO XXX': "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "_num_samples(np.asarray(X, None).astype(numeric, casting='unsafe', False).astype(np.float64)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "_num_samples(np.asarray(X, None).astype(numeric, casting='unsafe', False)) >= 1"
    }]}]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=numeric).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': '_num_samples(np.asarray(X, None, dtype=numeric)) >= 1'
    }]}]}]}]}]}]}]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf':
    [{'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {
    'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=np.float64)) >= 1'
    }]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'
    }}}}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=np.float64).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=np.float64)) >= 1'}]}]}]}]}]}]}
    ]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) not in numeric"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], None, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind not in 'OUSV'"},
    {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, None).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, None)) >= 1'}]}]}]}]}
    ]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], None, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'
    }}}}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, None).dtype.kind not in 'OUSV'"}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, None).astype(np.float64)) >= 1'}]}, {
    'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, None).dtype.kind in 'OUSV'"}]}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, None)) >= 1'}]}]}]}]}]}]}]}, {'anyOf':
    [{'allOf': [{'XXX TODO XXX': "getattr(X, 'dtype', None) is not None"},
    {'XXX TODO XXX': "getattr(X, 'dtype', None) in numeric"}]}, {'allOf': [
    {'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object',
    'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).astype(np.float64)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False)) >= 1"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'},
    {'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0])) >= 1'
    }]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "_num_samples(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).astype(np.float64)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "_num_samples(np.asarray(X, None).astype(dtype[0], casting='unsafe', False)) >= 1"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'},
    {'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=dtype[0]).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=dtype[0])) >= 1'}]}]}]}]}]}]}]}
    ]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).astype(np.float64)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False)) >= 1"
    }]}]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=numeric).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=numeric)) >= 1'
    }]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'enum': [None]}}}, {
    'XXX TODO XXX': "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "_num_samples(np.asarray(X, None).astype(numeric, casting='unsafe', False).astype(np.float64)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "_num_samples(np.asarray(X, None).astype(numeric, casting='unsafe', False)) >= 1"
    }]}]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=numeric).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': '_num_samples(np.asarray(X, None, dtype=numeric)) >= 1'
    }]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}, {'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Found array with %d feature(s) (shape=%s) while a minimum of %d is required%s.'      % (n_features, array.shape, ensure_min_features, context)) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'enum': [None]}}}, {'type':
    'object', 'properties': {'y': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'y': {'not': {'enum': ['no_validation']}}}}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf':
    [{'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {
    'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'
    }}}}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).ndim != 2'
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}, {'anyOf': [{'allOf':
    [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    'np.asarray(X, None, dtype=np.float64).astype(np.float64).ndim != 2'},
    {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}, {'anyOf': [{
    'allOf': [{'type': 'object', 'properties': {'numeric': {'type':
    'string'}}}, {'type': 'object', 'properties': {'numeric': {'enum': [
    'numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).astype(np.float64).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf':
    [{'XXX TODO XXX': 'dtype[0] is not None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).astype(np.float64).ndim != 2'
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}, {'anyOf': [{
    'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).astype(np.float64).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf':
    [{'XXX TODO XXX': 'dtype[0] is not None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    'np.asarray(X, None, dtype=dtype[0]).astype(np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{'type':
    'object', 'properties': {'numeric': {'type': 'string'}}}, {'type':
    'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=dtype[0]).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}]}]}, {'anyOf': [{
    'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'enum': [None]}}}, {
    'XXX TODO XXX': "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).astype(np.float64).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'enum': [None]}}
    }}, {'XXX TODO XXX': "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).astype(np.float64).ndim != 2'
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}, {'anyOf': [{
    'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).astype(np.float64).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'enum': [None]}}
    }}, {'XXX TODO XXX': "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    'np.asarray(X, None, dtype=numeric).astype(np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{'type':
    'object', 'properties': {'numeric': {'type': 'string'}}}, {'type':
    'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=numeric).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}]}]}]}]}]}]}, {
    'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf':
    [{'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {
    'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'
    }}}}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).ndim != 2'
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}, {'anyOf': [{'allOf':
    [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    'np.asarray(X, None, dtype=np.float64).astype(np.float64).ndim != 2'},
    {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}, {'anyOf': [{
    'allOf': [{'type': 'object', 'properties': {'numeric': {'type':
    'string'}}}, {'type': 'object', 'properties': {'numeric': {'enum': [
    'numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) not in numeric"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], None, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'
    }}}}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind not in 'OUSV'"},
    {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, None).astype(np.float64).ndim != 2'
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': 'np.asarray(X.sparse.to_coo(), None, None).ndim != 2'},
    {'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}, {'anyOf': [{'allOf':
    [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], None, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, None).dtype.kind not in 'OUSV'"}, {'XXX TODO XXX':
    'np.asarray(X, None, None).astype(np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{'type':
    'object', 'properties': {'numeric': {'type': 'string'}}}, {'type':
    'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX': "np.asarray(X, None, None).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': 'np.asarray(X, None, None).ndim != 2'}, {'XXX TODO XXX':
    'array.shape[1] >= 1'}]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is not None"}, {
    'XXX TODO XXX': "getattr(X, 'dtype', None) in numeric"}]}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).astype(np.float64).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf':
    [{'XXX TODO XXX': 'dtype[0] is not None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).astype(np.float64).ndim != 2'
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}, {'anyOf': [{
    'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).astype(np.float64).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf':
    [{'XXX TODO XXX': 'dtype[0] is not None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    'np.asarray(X, None, dtype=dtype[0]).astype(np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{'type':
    'object', 'properties': {'numeric': {'type': 'string'}}}, {'type':
    'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=dtype[0]).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}]}]}]}]}, {'anyOf':
    [{'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'enum': [None]}}}, {
    'XXX TODO XXX': "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).astype(np.float64).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'enum': [None]}}
    }}, {'XXX TODO XXX': "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).astype(np.float64).ndim != 2'
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}, {'anyOf': [{
    'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).astype(np.float64).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'enum': [None]}}
    }}, {'XXX TODO XXX': "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    'np.asarray(X, None, dtype=numeric).astype(np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{'type':
    'object', 'properties': {'numeric': {'type': 'string'}}}, {'type':
    'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=numeric).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}, {
    'description':
    'From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'enum': [None]}}}, {
    'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'XXX TODO XXX': "not hasattr(X, 'fit')"}, {'XXX TODO XXX':
    'not callable(X.fit)'}]}, {'description':
    'From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'enum': [None]}}}, {
    'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'XXX TODO XXX': "hasattr(X, '__len__')"}, {'XXX TODO XXX':
    "hasattr(X, 'shape')"}, {'XXX TODO XXX': "hasattr(X, '__array__')"}]},
    {'description':
    "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(     'Singleton array %r cannot be considered a valid collection.' % x) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'enum': [None]}}}, {
    'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
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
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'enum': [None]}}}, {
    'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
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
    , 'allOf': [{'anyOf': [{'type': 'object', 'properties': {
    'base_estimator': {'not': {'enum': [None]}}}}, {'type': 'object',
    'properties': {'cv': {'enum': ['prefit']}}}, {'type': 'object',
    'properties': {'y': {'enum': [None]}}}, {'allOf': [{'type': 'object',
    'properties': {'y': {'type': 'string'}}}, {'type': 'object',
    'properties': {'y': {'enum': ['no_validation']}}}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'y': {'not': {'enum': [None
    ]}}}}, {'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }]}, {'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}
    }}, {'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }]}]}]}, {'anyOf': [{'type': 'object', 'properties': {'base_estimator':
    {'enum': [None]}}}, {'type': 'object', 'properties': {'cv': {'enum': [
    'prefit']}}}, {'type': 'object', 'properties': {'y': {'enum': [None]}}},
    {'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'y': {'not': {
    'enum': [None]}}}}, {'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }]}, {'anyOf': [{'type': 'object', 'properties': {'y': {'enum': [None]}
    }}, {'XXX TODO XXX':
    'len(np.unique([_num_samples(X) for X in arrays if X is not None])) <= 1'
    }]}]}]}]}, {'description':
    'From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'enum': [None]}}}, {
    'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf':
    [{'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {
    'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).fit)'
    }]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'
    }}}}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=np.float64).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, dtype=np.float64).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=np.float64), 'fit')"}, {
    'XXX TODO XXX':
    'not callable(np.asarray(X, None, dtype=np.float64).fit)'}]}]}]}]}]}]}]
    }, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).astype(np.float64).fit)"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).fit)"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'},
    {'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).fit)'
    }]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).astype(np.float64).fit)"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).fit)"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'},
    {'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=dtype[0]).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, dtype=dtype[0]).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'fit')"}, {
    'XXX TODO XXX': 'not callable(np.asarray(X, None, dtype=dtype[0]).fit)'
    }]}]}]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).astype(np.float64).fit)"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).fit)"
    }]}]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=numeric).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=numeric).fit)'}
    ]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'enum': [None]}}}, {
    'XXX TODO XXX': "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X, None).astype(numeric, casting='unsafe', False).astype(np.float64).fit)"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X, None).astype(numeric, casting='unsafe', False).fit)"
    }]}]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, dtype=numeric).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric), 'fit')"}, {
    'XXX TODO XXX': 'not callable(np.asarray(X, None, dtype=numeric).fit)'}
    ]}]}]}]}]}]}]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf':
    [{'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {
    'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).fit)'
    }]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'
    }}}}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=np.float64).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, dtype=np.float64).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=np.float64), 'fit')"}, {
    'XXX TODO XXX':
    'not callable(np.asarray(X, None, dtype=np.float64).fit)'}]}]}]}]}]}]}]
    }, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) not in numeric"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], None, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], None, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind not in 'OUSV'"},
    {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, None).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, None).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, None), 'fit')"}, {
    'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, None).fit)'}]}]}]}]}]
    }, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], None, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], None, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'
    }}}}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, None).dtype.kind not in 'OUSV'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, None).astype(np.float64), 'fit')"}, {
    'XXX TODO XXX':
    'not callable(np.asarray(X, None, None).astype(np.float64).fit)'}]}, {
    'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, None).dtype.kind in 'OUSV'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, None), 'fit')"}, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, None).fit)'}]}]}]}]}]}]}]}, {'anyOf':
    [{'allOf': [{'XXX TODO XXX': "getattr(X, 'dtype', None) is not None"},
    {'XXX TODO XXX': "getattr(X, 'dtype', None) in numeric"}]}, {'allOf': [
    {'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object',
    'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).astype(np.float64).fit)"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).fit)"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'},
    {'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).fit)'
    }]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).astype(np.float64).fit)"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(dtype[0], casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).fit)"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'},
    {'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=dtype[0]).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, dtype=dtype[0]).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=dtype[0]), 'fit')"}, {
    'XXX TODO XXX': 'not callable(np.asarray(X, None, dtype=dtype[0]).fit)'
    }]}]}]}]}]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).astype(np.float64).fit)"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).fit)"
    }]}]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=numeric).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X.sparse.to_coo(), None, dtype=numeric).fit)'}
    ]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "not hasattr(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True).fit)"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'enum': [None]}}}, {
    'XXX TODO XXX': "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X, None).astype(numeric, casting='unsafe', False).astype(np.float64).fit)"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False), 'fit')"
    }, {'XXX TODO XXX':
    "not callable(np.asarray(X, None).astype(numeric, casting='unsafe', False).fit)"
    }]}]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric).astype(np.float64), 'fit')"
    }, {'XXX TODO XXX':
    'not callable(np.asarray(X, None, dtype=numeric).astype(np.float64).fit)'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric), 'fit')"}, {
    'XXX TODO XXX': 'not callable(np.asarray(X, None, dtype=numeric).fit)'}
    ]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}, {'description':
    'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'enum': [None]}}}, {
    'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
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
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'enum': [None]}}}, {
    'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "not hasattr(X.dtypes, '__array__')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX':
    'not all((isinstance(numeric, np.dtype) for numeric in list(X.dtypes)))'
    }, {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
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
    'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'np.result_type(*list(X.dtypes)) is None'}, {
    'XXX TODO XXX': 'np.result_type(*list(X.dtypes)) not in numeric'}, {
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
    'np.result_type(*list(X.dtypes)) in numeric'}]}, {'allOf': [{'anyOf': [
    {'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
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
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric).dtype, 'kind')"}, {
    'XXX TODO XXX': "np.asarray(X, None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'all((isinstance(numeric, np.dtype) for numeric in list(X.dtypes)))'},
    {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
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
    'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
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
    }]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric).dtype, 'kind')"}, {
    'XXX TODO XXX': "np.asarray(X, None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}]}]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'XXX TODO XXX':
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
    'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
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
    }]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric).dtype, 'kind')"}, {
    'XXX TODO XXX': "np.asarray(X, None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}]}]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': "not hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "not hasattr(X.dtypes, '__array__')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX':
    'not all((isinstance(numeric, np.dtype) for numeric in list(X.dtypes)))'
    }, {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
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
    'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'np.result_type(*list(X.dtypes)) is None'}, {
    'XXX TODO XXX': 'np.result_type(*list(X.dtypes)) not in numeric'}, {
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
    'np.result_type(*list(X.dtypes)) in numeric'}]}, {'allOf': [{'anyOf': [
    {'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
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
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric).dtype, 'kind')"}, {
    'XXX TODO XXX': "np.asarray(X, None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'all((isinstance(numeric, np.dtype) for numeric in list(X.dtypes)))'},
    {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
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
    'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) not in numeric"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
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
    {'XXX TODO XXX': "np.asarray(X, None, None).dtype.kind != 'c'"}]}]}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "getattr(X, 'dtype', None) is not None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) in numeric"}]}, {'allOf': [{'anyOf': [{
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
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric).dtype, 'kind')"}, {
    'XXX TODO XXX': "np.asarray(X, None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}]}]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'XXX TODO XXX':
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
    'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) not in numeric"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
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
    {'XXX TODO XXX': "np.asarray(X, None, None).dtype.kind != 'c'"}]}]}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "getattr(X, 'dtype', None) is not None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) in numeric"}]}, {'allOf': [{'anyOf': [{
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
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric), 'dtype')"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False), 'dtype')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype is None"
    }, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype, 'kind')"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind != 'c'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric), 'dtype')"}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=numeric).dtype is None'}, {
    'XXX TODO XXX':
    "not hasattr(np.asarray(X, None, dtype=numeric).dtype, 'kind')"}, {
    'XXX TODO XXX': "np.asarray(X, None, dtype=numeric).dtype.kind != 'c'"}
    ]}]}]}]}]}]}]}]}]}]}]}]}]}, {'description':
    'From /utils/validation.py:None:check_array, Exception: raise ValueError("""Complex data not supported {} """.format(array)     ) from complex_warning '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'enum': [None]}}}, {
    'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}]}, {'anyOf': [{'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}
    ]}, {'XXX TODO XXX': 'sp.issparse(X)'}]}]}]}, {'description':
    'From /utils/validation.py:None:check_array, Exception: raise ValueError(     "Unable to convert array of bytes/strings into decimal numbers with dtype=\'numeric\'"     ) from e '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'enum': [None]}}}, {
    'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "not hasattr(X.dtypes, '__array__')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX':
    'not all((isinstance(numeric, np.dtype) for numeric in list(X.dtypes)))'
    }, {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}]}]}]},
    {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'np.result_type(*list(X.dtypes)) is None'}, {
    'XXX TODO XXX': 'np.result_type(*list(X.dtypes)) not in numeric'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind not in 'OUSV'"}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, None).dtype.kind not in 'OUSV'"}]}]}]}, {'anyOf':
    [{'allOf': [{'XXX TODO XXX':
    'np.result_type(*list(X.dtypes)) is not None'}, {'XXX TODO XXX':
    'np.result_type(*list(X.dtypes)) in numeric'}]}, {'allOf': [{'anyOf': [
    {'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}]}]}]}]}
    ]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}]}]}]}]}]
    }]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'all((isinstance(numeric, np.dtype) for numeric in list(X.dtypes)))'},
    {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}]}]}]},
    {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}]}]}]}]}
    ]}, {'anyOf': [{'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'},
    {'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}]}]}]}]}]
    }]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}]}]}]},
    {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}]}]}]}]}
    ]}, {'anyOf': [{'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'},
    {'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}]}]}]}]}]
    }]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': "not hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "not hasattr(X.dtypes, '__array__')"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX':
    'not all((isinstance(numeric, np.dtype) for numeric in list(X.dtypes)))'
    }, {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}]}]}]},
    {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'np.result_type(*list(X.dtypes)) is None'}, {
    'XXX TODO XXX': 'np.result_type(*list(X.dtypes)) not in numeric'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind not in 'OUSV'"}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, None).dtype.kind not in 'OUSV'"}]}]}]}, {'anyOf':
    [{'allOf': [{'XXX TODO XXX':
    'np.result_type(*list(X.dtypes)) is not None'}, {'XXX TODO XXX':
    'np.result_type(*list(X.dtypes)) in numeric'}]}, {'allOf': [{'anyOf': [
    {'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}]}]}]}]}
    ]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}]}]}]}]}]
    }]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'all((isinstance(numeric, np.dtype) for numeric in list(X.dtypes)))'},
    {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}]}]}]},
    {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) not in numeric"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind not in 'OUSV'"}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, None).dtype.kind not in 'OUSV'"}]}]}]}, {'anyOf':
    [{'allOf': [{'XXX TODO XXX': "getattr(X, 'dtype', None) is not None"},
    {'XXX TODO XXX': "getattr(X, 'dtype', None) in numeric"}]}, {'allOf': [
    {'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}]}]}]}]}
    ]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}]}]}]}]}]
    }]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}]}]}]},
    {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) not in numeric"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind not in 'OUSV'"}]},
    {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'}}
    }}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, None).dtype.kind not in 'OUSV'"}]}]}]}, {'anyOf':
    [{'allOf': [{'XXX TODO XXX': "getattr(X, 'dtype', None) is not None"},
    {'XXX TODO XXX': "getattr(X, 'dtype', None) in numeric"}]}, {'allOf': [
    {'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'type': 'object',
    'properties': {'numeric': {'not': {'type': 'string'}}}}, {'type':
    'object', 'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}]}]}]}]}
    ]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"},
    {'XXX TODO XXX': 'X.ndim > 1'}]}, {'XXX TODO XXX': 'sp.issparse(X)'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'type': 'object', 'properties':
    {'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'type': 'object', 'properties': {
    'numeric': {'not': {'type': 'string'}}}}, {'type': 'object',
    'properties': {'numeric': {'not': {'enum': ['numeric']}}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}]}]}]}]}]
    }]}]}]}]}]}]}]}]}, {'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Found array with %d sample(s) (shape=%s) while a minimum of %d is required%s.'      % (n_samples, array.shape, ensure_min_samples, context)) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'enum': [None]}}}, {
    'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf':
    [{'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {
    'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=np.float64)) >= 1'
    }]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'
    }}}}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=np.float64).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=np.float64)) >= 1'}]}]}]}]}]}]}
    ]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).astype(np.float64)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False)) >= 1"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'},
    {'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0])) >= 1'
    }]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "_num_samples(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).astype(np.float64)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "_num_samples(np.asarray(X, None).astype(dtype[0], casting='unsafe', False)) >= 1"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'},
    {'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=dtype[0]).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=dtype[0])) >= 1'}]}]}]}]}]}]}]}
    ]}]}, {'anyOf': [{'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'},
    {'allOf': [{'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object',
    'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).astype(np.float64)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False)) >= 1"
    }]}]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=numeric).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=numeric)) >= 1'
    }]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'enum': [None]}}}, {
    'XXX TODO XXX': "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "_num_samples(np.asarray(X, None).astype(numeric, casting='unsafe', False).astype(np.float64)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "_num_samples(np.asarray(X, None).astype(numeric, casting='unsafe', False)) >= 1"
    }]}]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=numeric).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': '_num_samples(np.asarray(X, None, dtype=numeric)) >= 1'
    }]}]}]}]}]}]}]}]}]}]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf':
    [{'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {
    'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=np.float64)) >= 1'
    }]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'
    }}}}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=np.float64).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=np.float64)) >= 1'}]}]}]}]}]}]}
    ]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) not in numeric"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], None, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'not': {'type': 'string'}}}}, {'type': 'object', 'properties': {
    'numeric': {'not': {'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind not in 'OUSV'"},
    {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, None).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, None)) >= 1'}]}]}]}]}
    ]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], None, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'
    }}}}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, None).dtype.kind not in 'OUSV'"}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, None).astype(np.float64)) >= 1'}]}, {
    'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric': {
    'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, None).dtype.kind in 'OUSV'"}]}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, None)) >= 1'}]}]}]}]}]}]}]}, {'anyOf':
    [{'allOf': [{'XXX TODO XXX': "getattr(X, 'dtype', None) is not None"},
    {'XXX TODO XXX': "getattr(X, 'dtype', None) in numeric"}]}, {'allOf': [
    {'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {
    'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object',
    'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX': 'dtype[0] is None'}, {
    'XXX TODO XXX': "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).astype(np.float64)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False)) >= 1"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'},
    {'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=dtype[0])) >= 1'
    }]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "_num_samples(np.asarray(X, None).astype(dtype[0], casting='unsafe', False).astype(np.float64)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "_num_samples(np.asarray(X, None).astype(dtype[0], casting='unsafe', False)) >= 1"
    }]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX': 'dtype[0] is not None'},
    {'XXX TODO XXX': "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=dtype[0]).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=dtype[0])) >= 1'}]}]}]}]}]}]}]}
    ]}]}]}]}, {'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'numeric': {
    'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).astype(np.float64)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "_num_samples(np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False)) >= 1"
    }]}]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=numeric).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    '_num_samples(np.asarray(X.sparse.to_coo(), None, dtype=numeric)) >= 1'
    }]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{'XXX TODO XXX':
    "hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim > 1'}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {'XXX TODO XXX':
    "_num_samples(_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True)) >= 1"
    }]}, {'anyOf': [{'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'enum': [None]}}}, {
    'XXX TODO XXX': "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "_num_samples(np.asarray(X, None).astype(numeric, casting='unsafe', False).astype(np.float64)) >= 1"
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "_num_samples(np.asarray(X, None).astype(numeric, casting='unsafe', False)) >= 1"
    }]}]}]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'numeric': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    '_num_samples(np.asarray(X, None, dtype=numeric).astype(np.float64)) >= 1'
    }]}, {'anyOf': [{'allOf': [{'type': 'object', 'properties': {'numeric':
    {'type': 'string'}}}, {'type': 'object', 'properties': {'numeric': {
    'enum': ['numeric']}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': '_num_samples(np.asarray(X, None, dtype=numeric)) >= 1'
    }]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}, {'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Found array with %d feature(s) (shape=%s) while a minimum of %d is required%s.'      % (n_features, array.shape, ensure_min_features, context)) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'enum': [None]}}}, {
    'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf':
    [{'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {
    'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'
    }}}}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).ndim != 2'
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}, {'anyOf': [{'allOf':
    [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    'np.asarray(X, None, dtype=np.float64).astype(np.float64).ndim != 2'},
    {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}, {'anyOf': [{
    'allOf': [{'type': 'object', 'properties': {'numeric': {'type':
    'string'}}}, {'type': 'object', 'properties': {'numeric': {'enum': [
    'numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).astype(np.float64).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf':
    [{'XXX TODO XXX': 'dtype[0] is not None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).astype(np.float64).ndim != 2'
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}, {'anyOf': [{
    'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).astype(np.float64).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf':
    [{'XXX TODO XXX': 'dtype[0] is not None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    'np.asarray(X, None, dtype=dtype[0]).astype(np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{'type':
    'object', 'properties': {'numeric': {'type': 'string'}}}, {'type':
    'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=dtype[0]).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}]}]}, {'anyOf': [{
    'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'enum': [None]}}}, {
    'XXX TODO XXX': "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).astype(np.float64).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'enum': [None]}}
    }}, {'XXX TODO XXX': "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).astype(np.float64).ndim != 2'
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}, {'anyOf': [{
    'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).astype(np.float64).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'enum': [None]}}
    }}, {'XXX TODO XXX': "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    'np.asarray(X, None, dtype=numeric).astype(np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{'type':
    'object', 'properties': {'numeric': {'type': 'string'}}}, {'type':
    'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=numeric).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}]}]}]}]}]}]}, {
    'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(X, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(X, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(X.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(X, 'sparse')"}, {'XXX TODO XXX': 'X.ndim <= 1'}, {'allOf':
    [{'anyOf': [{'type': 'object', 'laleNot': 'X/isSparse'}, {
    'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'
    }}}}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=np.float64).astype(np.float64).ndim != 2'
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=np.float64).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}, {'anyOf': [{'allOf':
    [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=np.float64, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    'np.asarray(X, None, dtype=np.float64).astype(np.float64).ndim != 2'},
    {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=np.float64).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}, {'anyOf': [{
    'allOf': [{'type': 'object', 'properties': {'numeric': {'type':
    'string'}}}, {'type': 'object', 'properties': {'numeric': {'enum': [
    'numeric']}}}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'isinstance(numeric, [list, tuple])'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is None"}, {'XXX TODO XXX':
    "getattr(X, 'dtype', None) not in numeric"}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], None, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'type': 'string'
    }}}}, {'type': 'object', 'properties': {'numeric': {'not': {'enum': [
    'numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind not in 'OUSV'"},
    {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, None).astype(np.float64).ndim != 2'
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, None).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': 'np.asarray(X.sparse.to_coo(), None, None).ndim != 2'},
    {'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}, {'anyOf': [{'allOf':
    [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], None, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, None).dtype.kind not in 'OUSV'"}, {'XXX TODO XXX':
    'np.asarray(X, None, None).astype(np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{'type':
    'object', 'properties': {'numeric': {'type': 'string'}}}, {'type':
    'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX': "np.asarray(X, None, None).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': 'np.asarray(X, None, None).ndim != 2'}, {'XXX TODO XXX':
    'array.shape[1] >= 1'}]}]}]}]}]}]}]}, {'anyOf': [{'allOf': [{
    'XXX TODO XXX': "getattr(X, 'dtype', None) is not None"}, {
    'XXX TODO XXX': "getattr(X, 'dtype', None) in numeric"}]}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).astype(np.float64).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(dtype[0], casting='unsafe', False).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf':
    [{'XXX TODO XXX': 'dtype[0] is not None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).astype(np.float64).ndim != 2'
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=dtype[0]).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}, {'anyOf': [{
    'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=dtype[0], False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf': [{
    'XXX TODO XXX': 'dtype[0] is None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).astype(np.float64).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(dtype[0], casting='unsafe', False).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf':
    [{'XXX TODO XXX': 'dtype[0] is not None'}, {'XXX TODO XXX':
    "np.dtype(dtype[0]).kind in 'iu'"}]}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    'np.asarray(X, None, dtype=dtype[0]).astype(np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{'type':
    'object', 'properties': {'numeric': {'type': 'string'}}}, {'type':
    'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=dtype[0]).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=dtype[0]).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}]}]}]}]}, {'anyOf':
    [{'XXX TODO XXX': 'isinstance(numeric, [list, tuple])'}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX': "not hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim <= 1'}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X.sparse.to_coo(), accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X.sparse.to_coo())'}, {'allOf': [{'anyOf':
    [{'type': 'object', 'properties': {'numeric': {'enum': [None]}}}, {
    'XXX TODO XXX': "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).astype(np.float64).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None).astype(numeric, casting='unsafe', False).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'enum': [None]}}
    }}, {'XXX TODO XXX': "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).astype(np.float64).ndim != 2'
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X.sparse.to_coo(), None, dtype=numeric).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    'np.asarray(X.sparse.to_coo(), None, dtype=numeric).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}, {'anyOf': [{
    'allOf': [{'XXX TODO XXX': "hasattr(X, 'sparse')"}, {'XXX TODO XXX':
    'X.ndim > 1'}]}, {'allOf': [{'anyOf': [{'type': 'object', 'laleNot':
    'X/isSparse'}, {'XXX TODO XXX':
    "_ensure_sparse_format(X, accept_sparse=['csc', 'csr', 'coo'], dtype=numeric, False, False, True).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{
    'XXX TODO XXX': 'sp.issparse(X)'}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'enum': [None]}}}, {'XXX TODO XXX':
    "np.dtype(numeric).kind not in 'iu'"}, {'allOf': [{'anyOf': [{'type':
    'object', 'properties': {'numeric': {'not': {'type': 'string'}}}}, {
    'type': 'object', 'properties': {'numeric': {'not': {'enum': ['numeric'
    ]}}}}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind not in 'OUSV'"
    }, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).astype(np.float64).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{
    'type': 'object', 'properties': {'numeric': {'type': 'string'}}}, {
    'type': 'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).dtype.kind in 'OUSV'"
    }]}, {'XXX TODO XXX':
    "np.asarray(X, None).astype(numeric, casting='unsafe', False).ndim != 2"
    }, {'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}, {'anyOf': [{'allOf':
    [{'type': 'object', 'properties': {'numeric': {'not': {'enum': [None]}}
    }}, {'XXX TODO XXX': "np.dtype(numeric).kind in 'iu'"}]}, {'allOf': [{
    'anyOf': [{'type': 'object', 'properties': {'numeric': {'not': {'type':
    'string'}}}}, {'type': 'object', 'properties': {'numeric': {'not': {
    'enum': ['numeric']}}}}, {'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind not in 'OUSV'"}, {
    'XXX TODO XXX':
    'np.asarray(X, None, dtype=numeric).astype(np.float64).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}, {'anyOf': [{'allOf': [{'type':
    'object', 'properties': {'numeric': {'type': 'string'}}}, {'type':
    'object', 'properties': {'numeric': {'enum': ['numeric']}}}, {
    'XXX TODO XXX':
    "np.asarray(X, None, dtype=numeric).dtype.kind in 'OUSV'"}]}, {
    'XXX TODO XXX': 'np.asarray(X, None, dtype=numeric).ndim != 2'}, {
    'XXX TODO XXX': 'array.shape[1] >= 1'}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}, {
    'description':
    'From /utils/validation.py:None:_assert_all_finite, Exception: raise ValueError(msg_err.format(type_err, msg_dtype if msg_dtype is not     None else X.dtype)) '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'enum': [None]}}}, {
    'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'XXX TODO XXX': "_get_config()['assume_finite']"}, {'allOf': [{
    'XXX TODO XXX': "y.dtype.kind in 'fc'"}, {'XXX TODO XXX':
    'np.isfinite(_safe_accumulator_op(np.sum, y))'}]}, {'XXX TODO XXX':
    "y.dtype.kind not in 'fc'"}, {'XXX TODO XXX': 'np.isfinite(y).all()'}]},
    {'description':
    "From /utils/validation.py:None:_assert_all_finite, Exception: raise ValueError('Input contains NaN') "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'enum': [None]}}}, {
    'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'XXX TODO XXX': "_get_config()['assume_finite']"}, {'allOf': [{
    'XXX TODO XXX': "y.dtype.kind in 'fc'"}, {'XXX TODO XXX':
    'np.isfinite(_safe_accumulator_op(np.sum, y))'}]}, {'XXX TODO XXX':
    "y.dtype.kind in 'fc'"}, {'XXX TODO XXX':
    "y.dtype != np.dtype('object')"}, {'XXX TODO XXX':
    'not _object_dtype_isnan(y).any()'}]}, {'description':
    "From /utils/validation.py:None:column_or_1d, Exception: raise ValueError('y should be a 1d array, got an array of shape {} instead.'     .format(shape)) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'enum': [None]}}}, {
    'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]}]
    }, {'description':
    "From /utils/validation.py:None:check_X_y, Exception: raise ValueError('y cannot be None') "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'enum': [None]}}}, {
    'allOf': [{'type': 'object', 'properties': {'y': {'type': 'string'}}},
    {'type': 'object', 'properties': {'y': {'enum': ['no_validation']}}}]},
    {'type': 'object', 'properties': {'y': {'not': {'enum': [None]}}}}]}, {
    'description':
    "From /base.py:BaseEstimator:_validate_data, Exception: raise ValueError(     f'This {self.__class__.__name__} estimator requires y to be passed, but the target y is None.'     ) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'y': {'not': {'enum': [None]}}}},
    {'XXX TODO XXX': "not self._get_tags()['requires_y']"}]}, {
    'description':
    'From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'sample_weight': {'enum': [None]
    }}}, {'type': 'object', 'properties': {'sample_weight': {'enum': [None]
    }}}, {'type': 'object', 'properties': {'sample_weight': {'type':
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
    'From /utils/validation.py:None:_ensure_no_complex_data, Exception: raise ValueError("""Complex data not supported {} """.format(array)) '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'sample_weight': {'enum': [None]
    }}}, {'type': 'object', 'properties': {'sample_weight': {'enum': [None]
    }}}, {'type': 'object', 'properties': {'sample_weight': {'type':
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
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'sample_weight': {'enum': [None]
    }}}, {'type': 'object', 'properties': {'sample_weight': {'enum': [None]
    }}}, {'type': 'object', 'properties': {'sample_weight': {'type':
    'number'}}}, {'type': 'object', 'laleNot': 'X/isSparse'}]}, {
    'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError(     'Pandas DataFrame with mixed sparse extension arrays generated a sparse matrix with object dtype which can not be converted to a scipy sparse matrix.Sparse extension arrays should all have the same numeric type.'     ) "
    , 'allOf': [{'anyOf': [{'type': 'object', 'properties': {
    'base_estimator': {'not': {'enum': [None]}}}}, {'type': 'object',
    'properties': {'cv': {'enum': ['prefit']}}}, {'type': 'object',
    'properties': {'sample_weight': {'enum': [None]}}}, {'type': 'object',
    'properties': {'sample_weight': {'enum': [None]}}}, {'type': 'object',
    'properties': {'sample_weight': {'type': 'number'}}}, {'allOf': [{
    'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(sample_weight, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(sample_weight, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(sample_weight.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(sample_weight, 'sparse')"}, {'XXX TODO XXX':
    'sample_weight.ndim <= 1'}, {'XXX TODO XXX':
    "sample_weight.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in sample_weight.dtypes])) <= 1'}]}, {
    'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(sample_weight, 'dtype', None), 'kind')"}, {'allOf':
    [{'XXX TODO XXX': "hasattr(sample_weight, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(sample_weight.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [
    {'XXX TODO XXX': "getattr(sample_weight, 'dtype', None) is None"}, {
    'XXX TODO XXX':
    "getattr(sample_weight, 'dtype', None) not in [np.float64, np.float32]"
    }, {'XXX TODO XXX': "not hasattr(sample_weight, 'sparse')"}, {
    'XXX TODO XXX': 'sample_weight.ndim <= 1'}, {'XXX TODO XXX':
    "sample_weight.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in sample_weight.dtypes])) <= 1'}]}, {
    'anyOf': [{'allOf': [{'XXX TODO XXX':
    "getattr(sample_weight, 'dtype', None) is not None"}, {'XXX TODO XXX':
    "getattr(sample_weight, 'dtype', None) in [np.float64, np.float32]"}]},
    {'XXX TODO XXX': "not hasattr(sample_weight, 'sparse')"}, {
    'XXX TODO XXX': 'sample_weight.ndim <= 1'}, {'XXX TODO XXX':
    "sample_weight.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in sample_weight.dtypes])) <= 1'}]}]}]
    }]}]}, {'anyOf': [{'type': 'object', 'properties': {'base_estimator': {
    'enum': [None]}}}, {'type': 'object', 'properties': {'cv': {'enum': [
    'prefit']}}}, {'type': 'object', 'properties': {'sample_weight': {
    'enum': [None]}}}, {'type': 'object', 'properties': {'sample_weight': {
    'enum': [None]}}}, {'type': 'object', 'properties': {'sample_weight': {
    'type': 'number'}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "hasattr(getattr(sample_weight, 'dtype', None), 'kind')"}, {'allOf': [{
    'XXX TODO XXX': "hasattr(sample_weight, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(sample_weight.dtypes, '__array__')"}]}, {'XXX TODO XXX':
    "not hasattr(sample_weight, 'sparse')"}, {'XXX TODO XXX':
    'sample_weight.ndim <= 1'}, {'XXX TODO XXX':
    "sample_weight.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in sample_weight.dtypes])) <= 1'}]}, {
    'anyOf': [{'XXX TODO XXX':
    "not hasattr(getattr(sample_weight, 'dtype', None), 'kind')"}, {'allOf':
    [{'XXX TODO XXX': "hasattr(sample_weight, 'dtypes')"}, {'XXX TODO XXX':
    "hasattr(sample_weight.dtypes, '__array__')"}]}, {'allOf': [{'anyOf': [
    {'XXX TODO XXX': "getattr(sample_weight, 'dtype', None) is None"}, {
    'XXX TODO XXX':
    "getattr(sample_weight, 'dtype', None) not in [np.float64, np.float32]"
    }, {'XXX TODO XXX': "not hasattr(sample_weight, 'sparse')"}, {
    'XXX TODO XXX': 'sample_weight.ndim <= 1'}, {'XXX TODO XXX':
    "sample_weight.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in sample_weight.dtypes])) <= 1'}]}, {
    'anyOf': [{'allOf': [{'XXX TODO XXX':
    "getattr(sample_weight, 'dtype', None) is not None"}, {'XXX TODO XXX':
    "getattr(sample_weight, 'dtype', None) in [np.float64, np.float32]"}]},
    {'XXX TODO XXX': "not hasattr(sample_weight, 'sparse')"}, {
    'XXX TODO XXX': 'sample_weight.ndim <= 1'}, {'XXX TODO XXX':
    "sample_weight.sparse.to_coo().dtype != np.dtype('object')"}, {
    'XXX TODO XXX':
    'len(set([dt.subtype.name for dt in sample_weight.dtypes])) <= 1'}]}]}]
    }]}]}]}, {'description':
    'From /utils/validation.py:None:check_array, Exception: raise ValueError("""Complex data not supported {} """.format(array)     ) from complex_warning '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'sample_weight': {'enum': [None]
    }}}, {'type': 'object', 'properties': {'sample_weight': {'enum': [None]
    }}}, {'type': 'object', 'properties': {'sample_weight': {'type':
    'number'}}}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    "not hasattr(sample_weight, 'sparse')"}, {'XXX TODO XXX':
    'sample_weight.ndim <= 1'}, {'XXX TODO XXX':
    'sp.issparse(sample_weight.sparse.to_coo())'}]}, {'anyOf': [{'allOf': [
    {'XXX TODO XXX': "hasattr(sample_weight, 'sparse')"}, {'XXX TODO XXX':
    'sample_weight.ndim > 1'}]}, {'XXX TODO XXX':
    'sp.issparse(sample_weight)'}]}]}]}, {'description':
    "From /utils/validation.py:None:check_array, Exception: raise ValueError('Found array with dim %d. %s expected <= 2.' % (array.ndim,     estimator_name)) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'sample_weight': {'enum': [None]
    }}}, {'type': 'object', 'properties': {'sample_weight': {'enum': [None]
    }}}, {'type': 'object', 'properties': {'sample_weight': {'type':
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
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'sample_weight': {'enum': [None]
    }}}, {'type': 'object', 'properties': {'sample_weight': {'enum': [None]
    }}}, {'type': 'object', 'properties': {'sample_weight': {'type':
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
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'sample_weight': {'enum': [None]
    }}}, {'XXX TODO XXX': "not hasattr(X, 'fit')"}, {'XXX TODO XXX':
    'not callable(X.fit)'}]}, {'description':
    'From /utils/validation.py:None:_num_samples, Exception: raise TypeError(message) '
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'sample_weight': {'enum': [None]
    }}}, {'XXX TODO XXX': "hasattr(X, '__len__')"}, {'XXX TODO XXX':
    "hasattr(X, 'shape')"}, {'XXX TODO XXX': "hasattr(X, '__array__')"}]},
    {'description':
    "From /utils/validation.py:None:_num_samples, Exception: raise TypeError(     'Singleton array %r cannot be considered a valid collection.' % x) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'sample_weight': {'enum': [None]
    }}}, {'allOf': [{'anyOf': [{'XXX TODO XXX': "hasattr(X, '__len__')"}, {
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
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'sample_weight': {'enum': [None]
    }}}, {'allOf': [{'anyOf': [{'XXX TODO XXX': "hasattr(X, '__len__')"}, {
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
    "From /utils/validation.py:None:_check_sample_weight, Exception: raise ValueError('Sample weights must be 1D array or scalar') "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'sample_weight': {'enum': [None]
    }}}, {'type': 'object', 'properties': {'sample_weight': {'enum': [None]
    }}}, {'type': 'object', 'properties': {'sample_weight': {'type':
    'number'}}}, {'XXX TODO XXX':
    "check_array(sample_weight, False, False, dtype=[np.float64, np.float32], order='C', False).ndim == 1"
    }]}, {'description':
    "From /utils/validation.py:None:_check_sample_weight, Exception: raise ValueError('sample_weight.shape == {}, expected {}!'.format(     sample_weight.shape, (n_samples,))) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'type': 'object', 'properties': {'sample_weight': {'enum': [None]
    }}}, {'type': 'object', 'properties': {'sample_weight': {'enum': [None]
    }}}, {'type': 'object', 'properties': {'sample_weight': {'type':
    'number'}}}, {'XXX TODO XXX':
    "check_array(sample_weight, False, False, dtype=[np.float64, np.float32], order='C', False).shape == [_num_samples(X)]"
    }]}, {'description':
    "From /model_selection/_split.py:None:check_cv, Exception: raise ValueError(     'Expected cv as an integer, cross-validation object (from sklearn.model_selection) or an iterable. Got %s.'      % cv) "
    , 'anyOf': [{'type': 'object', 'properties': {'cv': {'enum': ['prefit']
    }}}, {'allOf': [{'XXX TODO XXX':
    "hasattr(5 if self.cv is None else self.cv, 'split')"}, {'XXX TODO XXX':
    'isinstance(5 if self.cv is None else self.cv, str)'}]}, {'allOf': [{
    'XXX TODO XXX':
    'isinstance(5 if self.cv is None else self.cv, Iterable)'}, {
    'XXX TODO XXX': 'isinstance(5 if self.cv is None else self.cv, str)'}]}
    ]}, {'description':
    "From /base.py:None:clone, Exception: raise TypeError('Cannot clone object. ' +     'You should provide an instance of ' +     'scikit-learn estimator instead of a class.') "
    , 'allOf': [{'anyOf': [{'type': 'object', 'properties': {
    'base_estimator': {'not': {'enum': [None]}}}}, {'type': 'object',
    'properties': {'cv': {'enum': ['prefit']}}}, {'type': 'object',
    'properties': {'ensemble': {'enum': [False]}}}, {'XXX TODO XXX':
    'type(LinearSVC(random_state=0)) in [list, tuple, set, frozenset]'}, {
    'allOf': [{'XXX TODO XXX':
    "hasattr(LinearSVC(random_state=0), 'get_params')"}, {'XXX TODO XXX':
    'isinstance(LinearSVC(random_state=0), type)'}]}, {'XXX TODO XXX':
    'isinstance(LinearSVC(random_state=0), type)'}]}, {'anyOf': [{'type':
    'object', 'properties': {'base_estimator': {'enum': [None]}}}, {'type':
    'object', 'properties': {'cv': {'enum': ['prefit']}}}, {'type':
    'object', 'properties': {'ensemble': {'enum': [False]}}}, {
    'XXX TODO XXX':
    'type(self.base_estimator) in [list, tuple, set, frozenset]'}, {'allOf':
    [{'XXX TODO XXX': "hasattr(self.base_estimator, 'get_params')"}, {
    'XXX TODO XXX': 'isinstance(self.base_estimator, type)'}]}, {
    'XXX TODO XXX': 'isinstance(self.base_estimator, type)'}]}]}, {
    'description':
    'From /base.py:None:clone, Exception: raise TypeError(     "Cannot clone object \'%s\' (type %s): it does not seem to be a scikit-learn estimator as it does not implement a \'get_params\' method."      % (repr(estimator), type(estimator))) '
    , 'allOf': [{'anyOf': [{'type': 'object', 'properties': {
    'base_estimator': {'not': {'enum': [None]}}}}, {'type': 'object',
    'properties': {'cv': {'enum': ['prefit']}}}, {'type': 'object',
    'properties': {'ensemble': {'enum': [False]}}}, {'XXX TODO XXX':
    'type(LinearSVC(random_state=0)) in [list, tuple, set, frozenset]'}, {
    'allOf': [{'XXX TODO XXX':
    "hasattr(LinearSVC(random_state=0), 'get_params')"}, {'XXX TODO XXX':
    'isinstance(LinearSVC(random_state=0), type)'}]}, {'XXX TODO XXX':
    'isinstance(LinearSVC(random_state=0), type)'}]}, {'anyOf': [{'type':
    'object', 'properties': {'base_estimator': {'enum': [None]}}}, {'type':
    'object', 'properties': {'cv': {'enum': ['prefit']}}}, {'type':
    'object', 'properties': {'ensemble': {'enum': [False]}}}, {
    'XXX TODO XXX':
    'type(self.base_estimator) in [list, tuple, set, frozenset]'}, {'allOf':
    [{'XXX TODO XXX': "hasattr(self.base_estimator, 'get_params')"}, {
    'XXX TODO XXX': 'isinstance(self.base_estimator, type)'}]}, {
    'XXX TODO XXX': 'isinstance(self.base_estimator, type)'}]}]}, {
    'description':
    "From /base.py:None:clone, Exception: raise RuntimeError(     'Cannot clone object %s, as the constructor either does not set or modifies parameter %s'      % (estimator, name)) "
    , 'allOf': [{'anyOf': [{'type': 'object', 'properties': {
    'base_estimator': {'not': {'enum': [None]}}}}, {'type': 'object',
    'properties': {'cv': {'enum': ['prefit']}}}, {'type': 'object',
    'properties': {'ensemble': {'enum': [False]}}}, {'XXX TODO XXX':
    'name not in LinearSVC(random_state=0).get_params(False)'}, {
    'XXX TODO XXX': 'new_object_params[name] is params_set[name]'}]}, {
    'anyOf': [{'type': 'object', 'properties': {'base_estimator': {'enum':
    [None]}}}, {'type': 'object', 'properties': {'cv': {'enum': ['prefit']}
    }}, {'type': 'object', 'properties': {'ensemble': {'enum': [False]}}},
    {'XXX TODO XXX': 'name not in self.base_estimator.get_params(False)'},
    {'XXX TODO XXX': 'new_object_params[name] is params_set[name]'}]}]}, {
    'description':
    "From /base.py:None:clone, Exception: raise TypeError('Cannot clone object. ' +     'You should provide an instance of ' +     'scikit-learn estimator instead of a class.') "
    , 'allOf': [{'anyOf': [{'type': 'object', 'properties': {
    'base_estimator': {'not': {'enum': [None]}}}}, {'type': 'object',
    'properties': {'cv': {'enum': ['prefit']}}}, {'type': 'object',
    'properties': {'ensemble': {'enum': [True]}}}, {'XXX TODO XXX':
    'type(LinearSVC(random_state=0)) in [list, tuple, set, frozenset]'}, {
    'allOf': [{'XXX TODO XXX':
    "hasattr(LinearSVC(random_state=0), 'get_params')"}, {'XXX TODO XXX':
    'isinstance(LinearSVC(random_state=0), type)'}]}, {'XXX TODO XXX':
    'isinstance(LinearSVC(random_state=0), type)'}]}, {'anyOf': [{'type':
    'object', 'properties': {'base_estimator': {'enum': [None]}}}, {'type':
    'object', 'properties': {'cv': {'enum': ['prefit']}}}, {'type':
    'object', 'properties': {'ensemble': {'enum': [True]}}}, {
    'XXX TODO XXX':
    'type(self.base_estimator) in [list, tuple, set, frozenset]'}, {'allOf':
    [{'XXX TODO XXX': "hasattr(self.base_estimator, 'get_params')"}, {
    'XXX TODO XXX': 'isinstance(self.base_estimator, type)'}]}, {
    'XXX TODO XXX': 'isinstance(self.base_estimator, type)'}]}]}, {
    'description':
    'From /base.py:None:clone, Exception: raise TypeError(     "Cannot clone object \'%s\' (type %s): it does not seem to be a scikit-learn estimator as it does not implement a \'get_params\' method."      % (repr(estimator), type(estimator))) '
    , 'allOf': [{'anyOf': [{'type': 'object', 'properties': {
    'base_estimator': {'not': {'enum': [None]}}}}, {'type': 'object',
    'properties': {'cv': {'enum': ['prefit']}}}, {'type': 'object',
    'properties': {'ensemble': {'enum': [True]}}}, {'XXX TODO XXX':
    'type(LinearSVC(random_state=0)) in [list, tuple, set, frozenset]'}, {
    'allOf': [{'XXX TODO XXX':
    "hasattr(LinearSVC(random_state=0), 'get_params')"}, {'XXX TODO XXX':
    'isinstance(LinearSVC(random_state=0), type)'}]}, {'XXX TODO XXX':
    'isinstance(LinearSVC(random_state=0), type)'}]}, {'anyOf': [{'type':
    'object', 'properties': {'base_estimator': {'enum': [None]}}}, {'type':
    'object', 'properties': {'cv': {'enum': ['prefit']}}}, {'type':
    'object', 'properties': {'ensemble': {'enum': [True]}}}, {
    'XXX TODO XXX':
    'type(self.base_estimator) in [list, tuple, set, frozenset]'}, {'allOf':
    [{'XXX TODO XXX': "hasattr(self.base_estimator, 'get_params')"}, {
    'XXX TODO XXX': 'isinstance(self.base_estimator, type)'}]}, {
    'XXX TODO XXX': 'isinstance(self.base_estimator, type)'}]}]}, {
    'description':
    "From /base.py:None:clone, Exception: raise RuntimeError(     'Cannot clone object %s, as the constructor either does not set or modifies parameter %s'      % (estimator, name)) "
    , 'allOf': [{'anyOf': [{'type': 'object', 'properties': {
    'base_estimator': {'not': {'enum': [None]}}}}, {'type': 'object',
    'properties': {'cv': {'enum': ['prefit']}}}, {'type': 'object',
    'properties': {'ensemble': {'enum': [True]}}}, {'XXX TODO XXX':
    'name not in LinearSVC(random_state=0).get_params(False)'}, {
    'XXX TODO XXX': 'new_object_params[name] is params_set[name]'}]}, {
    'anyOf': [{'type': 'object', 'properties': {'base_estimator': {'enum':
    [None]}}}, {'type': 'object', 'properties': {'cv': {'enum': ['prefit']}
    }}, {'type': 'object', 'properties': {'ensemble': {'enum': [True]}}}, {
    'XXX TODO XXX': 'name not in self.base_estimator.get_params(False)'}, {
    'XXX TODO XXX': 'new_object_params[name] is params_set[name]'}]}]}, {
    'description':
    "From /calibration.py:CalibratedClassifierCV:fit, Exception: raise ValueError(     f'Requesting {n_folds}-fold cross-validation but provided less than {n_folds} examples for at least one class.'     ) "
    , 'allOf': [{'anyOf': [{'type': 'object', 'properties': {
    'base_estimator': {'not': {'enum': [None]}}}}, {'type': 'object',
    'properties': {'cv': {'enum': ['prefit']}}}, {'allOf': [{'anyOf': [{
    'type': 'object', 'properties': {'sample_weight': {'enum': [None]}}}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX':
    "'sample_weight' in signature(LinearSVC(random_state=0).fit).parameters"
    }, {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'cv': {'not':
    {'type': 'integer'}}}}, {'type': 'object', 'properties': {'cv': {'enum':
    [False]}}}, {'XXX TODO XXX':
    'not np.any([np.sum(y == class_) < self.cv for class_ in LabelEncoder().fit(y).classes_])'
    }]}, {'anyOf': [{'type': 'object', 'properties': {'cv': {'type':
    'integer'}}}, {'XXX TODO XXX': "not hasattr(self.cv, 'n_splits')"}, {
    'XXX TODO XXX': 'not self.cv.n_splits'}, {'XXX TODO XXX':
    'not np.any([np.sum(y == class_) < self.cv.n_splits for class_ in LabelEncoder().fit(y).classes_])'
    }]}]}]}, {'anyOf': [{'XXX TODO XXX':
    "'sample_weight' not in signature(LinearSVC(random_state=0).fit).parameters"
    }, {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'cv': {'not':
    {'type': 'integer'}}}}, {'type': 'object', 'properties': {'cv': {'enum':
    [False]}}}, {'XXX TODO XXX':
    'not np.any([np.sum(y == class_) < self.cv for class_ in LabelEncoder().fit(y).classes_])'
    }]}, {'anyOf': [{'type': 'object', 'properties': {'cv': {'type':
    'integer'}}}, {'XXX TODO XXX': "not hasattr(self.cv, 'n_splits')"}, {
    'XXX TODO XXX': 'not self.cv.n_splits'}, {'XXX TODO XXX':
    'not np.any([np.sum(y == class_) < self.cv.n_splits for class_ in LabelEncoder().fit(y).classes_])'
    }]}]}]}]}]}, {'anyOf': [{'type': 'object', 'properties': {
    'sample_weight': {'not': {'enum': [None]}}}}, {'allOf': [{'anyOf': [{
    'type': 'object', 'properties': {'cv': {'not': {'type': 'integer'}}}},
    {'type': 'object', 'properties': {'cv': {'enum': [False]}}}, {
    'XXX TODO XXX':
    'not np.any([np.sum(y == class_) < self.cv for class_ in LabelEncoder().fit(y).classes_])'
    }]}, {'anyOf': [{'type': 'object', 'properties': {'cv': {'type':
    'integer'}}}, {'XXX TODO XXX': "not hasattr(self.cv, 'n_splits')"}, {
    'XXX TODO XXX': 'not self.cv.n_splits'}, {'XXX TODO XXX':
    'not np.any([np.sum(y == class_) < self.cv.n_splits for class_ in LabelEncoder().fit(y).classes_])'
    }]}]}]}]}]}, {'anyOf': [{'type': 'object', 'properties': {
    'base_estimator': {'enum': [None]}}}, {'type': 'object', 'properties':
    {'cv': {'enum': ['prefit']}}}, {'allOf': [{'anyOf': [{'type': 'object',
    'properties': {'sample_weight': {'enum': [None]}}}, {'allOf': [{'anyOf':
    [{'XXX TODO XXX':
    "'sample_weight' in signature(self.base_estimator.fit).parameters"}, {
    'allOf': [{'anyOf': [{'type': 'object', 'properties': {'cv': {'not': {
    'type': 'integer'}}}}, {'type': 'object', 'properties': {'cv': {'enum':
    [False]}}}, {'XXX TODO XXX':
    'not np.any([np.sum(y == class_) < self.cv for class_ in LabelEncoder().fit(y).classes_])'
    }]}, {'anyOf': [{'type': 'object', 'properties': {'cv': {'type':
    'integer'}}}, {'XXX TODO XXX': "not hasattr(self.cv, 'n_splits')"}, {
    'XXX TODO XXX': 'not self.cv.n_splits'}, {'XXX TODO XXX':
    'not np.any([np.sum(y == class_) < self.cv.n_splits for class_ in LabelEncoder().fit(y).classes_])'
    }]}]}]}, {'anyOf': [{'XXX TODO XXX':
    "'sample_weight' not in signature(self.base_estimator.fit).parameters"},
    {'allOf': [{'anyOf': [{'type': 'object', 'properties': {'cv': {'not': {
    'type': 'integer'}}}}, {'type': 'object', 'properties': {'cv': {'enum':
    [False]}}}, {'XXX TODO XXX':
    'not np.any([np.sum(y == class_) < self.cv for class_ in LabelEncoder().fit(y).classes_])'
    }]}, {'anyOf': [{'type': 'object', 'properties': {'cv': {'type':
    'integer'}}}, {'XXX TODO XXX': "not hasattr(self.cv, 'n_splits')"}, {
    'XXX TODO XXX': 'not self.cv.n_splits'}, {'XXX TODO XXX':
    'not np.any([np.sum(y == class_) < self.cv.n_splits for class_ in LabelEncoder().fit(y).classes_])'
    }]}]}]}]}]}, {'anyOf': [{'type': 'object', 'properties': {
    'sample_weight': {'not': {'enum': [None]}}}}, {'allOf': [{'anyOf': [{
    'type': 'object', 'properties': {'cv': {'not': {'type': 'integer'}}}},
    {'type': 'object', 'properties': {'cv': {'enum': [False]}}}, {
    'XXX TODO XXX':
    'not np.any([np.sum(y == class_) < self.cv for class_ in LabelEncoder().fit(y).classes_])'
    }]}, {'anyOf': [{'type': 'object', 'properties': {'cv': {'type':
    'integer'}}}, {'XXX TODO XXX': "not hasattr(self.cv, 'n_splits')"}, {
    'XXX TODO XXX': 'not self.cv.n_splits'}, {'XXX TODO XXX':
    'not np.any([np.sum(y == class_) < self.cv.n_splits for class_ in LabelEncoder().fit(y).classes_])'
    }]}]}]}]}]}]}]

