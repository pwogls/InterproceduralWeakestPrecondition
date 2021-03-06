[{'description':
    "From /utils/metaestimators.py:_BaseComposition:_validate_names, Exception: raise ValueError('Names provided are not unique: {0!r}'.format(list(names))) "
    , 'XXX TODO XXX':
    'len(set(zip(*self.estimators)[0])) == len(zip(*self.estimators)[0])'},
    {'description':
    "From /utils/metaestimators.py:_BaseComposition:_validate_names, Exception: raise ValueError('Estimator names conflict with constructor arguments: {0!r}'     .format(sorted(invalid_names))) "
    , 'XXX TODO XXX':
    'not set(zip(*self.estimators)[0]).intersection(self.get_params(False))'
    }, {'description':
    "From /utils/metaestimators.py:_BaseComposition:_validate_names, Exception: raise ValueError('Estimator names must not contain __: got {0!r}'.format(     invalid_names)) "
    , 'allOf': [{'anyOf': [{'allOf': [{'type': 'object', 'properties': {
    'estimators': {'not': {'enum': [None]}}}}, {'XXX TODO XXX':
    'len(self.estimators) != 0'}]}, {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'len(set(zip(*self.estimators)[0])) == len(zip(*self.estimators)[0])'},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'not set(zip(*self.estimators)[0]).intersection(self.get_params(False))'
    }, {'XXX TODO XXX':
    "not [name for name in zip(*self.estimators)[0] if '__' in name]"}]}, {
    'anyOf': [{'XXX TODO XXX':
    'set(zip(*self.estimators)[0]).intersection(self.get_params(False))'},
    {'XXX TODO XXX':
    "not [name for name in zip(*self.estimators)[0] if '__' in name]"}]}]}]
    }, {'anyOf': [{'XXX TODO XXX':
    'len(set(zip(*self.estimators)[0])) != len(zip(*self.estimators)[0])'},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'not set(zip(*self.estimators)[0]).intersection(self.get_params(False))'
    }, {'XXX TODO XXX':
    "not [name for name in zip(*self.estimators)[0] if '__' in name]"}]}, {
    'anyOf': [{'XXX TODO XXX':
    'set(zip(*self.estimators)[0]).intersection(self.get_params(False))'},
    {'XXX TODO XXX':
    "not [name for name in zip(*self.estimators)[0] if '__' in name]"}]}]}]
    }]}]}, {'anyOf': [{'type': 'object', 'properties': {'estimators': {
    'enum': [None]}}}, {'XXX TODO XXX': 'len(self.estimators) == 0'}, {
    'allOf': [{'anyOf': [{'XXX TODO XXX':
    'len(set(zip(*self.estimators)[0])) == len(zip(*self.estimators)[0])'},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'not set(zip(*self.estimators)[0]).intersection(self.get_params(False))'
    }, {'XXX TODO XXX':
    "not [name for name in zip(*self.estimators)[0] if '__' in name]"}]}, {
    'anyOf': [{'XXX TODO XXX':
    'set(zip(*self.estimators)[0]).intersection(self.get_params(False))'},
    {'XXX TODO XXX':
    "not [name for name in zip(*self.estimators)[0] if '__' in name]"}]}]}]
    }, {'anyOf': [{'XXX TODO XXX':
    'len(set(zip(*self.estimators)[0])) != len(zip(*self.estimators)[0])'},
    {'allOf': [{'anyOf': [{'XXX TODO XXX':
    'not set(zip(*self.estimators)[0]).intersection(self.get_params(False))'
    }, {'XXX TODO XXX':
    "not [name for name in zip(*self.estimators)[0] if '__' in name]"}]}, {
    'anyOf': [{'XXX TODO XXX':
    'set(zip(*self.estimators)[0]).intersection(self.get_params(False))'},
    {'XXX TODO XXX':
    "not [name for name in zip(*self.estimators)[0] if '__' in name]"}]}]}]
    }]}]}]}, {'description':
    'From /ensemble/_base.py:_BaseHeterogeneousEnsemble:_validate_estimators, Exception: raise ValueError(     "Invalid \'estimators\' attribute, \'estimators\' should be a list of (string, estimator) tuples."     ) '
    , 'allOf': [{'type': 'object', 'properties': {'estimators': {'not': {
    'enum': [None]}}}}, {'XXX TODO XXX': 'len(self.estimators) != 0'}]}, {
    'description':
    "From /ensemble/_base.py:_BaseHeterogeneousEnsemble:_validate_estimators, Exception: raise ValueError(     'All estimators are dropped. At least one is required to be an estimator.') "
    , 'XXX TODO XXX':
    "any((est != 'drop' for est in zip(*self.estimators)[1]))"}, {
    'description':
    "From /ensemble/_base.py:_BaseHeterogeneousEnsemble:_validate_estimators, Exception: raise ValueError('The estimator {} should be a {}.'.format(est.__class__.     __name__, is_estimator_type.__name__[3:])) "
    , 'anyOf': [{'XXX TODO XXX': 'est not in zip(*self.estimators)[1]'}, {
    'type': 'object', 'properties': {'est': {'enum': ['drop']}}}, {
    'XXX TODO XXX':
    '(is_classifier if is_classifier(self) else is_regressor)(est)'}]}, {
    'description':
    "From /base.py:None:clone, Exception: raise TypeError('Cannot clone object. ' +     'You should provide an instance of ' +     'scikit-learn estimator instead of a class.') "
    , 'anyOf': [{'XXX TODO XXX':
    'type(clf) in [list, tuple, set, frozenset]'}, {'allOf': [{
    'XXX TODO XXX': "hasattr(clf, 'get_params')"}, {'XXX TODO XXX':
    'isinstance(clf, type)'}]}, {'XXX TODO XXX': 'isinstance(clf, type)'}]},
    {'description':
    'From /base.py:None:clone, Exception: raise TypeError(     "Cannot clone object \'%s\' (type %s): it does not seem to be a scikit-learn estimator as it does not implement a \'get_params\' method."      % (repr(estimator), type(estimator))) '
    , 'anyOf': [{'XXX TODO XXX':
    'type(clf) in [list, tuple, set, frozenset]'}, {'allOf': [{
    'XXX TODO XXX': "hasattr(clf, 'get_params')"}, {'XXX TODO XXX':
    'isinstance(clf, type)'}]}, {'XXX TODO XXX': 'isinstance(clf, type)'}]},
    {'description':
    "From /base.py:None:clone, Exception: raise RuntimeError(     'Cannot clone object %s, as the constructor either does not set or modifies parameter %s'      % (estimator, name)) "
    , 'anyOf': [{'XXX TODO XXX': 'name not in clf.get_params(False)'}, {
    'XXX TODO XXX': 'new_object_params[name] is params_set[name]'}]}, {
    'description':
    "From /ensemble/_voting.py:_BaseVoting:fit, Exception: raise ValueError(     'Number of `estimators` and weights must be equal; got %d weights, %d estimators'      % (len(self.weights), len(self.estimators))) "
    , 'anyOf': [{'type': 'object', 'properties': {'weights': {'enum': [None
    ]}}}, {'XXX TODO XXX': 'len(self.weights) == len(self.estimators)'}]}]

