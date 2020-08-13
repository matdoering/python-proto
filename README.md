# python-proto
This repo offers boilerplate code for using Protobuf in a Python project. A requirement is that `protoc` is available.

For more information, see the [corresponding blog post](https://www.datascienceblog.net/post/programming/essential-protobuf-guide-python/).

## How to use?

- To compile the proto files, execute

```
pip install -e ./
```

This will generate the `*_pb2.py` files under `src/generated`.

- To generate Protobuf messages, execute

```
python src/main.py
```

The corresponding files will be generated in the `proto_dump` folder.
