# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Support for the CodeSystemDefNode."""
from google.fhir.core.execution import element_node


class CodeSystemDefNode(element_node.ElementNode):
  """Defines a code system identifier that can then be used to identify code systems involved in value set definitions."""

  def __init__(
      self,
      result_type_name=None,
      result_type_specifier=None,
      name=None,
      id_=None,
      version=None,
      access_level='Public',
  ):
    super().__init__(result_type_name, result_type_specifier)
    self.name = name
    self.id_ = id_
    self.version = version
    self.access_level = access_level
