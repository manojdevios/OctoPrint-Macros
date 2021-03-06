# OctoPrint Macros Plugin. Allows user to create customised macro buttons
# Copyright (C) 2020  manojdevios
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Email: manojdevios@gmail.com
#
# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class MacrosPlugin(octoprint.plugin.StartupPlugin,
		octoprint.plugin.TemplatePlugin,
		octoprint.plugin.SettingsPlugin,
		octoprint.plugin.AssetPlugin):
    def on_after_startup(self):
        self._logger.info("Hello World! %s" %__plugin_description__)
    def get_settings_defaults(self):
        return dict(macro1="G28; Home XYZ",
			macro1Name = "Home All Axis",
			macro2="G28\nG90 \nG1 Z30 F200\nG1 Y30 F3000\nG1 X30 F3000",
			macro2Name = "Ready to Extrude",
			macro3="",
			macro3Name = "Macro 3",)
    def get_template_configs(self):
        return [
            dict(type="settings", custom_bindings=False)
        ]
    def get_assets(self):
        return dict(
            js=["js/macros.js"],
            css=["css/macros.css"]
        )
    def get_update_information(self):
        return dict(
            macros=dict(
                displayName="Macros",
                displayVersion=self._plugin_version,

                # version check: github repository
                type="github_release",
                user="manojdevios",
                repo="OctoPrint-Macros",
                current=self._plugin_version,

                # update method: pip w/ dependency links
                pip="https://github.com/manojdevios/OctoPrint-Macros/archive/{target_version}.zip"
            )
        )


# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "Macros"
__plugin_version__ = "0.1.3"
__plugin_description__ = "This ia an awesome plugin to create user definable macro buttons"
#__plugin_implementation__ = MacrosPlugin()

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = MacrosPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
