[
    {
        "description": "From /utils/validation.py:None:_assert_all_finite, Exception: raise ValueError(msg_err.format(type_err, msg_dtype if msg_dtype is not     None else X.dtype)) ",
        "anyOf": [
            {"XXX TODO XXX": "is_multilabel(y)"},
            {"XXX TODO XXX": "y.ndim > 2"},
            {
                "allOf": [
                    {"XXX TODO XXX": "y.dtype == object"},
                    {"XXX TODO XXX": "len(y)"},
                    {"XXX TODO XXX": "isinstance(y.flat[0], str)"},
                ]
            },
            {
                "allOf": [
                    {"XXX TODO XXX": "y.ndim == 2"},
                    {"XXX TODO XXX": "y.shape[1] == 0"},
                ]
            },
            {"XXX TODO XXX": "y.dtype.kind != 'f'"},
            {"XXX TODO XXX": "not np.any(y != y.astype(int))"},
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
            {"XXX TODO XXX": "is_multilabel(y)"},
            {"XXX TODO XXX": "y.ndim > 2"},
            {
                "allOf": [
                    {"XXX TODO XXX": "y.dtype == object"},
                    {"XXX TODO XXX": "len(y)"},
                    {"XXX TODO XXX": "isinstance(y.flat[0], str)"},
                ]
            },
            {
                "allOf": [
                    {"XXX TODO XXX": "y.ndim == 2"},
                    {"XXX TODO XXX": "y.shape[1] == 0"},
                ]
            },
            {"XXX TODO XXX": "y.dtype.kind != 'f'"},
            {"XXX TODO XXX": "not np.any(y != y.astype(int))"},
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
        "description": "From /utils/multiclass.py:None:type_of_target, Exception: raise ValueError(     'Expected array-like (array or non-string sequence), got %r' % y) ",
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "isinstance(y, [Sequence, spmatrix])"},
                    {"XXX TODO XXX": "hasattr(y, '__array__')"},
                ]
            },
            {"type": "object", "properties": {"y": {"not": {"type": "string"}}}},
        ],
    },
    {
        "description": "From /utils/multiclass.py:None:type_of_target, Exception: raise ValueError(\"y cannot be class 'SparseSeries' or 'SparseArray'\") ",
        "XXX TODO XXX": "y.__class__.__name__ not in ['SparseSeries', 'SparseArray']",
    },
    {
        "description": "From /utils/multiclass.py:None:type_of_target, Exception: raise ValueError(     'You appear to be using a legacy multi-label data representation. Sequence of sequences are no longer supported; use a binary array or sparse matrix instead - the MultiLabelBinarizer transformer can convert to this format.'     ) ",
        "anyOf": [
            {"XXX TODO XXX": "is_multilabel(y)"},
            {"XXX TODO XXX": "hasattr(y[0], '__array__')"},
            {"XXX TODO XXX": "isinstance(y[0], Sequence)"},
            {"XXX TODO XXX": "isinstance(y[0], str)"},
        ],
    },
    {
        "description": "From /utils/multiclass.py:None:check_classification_targets, Exception: raise ValueError('Unknown label type: %r' % y_type) ",
        "XXX TODO XXX": "type_of_target(y) in ['binary', 'multiclass', 'multiclass-multioutput', 'multilabel-indicator', 'multilabel-sequences']",
    },
    {
        "description": "From /utils/metaestimators.py:_BaseComposition:_validate_names, Exception: raise ValueError('Names provided are not unique: {0!r}'.format(list(names))) ",
        "XXX TODO XXX": "len(set(zip(*self.estimators)[0])) == len(zip(*self.estimators)[0])",
    },
    {
        "description": "From /utils/metaestimators.py:_BaseComposition:_validate_names, Exception: raise ValueError('Estimator names conflict with constructor arguments: {0!r}'     .format(sorted(invalid_names))) ",
        "XXX TODO XXX": "not set(zip(*self.estimators)[0]).intersection(self.get_params(False))",
    },
    {
        "description": "From /utils/metaestimators.py:_BaseComposition:_validate_names, Exception: raise ValueError('Estimator names must not contain __: got {0!r}'.format(     invalid_names)) ",
        "allOf": [
            {
                "anyOf": [
                    {
                        "allOf": [
                            {
                                "type": "object",
                                "properties": {"estimators": {"not": {"enum": [None]}}},
                            },
                            {"XXX TODO XXX": "len(self.estimators) != 0"},
                        ]
                    },
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "len(set(zip(*self.estimators)[0])) == len(zip(*self.estimators)[0])"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "not set(zip(*self.estimators)[0]).intersection(self.get_params(False))"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not [name for name in zip(*self.estimators)[0] if '__' in name]"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "set(zip(*self.estimators)[0]).intersection(self.get_params(False))"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not [name for name in zip(*self.estimators)[0] if '__' in name]"
                                                    },
                                                ]
                                            },
                                        ]
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "len(set(zip(*self.estimators)[0])) != len(zip(*self.estimators)[0])"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "not set(zip(*self.estimators)[0]).intersection(self.get_params(False))"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not [name for name in zip(*self.estimators)[0] if '__' in name]"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "set(zip(*self.estimators)[0]).intersection(self.get_params(False))"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not [name for name in zip(*self.estimators)[0] if '__' in name]"
                                                    },
                                                ]
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
                    {"type": "object", "properties": {"estimators": {"enum": [None]}}},
                    {"XXX TODO XXX": "len(self.estimators) == 0"},
                    {
                        "allOf": [
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "len(set(zip(*self.estimators)[0])) == len(zip(*self.estimators)[0])"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "not set(zip(*self.estimators)[0]).intersection(self.get_params(False))"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not [name for name in zip(*self.estimators)[0] if '__' in name]"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "set(zip(*self.estimators)[0]).intersection(self.get_params(False))"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not [name for name in zip(*self.estimators)[0] if '__' in name]"
                                                    },
                                                ]
                                            },
                                        ]
                                    },
                                ]
                            },
                            {
                                "anyOf": [
                                    {
                                        "XXX TODO XXX": "len(set(zip(*self.estimators)[0])) != len(zip(*self.estimators)[0])"
                                    },
                                    {
                                        "allOf": [
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "not set(zip(*self.estimators)[0]).intersection(self.get_params(False))"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not [name for name in zip(*self.estimators)[0] if '__' in name]"
                                                    },
                                                ]
                                            },
                                            {
                                                "anyOf": [
                                                    {
                                                        "XXX TODO XXX": "set(zip(*self.estimators)[0]).intersection(self.get_params(False))"
                                                    },
                                                    {
                                                        "XXX TODO XXX": "not [name for name in zip(*self.estimators)[0] if '__' in name]"
                                                    },
                                                ]
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
        "description": "From /ensemble/_base.py:_BaseHeterogeneousEnsemble:_validate_estimators, Exception: raise ValueError(     \"Invalid 'estimators' attribute, 'estimators' should be a list of (string, estimator) tuples.\"     ) ",
        "allOf": [
            {"type": "object", "properties": {"estimators": {"not": {"enum": [None]}}}},
            {"XXX TODO XXX": "len(self.estimators) != 0"},
        ],
    },
    {
        "description": "From /ensemble/_base.py:_BaseHeterogeneousEnsemble:_validate_estimators, Exception: raise ValueError(     'All estimators are dropped. At least one is required to be an estimator.') ",
        "XXX TODO XXX": "any((est != 'drop' for est in zip(*self.estimators)[1]))",
    },
    {
        "description": "From /ensemble/_base.py:_BaseHeterogeneousEnsemble:_validate_estimators, Exception: raise ValueError('The estimator {} should be a {}.'.format(est.__class__.     __name__, is_estimator_type.__name__[3:])) ",
        "anyOf": [
            {"XXX TODO XXX": "est not in zip(*self.estimators)[1]"},
            {"type": "object", "properties": {"est": {"enum": ["drop"]}}},
            {
                "XXX TODO XXX": "(is_classifier if is_classifier(self) else is_regressor)(est)"
            },
        ],
    },
    {
        "description": "From /base.py:None:clone, Exception: raise TypeError('Cannot clone object. ' +     'You should provide an instance of ' +     'scikit-learn estimator instead of a class.') ",
        "anyOf": [
            {"type": "object", "properties": {"final_estimator": {"enum": [None]}}},
            {
                "XXX TODO XXX": "type(self.final_estimator) in [list, tuple, set, frozenset]"
            },
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(self.final_estimator, 'get_params')"},
                    {"XXX TODO XXX": "isinstance(self.final_estimator, type)"},
                ]
            },
            {"XXX TODO XXX": "isinstance(self.final_estimator, type)"},
        ],
    },
    {
        "description": "From /base.py:None:clone, Exception: raise TypeError(     \"Cannot clone object '%s' (type %s): it does not seem to be a scikit-learn estimator as it does not implement a 'get_params' method.\"      % (repr(estimator), type(estimator))) ",
        "anyOf": [
            {"type": "object", "properties": {"final_estimator": {"enum": [None]}}},
            {
                "XXX TODO XXX": "type(self.final_estimator) in [list, tuple, set, frozenset]"
            },
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(self.final_estimator, 'get_params')"},
                    {"XXX TODO XXX": "isinstance(self.final_estimator, type)"},
                ]
            },
            {"XXX TODO XXX": "isinstance(self.final_estimator, type)"},
        ],
    },
    {
        "description": "From /base.py:None:clone, Exception: raise RuntimeError(     'Cannot clone object %s, as the constructor either does not set or modifies parameter %s'      % (estimator, name)) ",
        "anyOf": [
            {"type": "object", "properties": {"final_estimator": {"enum": [None]}}},
            {"XXX TODO XXX": "name not in self.final_estimator.get_params(False)"},
            {"XXX TODO XXX": "new_object_params[name] is params_set[name]"},
        ],
    },
    {
        "description": "From /base.py:None:clone, Exception: raise TypeError('Cannot clone object. ' +     'You should provide an instance of ' +     'scikit-learn estimator instead of a class.') ",
        "anyOf": [
            {
                "type": "object",
                "properties": {"final_estimator": {"not": {"enum": [None]}}},
            },
            {
                "XXX TODO XXX": "type(LogisticRegression()) in [list, tuple, set, frozenset]"
            },
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(LogisticRegression(), 'get_params')"},
                    {"XXX TODO XXX": "isinstance(LogisticRegression(), type)"},
                ]
            },
            {"XXX TODO XXX": "isinstance(LogisticRegression(), type)"},
        ],
    },
    {
        "description": "From /base.py:None:clone, Exception: raise TypeError(     \"Cannot clone object '%s' (type %s): it does not seem to be a scikit-learn estimator as it does not implement a 'get_params' method.\"      % (repr(estimator), type(estimator))) ",
        "anyOf": [
            {
                "type": "object",
                "properties": {"final_estimator": {"not": {"enum": [None]}}},
            },
            {
                "XXX TODO XXX": "type(LogisticRegression()) in [list, tuple, set, frozenset]"
            },
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(LogisticRegression(), 'get_params')"},
                    {"XXX TODO XXX": "isinstance(LogisticRegression(), type)"},
                ]
            },
            {"XXX TODO XXX": "isinstance(LogisticRegression(), type)"},
        ],
    },
    {
        "description": "From /base.py:None:clone, Exception: raise RuntimeError(     'Cannot clone object %s, as the constructor either does not set or modifies parameter %s'      % (estimator, name)) ",
        "anyOf": [
            {
                "type": "object",
                "properties": {"final_estimator": {"not": {"enum": [None]}}},
            },
            {"XXX TODO XXX": "name not in LogisticRegression().get_params(False)"},
            {"XXX TODO XXX": "new_object_params[name] is params_set[name]"},
        ],
    },
    {
        "description": "From /ensemble/_stacking.py:StackingClassifier:_validate_final_estimator, Exception: raise ValueError(\"'final_estimator' parameter should be a classifier. Got {}\"     .format(self.final_estimator_)) ",
        "XXX TODO XXX": "is_classifier(self.final_estimator_)",
    },
    {
        "description": "From /base.py:None:clone, Exception: raise TypeError('Cannot clone object. ' +     'You should provide an instance of ' +     'scikit-learn estimator instead of a class.') ",
        "anyOf": [
            {"XXX TODO XXX": "type(est) in [list, tuple, set, frozenset]"},
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(est, 'get_params')"},
                    {"XXX TODO XXX": "isinstance(est, type)"},
                ]
            },
            {"XXX TODO XXX": "isinstance(est, type)"},
        ],
    },
    {
        "description": "From /base.py:None:clone, Exception: raise TypeError(     \"Cannot clone object '%s' (type %s): it does not seem to be a scikit-learn estimator as it does not implement a 'get_params' method.\"      % (repr(estimator), type(estimator))) ",
        "anyOf": [
            {"XXX TODO XXX": "type(est) in [list, tuple, set, frozenset]"},
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(est, 'get_params')"},
                    {"XXX TODO XXX": "isinstance(est, type)"},
                ]
            },
            {"XXX TODO XXX": "isinstance(est, type)"},
        ],
    },
    {
        "description": "From /base.py:None:clone, Exception: raise RuntimeError(     'Cannot clone object %s, as the constructor either does not set or modifies parameter %s'      % (estimator, name)) ",
        "anyOf": [
            {"XXX TODO XXX": "name not in est.get_params(False)"},
            {"XXX TODO XXX": "new_object_params[name] is params_set[name]"},
        ],
    },
    {
        "description": "From /base.py:None:clone, Exception: raise TypeError('Cannot clone object. ' +     'You should provide an instance of ' +     'scikit-learn estimator instead of a class.') ",
        "anyOf": [
            {"XXX TODO XXX": "type(est) in [list, tuple, set, frozenset]"},
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(est, 'get_params')"},
                    {"XXX TODO XXX": "isinstance(est, type)"},
                ]
            },
            {"XXX TODO XXX": "isinstance(est, type)"},
        ],
    },
    {
        "description": "From /base.py:None:clone, Exception: raise TypeError(     \"Cannot clone object '%s' (type %s): it does not seem to be a scikit-learn estimator as it does not implement a 'get_params' method.\"      % (repr(estimator), type(estimator))) ",
        "anyOf": [
            {"XXX TODO XXX": "type(est) in [list, tuple, set, frozenset]"},
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(est, 'get_params')"},
                    {"XXX TODO XXX": "isinstance(est, type)"},
                ]
            },
            {"XXX TODO XXX": "isinstance(est, type)"},
        ],
    },
    {
        "description": "From /base.py:None:clone, Exception: raise RuntimeError(     'Cannot clone object %s, as the constructor either does not set or modifies parameter %s'      % (estimator, name)) ",
        "anyOf": [
            {"XXX TODO XXX": "name not in est.get_params(False)"},
            {"XXX TODO XXX": "new_object_params[name] is params_set[name]"},
        ],
    },
    {
        "description": "From /model_selection/_split.py:None:check_cv, Exception: raise ValueError(     'Expected cv as an integer, cross-validation object (from sklearn.model_selection) or an iterable. Got %s.'      % cv) ",
        "anyOf": [
            {
                "allOf": [
                    {
                        "XXX TODO XXX": "hasattr(5 if self.cv is None else self.cv, 'split')"
                    },
                    {
                        "XXX TODO XXX": "isinstance(5 if self.cv is None else self.cv, str)"
                    },
                ]
            },
            {
                "allOf": [
                    {
                        "XXX TODO XXX": "isinstance(5 if self.cv is None else self.cv, Iterable)"
                    },
                    {
                        "XXX TODO XXX": "isinstance(5 if self.cv is None else self.cv, str)"
                    },
                ]
            },
        ],
    },
    {
        "description": "From /ensemble/_stacking.py:_BaseStacking:_method_name, Exception: raise ValueError('Underlying estimator {} does not implement the method {}.'     .format(name, method)) ",
        "anyOf": [
            {"type": "object", "properties": {"est": {"enum": ["drop"]}}},
            {"type": "object", "properties": {"meth": {"enum": ["auto"]}}},
            {"XXX TODO XXX": "hasattr(est, meth)"},
        ],
    },
    {
        "description": "From /ensemble/_base.py:None:_fit_single_estimator, Exception: raise TypeError('Underlying estimator {} does not support sample weights.'.     format(estimator.__class__.__name__)) from exc ",
        "anyOf": [
            {"type": "object", "properties": {"sample_weight": {"enum": [None]}}},
            {
                "XXX TODO XXX": "\"unexpected keyword argument 'sample_weight'\" not in str(exc)"
            },
        ],
    },
    {
        "description": "From /ensemble/_base.py:None:_fit_single_estimator, Exception: raise ",
        "type": "object",
        "properties": {"sample_weight": {"enum": [None]}},
    },
]
