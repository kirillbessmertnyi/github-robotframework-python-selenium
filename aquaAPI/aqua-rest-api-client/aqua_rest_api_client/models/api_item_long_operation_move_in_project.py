from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_item_long_operation_domain import ApiItemLongOperationDomain


T = TypeVar("T", bound="ApiItemLongOperationMoveInProject")


@attr.s(auto_attribs=True)
class ApiItemLongOperationMoveInProject:
    """Represents request to move items to a given folder (in scope of the same project)

    Attributes:
        criteria (Union[Unset, None, ApiItemLongOperationDomain]): Defines set of items to be processed.
        target_folder_id (Union[Unset, int]): Id of the target folder. Use zero for root folder.
    """

    criteria: Union[Unset, None, "ApiItemLongOperationDomain"] = UNSET
    target_folder_id: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        criteria: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.criteria, Unset):
            criteria = self.criteria.to_dict() if self.criteria else None

        target_folder_id = self.target_folder_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if criteria is not UNSET:
            field_dict["Criteria"] = criteria
        if target_folder_id is not UNSET:
            field_dict["TargetFolderId"] = target_folder_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_item_long_operation_domain import ApiItemLongOperationDomain

        d = src_dict.copy()
        _criteria = d.pop("Criteria", UNSET)
        criteria: Union[Unset, None, ApiItemLongOperationDomain]
        if _criteria is None:
            criteria = None
        elif isinstance(_criteria, Unset):
            criteria = UNSET
        else:
            criteria = ApiItemLongOperationDomain.from_dict(_criteria)

        target_folder_id = d.pop("TargetFolderId", UNSET)

        api_item_long_operation_move_in_project = cls(
            criteria=criteria,
            target_folder_id=target_folder_id,
        )

        return api_item_long_operation_move_in_project
