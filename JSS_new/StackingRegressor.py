[
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
            {"XXX TODO XXX": "type(RidgeCV()) in [list, tuple, set, frozenset]"},
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(RidgeCV(), 'get_params')"},
                    {"XXX TODO XXX": "isinstance(RidgeCV(), type)"},
                ]
            },
            {"XXX TODO XXX": "isinstance(RidgeCV(), type)"},
        ],
    },
    {
        "description": "From /base.py:None:clone, Exception: raise TypeError(     \"Cannot clone object '%s' (type %s): it does not seem to be a scikit-learn estimator as it does not implement a 'get_params' method.\"      % (repr(estimator), type(estimator))) ",
        "anyOf": [
            {
                "type": "object",
                "properties": {"final_estimator": {"not": {"enum": [None]}}},
            },
            {"XXX TODO XXX": "type(RidgeCV()) in [list, tuple, set, frozenset]"},
            {
                "allOf": [
                    {"XXX TODO XXX": "hasattr(RidgeCV(), 'get_params')"},
                    {"XXX TODO XXX": "isinstance(RidgeCV(), type)"},
                ]
            },
            {"XXX TODO XXX": "isinstance(RidgeCV(), type)"},
        ],
    },
    {
        "description": "From /base.py:None:clone, Exception: raise RuntimeError(     'Cannot clone object %s, as the constructor either does not set or modifies parameter %s'      % (estimator, name)) ",
        "anyOf": [
            {
                "type": "object",
                "properties": {"final_estimator": {"not": {"enum": [None]}}},
            },
            {"XXX TODO XXX": "name not in RidgeCV().get_params(False)"},
            {"XXX TODO XXX": "new_object_params[name] is params_set[name]"},
        ],
    },
    {
        "description": "From /ensemble/_stacking.py:StackingRegressor:_validate_final_estimator, Exception: raise ValueError(\"'final_estimator' parameter should be a regressor. Got {}\"     .format(self.final_estimator_)) ",
        "XXX TODO XXX": "is_regressor(self.final_estimator_)",
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
