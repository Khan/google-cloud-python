# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/vision_v1p3beta1/proto/product_search.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.cloud.vision_v1p3beta1.proto import (
    geometry_pb2 as google_dot_cloud_dot_vision__v1p3beta1_dot_proto_dot_geometry__pb2,
)
from google.cloud.vision_v1p3beta1.proto import (
    product_search_service_pb2 as google_dot_cloud_dot_vision__v1p3beta1_dot_proto_dot_product__search__service__pb2,
)
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/vision_v1p3beta1/proto/product_search.proto",
    package="google.cloud.vision.v1p3beta1",
    syntax="proto3",
    serialized_options=_b(
        "\n!com.google.cloud.vision.v1p3beta1B\022ProductSearchProtoP\001ZCgoogle.golang.org/genproto/googleapis/cloud/vision/v1p3beta1;vision\370\001\001"
    ),
    serialized_pb=_b(
        '\n8google/cloud/vision_v1p3beta1/proto/product_search.proto\x12\x1dgoogle.cloud.vision.v1p3beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x32google/cloud/vision_v1p3beta1/proto/geometry.proto\x1a@google/cloud/vision_v1p3beta1/proto/product_search_service.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb2\x03\n\x13ProductSearchParams\x12\x14\n\x0c\x63\x61talog_name\x18\x01 \x01(\t\x12\x46\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32\x34.google.cloud.vision.v1p3beta1.ProductSearchCategory\x12\x18\n\x10product_category\x18\x05 \x01(\t\x12W\n\x18normalized_bounding_poly\x18\x03 \x01(\x0b\x32\x35.google.cloud.vision.v1p3beta1.NormalizedBoundingPoly\x12\x42\n\rbounding_poly\x18\t \x01(\x0b\x32+.google.cloud.vision.v1p3beta1.BoundingPoly\x12\x45\n\x04view\x18\x04 \x01(\x0e\x32\x37.google.cloud.vision.v1p3beta1.ProductSearchResultsView\x12\x13\n\x0bproduct_set\x18\x06 \x01(\t\x12\x1a\n\x12product_categories\x18\x07 \x03(\t\x12\x0e\n\x06\x66ilter\x18\x08 \x01(\t"\xee\x03\n\x14ProductSearchResults\x12\x46\n\x08\x63\x61tegory\x18\x01 \x01(\x0e\x32\x34.google.cloud.vision.v1p3beta1.ProductSearchCategory\x12\x18\n\x10product_category\x18\x04 \x01(\t\x12.\n\nindex_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12Q\n\x08products\x18\x03 \x03(\x0b\x32?.google.cloud.vision.v1p3beta1.ProductSearchResults.ProductInfo\x12K\n\x07results\x18\x05 \x03(\x0b\x32:.google.cloud.vision.v1p3beta1.ProductSearchResults.Result\x1a\x43\n\x0bProductInfo\x12\x12\n\nproduct_id\x18\x01 \x01(\t\x12\x11\n\timage_uri\x18\x02 \x01(\t\x12\r\n\x05score\x18\x03 \x01(\x02\x1a_\n\x06Result\x12\x37\n\x07product\x18\x01 \x01(\x0b\x32&.google.cloud.vision.v1p3beta1.Product\x12\r\n\x05score\x18\x02 \x01(\x02\x12\r\n\x05image\x18\x03 \x01(\t*U\n\x15ProductSearchCategory\x12\'\n#PRODUCT_SEARCH_CATEGORY_UNSPECIFIED\x10\x00\x12\t\n\x05SHOES\x10\x01\x12\x08\n\x04\x42\x41GS\x10\x02*/\n\x18ProductSearchResultsView\x12\t\n\x05\x42\x41SIC\x10\x00\x12\x08\n\x04\x46ULL\x10\x01\x42\x81\x01\n!com.google.cloud.vision.v1p3beta1B\x12ProductSearchProtoP\x01ZCgoogle.golang.org/genproto/googleapis/cloud/vision/v1p3beta1;vision\xf8\x01\x01\x62\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_cloud_dot_vision__v1p3beta1_dot_proto_dot_geometry__pb2.DESCRIPTOR,
        google_dot_cloud_dot_vision__v1p3beta1_dot_proto_dot_product__search__service__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
    ],
)

