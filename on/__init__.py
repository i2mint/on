import os
from on.util import ModuleNotFoundIgnore

file_sep = os.path.sep

from on.util import lazyprop, groupby, regroupby, igroupby
from on.trans import add_ipython_key_completions

# Imports to be able to easily get started...
from on.base import (
    Collection,
    KvReader,
    KvPersister,
    Reader,
    Persister,
    kv_walk,
)

from on.stores.local_store import (
    LocalStore,
    LocalBinaryStore,
    LocalTextStore,
    LocalPickleStore,
    LocalJsonStore,
)
from on.stores.local_store import (
    QuickStore,
    QuickBinaryStore,
    QuickTextStore,
    QuickJsonStore,
    QuickPickleStore,
)
from on.stores.local_store import DirReader, DirStore

from on.misc import (
    MiscGetter,
    MiscGetterAndSetter,
    misc_objs,
    misc_objs_get,
    get_obj,
    set_obj,
)
from on.base import Store
from on.trans import (
    wrap_kvs,
    disable_delitem,
    disable_setitem,
    mk_read_only,
    kv_wrap,
    cached_keys,
    filt_iter,
    filtered_iter,
    add_path_get,
    insert_aliases,
)
from on.trans import cache_iter  # being deprecated
from on.access import (
    user_configs_dict,
    user_configs,
    user_defaults_dict,
    user_defaults,
)
from on.caching import (
    mk_cached_store,
    store_cached,
    store_cached_with_single_key,
    ensure_clear_to_kv_store,
    flush_on_exit,
    mk_write_cached_store,
)

from on.appendable import (
    appendable
)

from on.stores.local_store import (
    PickleStore,
)  # consider deprecating and use LocalPickleStore instead?
from on.slib.s_zipfile import (
    ZipReader,
    ZipFilesReader,
    FilesOfZip,
    FlatZipFilesReader,
)

with ModuleNotFoundIgnore():
    from on.access import myconfigs
with ModuleNotFoundIgnore():
    from on.access import mystores

with ModuleNotFoundIgnore():
    from on.stores.s3_store import (
        S3BinaryStore,
        S3TextStore,
        S3PickleStore,
    )
with ModuleNotFoundIgnore():
    from on.stores.mongo_store import (
        MongoStore,
        MongoTupleKeyStore,
        MongoAnyKeyStore,
    )


def kvhead(store, n=1):
    """Get the first item of a kv store, or a list of the first n items"""
    if n == 1:
        for k in store:
            return k, store[k]
    else:
        return [(k, store[k]) for i, k in enumerate(store) if i < n]


def ihead(store, n=1):
    """Get the first item of an iterable, or a list of the first n items"""
    if n == 1:
        for item in iter(store):
            return item
    else:
        return [item for i, item in enumerate(store) if i < n]