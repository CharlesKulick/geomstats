import numpy as _np

from geomstats._backend._dtype_utils import (
    _dyn_update_dtype,
    _modify_func_default_dtype,
)
from geomstats._backend._dtype_utils import _np_box_binary_scalar as _box_binary_scalar
from geomstats._backend._dtype_utils import _np_box_unary_scalar as _box_unary_scalar
from geomstats._backend._dtype_utils import (
    _pre_add_default_dtype_by_casting,
    _pre_allow_complex_dtype,
    _pre_cast_fout_to_input_dtype,
    _pre_cast_out_from_dtype,
    _pre_cast_out_to_input_dtype,
    _pre_set_default_dtype,
    get_default_cdtype,
    get_default_dtype,
)

from ._common import cast

_COMPLEX_DTYPES = (
    _np.complex64,
    _np.complex128,
)


def is_floating(x):
    return x.dtype.kind == "f"


def is_complex(x):
    return x.dtype.kind == "c"


def is_bool(x):
    return x.dtype.kind == "b"


def as_dtype(value):
    """Transform string representing dtype in dtype."""
    return _np.dtype(value)


def _dtype_as_str(dtype):
    return dtype.name


set_default_dtype = _pre_set_default_dtype(as_dtype)

_add_default_dtype_by_casting = _pre_add_default_dtype_by_casting(cast)
_cast_fout_to_input_dtype = _pre_cast_fout_to_input_dtype(cast, is_floating)
_cast_out_to_input_dtype = _pre_cast_out_to_input_dtype(
    cast, is_floating, is_complex, as_dtype, _dtype_as_str
)
_cast_out_from_dtype = _pre_cast_out_from_dtype(cast, is_floating, is_complex)
_allow_complex_dtype = _pre_allow_complex_dtype(cast, _COMPLEX_DTYPES)
