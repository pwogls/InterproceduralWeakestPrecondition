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
        "description": "From /utils/validation.py:None:_assert_all_finite, Exception: raise ValueError(msg_err.format(type_err, msg_dtype if msg_dtype is not     None else X.dtype)) ",
        "anyOf": [
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
        "allOf": [
            {
                "anyOf": [
                    {"XXX TODO XXX": "isinstance(x, [Sequence, spmatrix])"},
                    {"XXX TODO XXX": "hasattr(x, '__array__')"},
                ]
            },
            {"type": "object", "properties": {"x": {"not": {"type": "string"}}}},
        ],
    },
    {
        "description": "From /utils/multiclass.py:None:type_of_target, Exception: raise ValueError(\"y cannot be class 'SparseSeries' or 'SparseArray'\") ",
        "XXX TODO XXX": "x.__class__.__name__ not in ['SparseSeries', 'SparseArray']",
    },
    {
        "description": "From /utils/multiclass.py:None:type_of_target, Exception: raise ValueError(     'You appear to be using a legacy multi-label data representation. Sequence of sequences are no longer supported; use a binary array or sparse matrix instead - the MultiLabelBinarizer transformer can convert to this format.'     ) ",
        "anyOf": [
            {"XXX TODO XXX": "is_multilabel(x)"},
            {"XXX TODO XXX": "hasattr(y[0], '__array__')"},
            {"XXX TODO XXX": "isinstance(y[0], Sequence)"},
            {"XXX TODO XXX": "isinstance(y[0], str)"},
        ],
    },
    {
        "description": "From /utils/multiclass.py:None:unique_labels, Exception: raise ValueError('No argument has been passed.') ",
        "type": "object",
        "properties": {"ys": {"enum": [True]}},
    },
    {
        "description": "From /utils/multiclass.py:None:unique_labels, Exception: raise ValueError('Mix type of y not allowed, got types %s' % ys_types) ",
        "anyOf": [
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
        ],
    },
    {
        "description": "From /utils/multiclass.py:None:unique_labels, Exception: raise ValueError('Mix of label input types (string and number)') ",
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
        ],
    },
    {
        "description": "From /preprocessing/_label.py:LabelBinarizer:fit, Exception: raise ValueError(     'Multioutput target data is not supported with label binarization') ",
        "XXX TODO XXX": "'multioutput' not in type_of_target(y)",
    },
    {
        "description": "From /preprocessing/_label.py:LabelBinarizer:fit, Exception: raise ValueError('y has 0 samples: %r' % y) ",
        "XXX TODO XXX": "_num_samples(y) != 0",
    },
]
