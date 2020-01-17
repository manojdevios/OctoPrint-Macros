// OctoPrint Macros Plugin. Allows user to create customised macro buttons
// Copyright (C) 2020  manojdevios
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Affero General Public License as published
// by the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Affero General Public License for more details.
//
// You should have received a copy of the GNU Affero General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.
//
// Email: manojdevios@gmail.com
//

$(function() {
  function MyCustomViewModel (parameters) {
    var self = this;

    self.settings = parameters[0];

    self.getAdditionalControls = function() {
      var settings = self.settings.settings.settings.plugins.macros

      var baseSettings = [{
        'customClass': '', 'layout': 'horizontal_grid', 'name': 'Macros...', 'children':
          [{'width': '3', 'commands':
            settings.macro1().split('\n'),
          'customClass': 'btn', 'additionalClasses': 'nowrap', 'name': settings.macro1Name},
          {'width': '3', 'commands':
            settings.macro2().split('\n'),
          'customClass': 'btn', 'additionalClasses': 'nowrap', 'name': settings.macro2Name, 'offset': '1'},
          {'width': '3', 'commands':
            settings.macro3().split('\n'),
          'customClass': 'btn', 'additionalClasses': 'nowrap', 'name': settings.macro3Name, 'offset': '1'}]
      }]

      var finalSettings = baseSettings;
      return finalSettings;
    }

  }

  OCTOPRINT_VIEWMODELS.push({
    construct: MyCustomViewModel,
    dependencies: ["controlViewModel"]
  });
})
