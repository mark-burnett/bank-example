from bank import dispatcher

import pkg_resources


def make_dispatcher(storage):
    handlers = {}
    for ep in pkg_resources.iter_entry_points('bank_handler_modules'):
        module = ep.load()
        handlers[module.Request] = module.Handler(storage=storage)

    return dispatcher.Dispatcher(handlers)
