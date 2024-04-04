from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_attachments import ApiAttachments
    from ..models.api_field_update import ApiFieldUpdate
    from ..models.api_rich_text import ApiRichText


T = TypeVar("T", bound="ApiItemUpdateWithDescription")


@attr.s(auto_attribs=True)
class ApiItemUpdateWithDescription:
    """
    Attributes:
        details (Union[Unset, None, List['ApiFieldUpdate']]): The list of updates to perform on the different fields of
            the item.
        attachments (Union[Unset, None, ApiAttachments]): Contains all changes to the attachments of an item.
        description (Union[Unset, None, ApiRichText]): Contains some rich text. The rich text is provided in several
            different formats.
            When sending rich text to the server, the rich text must be provided in exactly
            one format.
    """

    details: Union[Unset, None, List["ApiFieldUpdate"]] = UNSET
    attachments: Union[Unset, None, "ApiAttachments"] = UNSET
    description: Union[Unset, None, "ApiRichText"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        details: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.details, Unset):
            if self.details is None:
                details = None
            else:
                details = []
                for details_item_data in self.details:
                    details_item = details_item_data.to_dict()

                    details.append(details_item)

        attachments: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict() if self.attachments else None

        description: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict() if self.description else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if details is not UNSET:
            field_dict["Details"] = details
        if attachments is not UNSET:
            field_dict["Attachments"] = attachments
        if description is not UNSET:
            field_dict["Description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_attachments import ApiAttachments
        from ..models.api_field_update import ApiFieldUpdate
        from ..models.api_rich_text import ApiRichText

        d = src_dict.copy()
        details = []
        _details = d.pop("Details", UNSET)
        for details_item_data in _details or []:
            details_item = ApiFieldUpdate.from_dict(details_item_data)

            details.append(details_item)

        _attachments = d.pop("Attachments", UNSET)
        attachments: Union[Unset, None, ApiAttachments]
        if _attachments is None:
            attachments = None
        elif isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = ApiAttachments.from_dict(_attachments)

        _description = d.pop("Description", UNSET)
        description: Union[Unset, None, ApiRichText]
        if _description is None:
            description = None
        elif isinstance(_description, Unset):
            description = UNSET
        else:
            description = ApiRichText.from_dict(_description)

        api_item_update_with_description = cls(
            details=details,
            attachments=attachments,
            description=description,
        )

        api_item_update_with_description.additional_properties = d
        return api_item_update_with_description

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