_PRODUCTSEARCHCATEGORY = _descriptor.EnumDescriptor(
    name="ProductSearchCategory",
    full_name="google.cloud.vision.v1p3beta1.ProductSearchCategory",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="PRODUCT_SEARCH_CATEGORY_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="SHOES", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="BAGS", index=2, number=2, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1206,
    serialized_end=1291,
)
_sym_db.RegisterEnumDescriptor(_PRODUCTSEARCHCATEGORY)

ProductSearchCategory = enum_type_wrapper.EnumTypeWrapper(_PRODUCTSEARCHCATEGORY)
_PRODUCTSEARCHRESULTSVIEW = _descriptor.EnumDescriptor(
    name="ProductSearchResultsView",
    full_name="google.cloud.vision.v1p3beta1.ProductSearchResultsView",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="BASIC", index=0, number=0, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="FULL", index=1, number=1, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1293,
    serialized_end=1340,
)
_sym_db.RegisterEnumDescriptor(_PRODUCTSEARCHRESULTSVIEW)

ProductSearchResultsView = enum_type_wrapper.EnumTypeWrapper(_PRODUCTSEARCHRESULTSVIEW)
PRODUCT_SEARCH_CATEGORY_UNSPECIFIED = 0
SHOES = 1
BAGS = 2
BASIC = 0
FULL = 1


_PRODUCTSEARCHPARAMS = _descriptor.Descriptor(
    name="ProductSearchParams",
    full_name="google.cloud.vision.v1p3beta1.ProductSearchParams",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="catalog_name",
            full_name="google.cloud.vision.v1p3beta1.ProductSearchParams.catalog_name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="category",
            full_name="google.cloud.vision.v1p3beta1.ProductSearchParams.category",
            index=1,
            number=2,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="product_category",
            full_name="google.cloud.vision.v1p3beta1.ProductSearchParams.product_category",
            index=2,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="normalized_bounding_poly",
            full_name="google.cloud.vision.v1p3beta1.ProductSearchParams.normalized_bounding_poly",
            index=3,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="bounding_poly",
            full_name="google.cloud.vision.v1p3beta1.ProductSearchParams.bounding_poly",
            index=4,
            number=9,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="view",
            full_name="google.cloud.vision.v1p3beta1.ProductSearchParams.view",
            index=5,
            number=4,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="product_set",
            full_name="google.cloud.vision.v1p3beta1.ProductSearchParams.product_set",
            index=6,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="product_categories",
            full_name="google.cloud.vision.v1p3beta1.ProductSearchParams.product_categories",
            index=7,
            number=7,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="filter",
            full_name="google.cloud.vision.v1p3beta1.ProductSearchParams.filter",
            index=8,
            number=8,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=273,
    serialized_end=707,
)


_PRODUCTSEARCHRESULTS_PRODUCTINFO = _descriptor.Descriptor(
    name="ProductInfo",
    full_name="google.cloud.vision.v1p3beta1.ProductSearchResults.ProductInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="product_id",
            full_name="google.cloud.vision.v1p3beta1.ProductSearchResults.ProductInfo.product_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="image_uri",
            full_name="google.cloud.vision.v1p3beta1.ProductSearchResults.ProductInfo.image_uri",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="score",
            full_name="google.cloud.vision.v1p3beta1.ProductSearchResults.ProductInfo.score",
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1040,
    serialized_end=1107,
)

_PRODUCTSEARCHRESULTS_RESULT = _descriptor.Descriptor(
    name="Result",
    full_name="google.cloud.vision.v1p3beta1.ProductSearchResults.Result",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="product",
            full_name="google.cloud.vision.v1p3beta1.ProductSearchResults.Result.product",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="score",
            full_name="google.cloud.vision.v1p3beta1.ProductSearchResults.Result.score",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="image",
            full_name="google.cloud.vision.v1p3beta1.ProductSearchResults.Result.image",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1109,
    serialized_end=1204,
)

