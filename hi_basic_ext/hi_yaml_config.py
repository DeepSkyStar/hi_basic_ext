#!/usr/bin/env python3
# coding=utf-8

from hi_basic import *
import yaml

class HiYamlConfig(HiConfig):
    def _load_config(self):
        if not os.path.exists(self._path):
            if self._auto_create:
                HiFile.ensure_dirs(os.path.split(self._path)[0])
                self._init_config()
        else:
            with open(self._path, "r", encoding="utf-8") as file:
                try:
                    self._items = yaml.safe_load(file)
                    self._filestamp.update()
                    HiLog.debug(f"Load config {self._path}")
                except ValueError:
                    HiLog.warning(f"Config {self._path} broken...")
        pass

    def _save_config(self):
        with open(self._path, "w", encoding="utf-8") as file:
            yaml.safe_dump(self._items, file, indent=4, allow_unicode=True)
        self._filestamp.update()
    pass
