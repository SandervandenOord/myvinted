from abc import ABC
from typing import Any

from pydantic import Field

from myvinted.dataclasses.base import BaseModelAdj


class Thumbnail(BaseModelAdj):
    type: str
    url: str
    width: int
    height: int
    original_size: bool | None


class HighResolution(BaseModelAdj):
    id: str
    timestamp: int
    orientation: str | None


class Photo(BaseModelAdj, ABC):
    id: int
    width: int
    height: int
    dominant_color: str
    dominant_color_opaque: str
    url: str
    thumbnails: list[Thumbnail]
    high_resolution: HighResolution | None
    is_suspicious: bool
    full_size_url: str
    is_hidden: bool
    extra: dict[str, Any]


class ItemPhoto(Photo):
    image_no: int
    is_main: bool


class UserPhoto(Photo):
    temp_uuid: None
    orientation: None


class Discount(BaseModelAdj):
    minimal_item_count: int
    fraction: str


class BundleDiscount(BaseModelAdj):
    id: int
    user_id: int
    enabled: bool
    minimal_item_count: int
    fraction: str
    discounts: list[Discount]


class Email(BaseModelAdj):
    valid: bool
    available: bool


class Facebook(BaseModelAdj):
    valid: bool
    verified_at: str | None
    available: bool


class Google(BaseModelAdj):
    valid: bool
    verified_at: str | None
    available: bool


class Phone(BaseModelAdj):
    valid: bool
    verified_at: str
    available: bool


class Verification(BaseModelAdj):
    email: Email
    facebook: Facebook
    google: Google
    phone: Phone


class AcceptedPayInMethod(BaseModelAdj):
    id: int
    code: str
    requires_credit_card: bool
    event_tracking_code: str
    icon: str
    enabled: bool
    translated_name: str
    note: str
    method_change_possible: bool


class User(BaseModelAdj):
    id: int
    anon_id: str
    login: str
    real_name: str | None
    email: str | None
    birthday: str | None
    gender: str
    item_count: int
    msg_template_count: int
    given_item_count: int
    taken_item_count: int
    favourite_topic_count: int
    forum_msg_count: int
    forum_topic_count: int
    followers_count: int
    following_count: int
    following_brands_count: int
    positive_feedback_count: int
    neutral_feedback_count: int
    negative_feedback_count: int
    meeting_transaction_count: int
    account_status: int
    email_bounces: str | None
    feedback_reputation: float
    feedback_count: int
    account_ban_date: str | None
    is_account_ban_permanent: str | None
    is_forum_ban_permanent: str | None
    is_on_holiday: bool
    is_publish_photos_agreed: bool
    expose_location: bool
    third_party_tracking: bool
    default_address: str | None
    last_loged_on_ts: str
    city_id: int
    city: str
    country_id: int
    country_code: str
    country_iso_code: str
    country_title: str
    contacts_permission: str | None
    contacts: str | None
    photo: UserPhoto
    path: str
    moderator: bool
    is_catalog_moderator: bool
    is_catalog_role_marketing_photos: bool
    hide_feedback: bool
    can_post_big_forum_photos: bool
    allow_direct_messaging: bool
    bundle_discount: BundleDiscount
    donation_configuration: str | None
    fundraiser: str | None
    business: bool
    business_account: str | None
    has_ship_fast_badge: bool
    total_items_count: int
    about: str
    verification: Verification
    avg_response_time: str | None
    carrier_ids: list[int]
    carriers_without_custom_ids: list[int]
    locale: str
    updated_on: int
    is_hated: bool
    hates_you: bool
    is_favourite: bool
    profile_url: str
    share_profile_url: str
    facebook_user_id: str | None
    is_online: bool
    can_view_profile: bool
    can_bundle: bool
    country_title_local: str
    last_loged_on: str
    accepted_pay_in_methods: list[AcceptedPayInMethod]
    localization: str
    is_bpf_price_prominence_applied: bool


class Price(BaseModelAdj):
    amount: str
    currency_code: str


class BrandDto(BaseModelAdj):
    id: int
    title: str
    slug: str
    favourite_count: int
    pretty_favourite_count: str
    item_count: int
    pretty_item_count: str
    is_visible_in_listings: bool
    requires_authenticity_check: bool
    is_luxury: bool
    is_hvf: bool
    path: str
    url: str
    is_favourite: bool


class AcceptedPayInMethod1(BaseModelAdj):
    id: int
    code: str
    requires_credit_card: bool
    event_tracking_code: str
    icon: str
    enabled: bool
    translated_name: str
    note: str
    method_change_possible: bool


class Item(BaseModelAdj):
    id: int
    title: str
    brand_id: int
    size_id: int
    status_id: int
    disposal_conditions: int
    user_id: int
    owner_id: str | None
    country_id: int
    catalog_id: int
    color1_id: int
    color2_id: int
    package_size_id: int
    is_hidden: int
    is_reserved: int
    reserved_for_user_id: str | None
    is_visible: int
    is_unisex: int
    is_closed: int
    active_bid_count: int
    favourite_count: int
    view_count: int
    moderation_status: int
    last_push_up_at: str
    description: str
    package_size_standard: bool
    item_closing_action: str | None
    related_catalog_ids: list
    related_catalogs_enabled: bool
    size: str
    brand: str
    composition: str
    extra_conditions: str
    is_for_sell: bool
    is_for_swap: bool
    is_for_give_away: bool
    is_handicraft: bool
    is_processing: bool
    is_draft: bool
    label: str
    real_value_numeric: str | None
    original_price_numeric: str
    currency: str
    price_numeric: str
    created_at_ts: str
    updated_at_ts: str
    user_updated_at_ts: str
    photos: list[ItemPhoto]
    push_up_interval: int
    can_be_sold: bool
    can_feedback: bool
    item_reservation_id: str | None
    receiver_id: str | None
    promoted_until: str | None
    promoted_internationally: str | None
    discount_price_numeric: str | None
    author: str | None
    book_title: str | None
    isbn: str | None
    measurement_width: str | None
    measurement_length: str | None
    measurement_unit: str | None
    transaction_permitted: bool
    video_game_rating_id: str | None
    item_attributes: list
    is_story_uploaded: bool
    haov_item_: bool = Field(..., alias="haov_item?")
    user: User
    price: Price
    discount_price: str | None
    service_fee: str
    total_item_price: str
    total_item_price_rounded: str | None
    can_edit: bool
    can_delete: bool
    can_reserve: bool
    can_mark_as_sold: bool
    can_transfer: bool
    instant_buy: bool
    can_close: bool
    can_buy: bool
    can_bundle: bool
    can_ask_seller: bool
    can_favourite: bool
    user_login: str
    city_id: int
    city: str
    country: str
    promoted: bool
    is_mobile: bool
    bump_badge_visible: bool
    brand_dto: BrandDto
    path: str
    url: str
    accepted_pay_in_methods: list[AcceptedPayInMethod1]
    created_at: str
    color1: str
    color2: str
    description_attributes: list
    video_game_rating: str | None
    status: str
    is_favourite: bool
    performance: str | None
    stats_visible: bool
    can_push_up: bool
    can_vas_gallery_promote: bool
    vas_gallery_promoted: bool
    badge: str | None
    size_guide_faq_entry_id: int
    localization: str
    is_upload_story_button_visible: bool
    offline_verification: bool
    offline_verification_fee: str | None
    icon_badges: list