_PRODUCTSEARCHRESULTS = _descriptor.Descriptor(
    name="ProductSearchResults",
    full_name="google.cloud.vision.v1p3beta1.ProductSearchResults",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="category",
            full_name="google.cloud.vision.v1p3beta1.ProductSearchResults.category",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="product_category",
            full_name="google.cloud.vision.v1p3beta1.ProductSearchResults.product_category",
            index=1,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="index_time",
            full_name="google.cloud.vision.v1p3beta1.ProductSearchResults.index_time",
            index=2,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="products",
            full_name="google.cloud.vision.v1p3beta1.ProductSearchResults.products",
            index=3,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="results",
            full_name="google.cloud.vision.v1p3beta1.ProductSearchResults.results",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_PRODUCTSEARCHRESULTS_PRODUCTINFO, _PRODUCTSEARCHRESULTS_RESULT],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=710,
    serialized_end=1204,
)

_PRODUCTSEARCHPARAMS.fields_by_name["category"].enum_type = _PRODUCTSEARCHCATEGORY
_PRODUCTSEARCHPARAMS.fields_by_name[
    "normalized_bounding_poly"
].message_type = (
    google_dot_cloud_dot_vision__v1p3beta1_dot_proto_dot_geometry__pb2._NORMALIZEDBOUNDINGPOLY
)
_PRODUCTSEARCHPARAMS.fields_by_name[
    "bounding_poly"
].message_type = (
    google_dot_cloud_dot_vision__v1p3beta1_dot_proto_dot_geometry__pb2._BOUNDINGPOLY
)
_PRODUCTSEARCHPARAMS.fields_by_name["view"].enum_type = _PRODUCTSEARCHRESULTSVIEW
_PRODUCTSEARCHRESULTS_PRODUCTINFO.containing_type = _PRODUCTSEARCHRESULTS
_PRODUCTSEARCHRESULTS_RESULT.fields_by_name[
    "product"
].message_type = (
    google_dot_cloud_dot_vision__v1p3beta1_dot_proto_dot_product__search__service__pb2._PRODUCT
)
_PRODUCTSEARCHRESULTS_RESULT.containing_type = _PRODUCTSEARCHRESULTS
_PRODUCTSEARCHRESULTS.fields_by_name["category"].enum_type = _PRODUCTSEARCHCATEGORY
_PRODUCTSEARCHRESULTS.fields_by_name[
    "index_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PRODUCTSEARCHRESULTS.fields_by_name[
    "products"
].message_type = _PRODUCTSEARCHRESULTS_PRODUCTINFO
_PRODUCTSEARCHRESULTS.fields_by_name[
    "results"
].message_type = _PRODUCTSEARCHRESULTS_RESULT
DESCRIPTOR.message_types_by_name["ProductSearchParams"] = _PRODUCTSEARCHPARAMS
DESCRIPTOR.message_types_by_name["ProductSearchResults"] = _PRODUCTSEARCHRESULTS
DESCRIPTOR.enum_types_by_name["ProductSearchCategory"] = _PRODUCTSEARCHCATEGORY
DESCRIPTOR.enum_types_by_name["ProductSearchResultsView"] = _PRODUCTSEARCHRESULTSVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProductSearchParams = _reflection.GeneratedProtocolMessageType(
    "ProductSearchParams",
    (_message.Message,),
    dict(
        DESCRIPTOR=_PRODUCTSEARCHPARAMS,
        __module__="google.cloud.vision_v1p3beta1.proto.product_search_pb2",
        __doc__="""Parameters for a product search request.
  
  
  Attributes:
      catalog_name:
          The resource name of the catalog to search.  Format is:
          ``productSearch/catalogs/CATALOG_NAME``.
      category:
          The category to search in. Optional. It is inferred by the
          system if it is not specified. [Deprecated] Use
          ``product_category``.
      product_category:
          The product category to search in. Optional. It is inferred by
          the system if it is not specified. Supported values are
          ``bag``, ``shoe``, ``sunglasses``, ``dress``, ``outerwear``,
          ``skirt``, ``top``, ``shorts``, and ``pants``.
      normalized_bounding_poly:
          The bounding polygon around the area of interest in the image.
          Optional. If it is not specified, system discretion will be
          applied. [Deprecated] Use ``bounding_poly``.
      bounding_poly:
          The bounding polygon around the area of interest in the image.
          Optional. If it is not specified, system discretion will be
          applied.
      view:
          Specifies the verbosity of the product search results.
          Optional. Defaults to ``BASIC``.
      product_set:
          The resource name of a
          [ProductSet][google.cloud.vision.v1p3beta1.ProductSet] to be
          searched for similar images.  Format is: ``projects/PROJECT_ID
          /locations/LOC_ID/productSets/PRODUCT_SET_ID``.
      product_categories:
          The list of product categories to search in. Currently, we
          only consider the first category, and either "homegoods" or
          "apparel" should be specified.
      filter:
          The filtering expression. This can be used to restrict search
          results based on Product labels. We currently support an AND
          of OR of key-value expressions, where each expression within
          an OR must have the same key.  For example, "(color = red OR
          color = blue) AND brand = Google" is acceptable, but not
          "(color = red OR brand = Google)" or "color: red".
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.vision.v1p3beta1.ProductSearchParams)
    ),
)
_sym_db.RegisterMessage(ProductSearchParams)

ProductSearchResults = _reflection.GeneratedProtocolMessageType(
    "ProductSearchResults",
    (_message.Message,),
    dict(
        ProductInfo=_reflection.GeneratedProtocolMessageType(
            "ProductInfo",
            (_message.Message,),
            dict(
                DESCRIPTOR=_PRODUCTSEARCHRESULTS_PRODUCTINFO,
                __module__="google.cloud.vision_v1p3beta1.proto.product_search_pb2",
                __doc__="""Information about a product.
    
    
    Attributes:
        product_id:
            Product ID.
        image_uri:
            The URI of the image which matched the query image.  This
            field is returned only if ``view`` is set to ``FULL`` in the
            request.
        score:
            A confidence level on the match, ranging from 0 (no
            confidence) to 1 (full confidence).  This field is returned
            only if ``view`` is set to ``FULL`` in the request.
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.vision.v1p3beta1.ProductSearchResults.ProductInfo)
            ),
        ),
        Result=_reflection.GeneratedProtocolMessageType(
            "Result",
            (_message.Message,),
            dict(
                DESCRIPTOR=_PRODUCTSEARCHRESULTS_RESULT,
                __module__="google.cloud.vision_v1p3beta1.proto.product_search_pb2",
                __doc__="""Information about a product.
    
    
    Attributes:
        product:
            The Product.
        score:
            A confidence level on the match, ranging from 0 (no
            confidence) to 1 (full confidence).  This field is returned
            only if ``view`` is set to ``FULL`` in the request.
        image:
            The resource name of the image from the product that is the
            closest match to the query.
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.vision.v1p3beta1.ProductSearchResults.Result)
            ),
        ),
        DESCRIPTOR=_PRODUCTSEARCHRESULTS,
        __module__="google.cloud.vision_v1p3beta1.proto.product_search_pb2",
        __doc__="""Results for a product search request.
  
  
  Attributes:
      category:
          Product category. [Deprecated] Use ``product_category``.
      product_category:
          Product category. Supported values are ``bag`` and ``shoe``.
          [Deprecated] ``product_category`` is provided in each Product.
      index_time:
          Timestamp of the index which provided these results. Changes
          made after this time are not reflected in the current results.
      products:
          List of detected products.
      results:
          List of results, one for each product match.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.vision.v1p3beta1.ProductSearchResults)
    ),
)
_sym_db.RegisterMessage(ProductSearchResults)
_sym_db.RegisterMessage(ProductSearchResults.ProductInfo)
_sym_db.RegisterMessage(ProductSearchResults.Result)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
