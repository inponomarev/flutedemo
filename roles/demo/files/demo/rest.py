from ru.curs.flute.rest.decorator import Mapping
from org.springframework.web.reactive.function.server import ServerResponse
from reactor.core.publisher import Mono
import basic_operations

@Mapping('/postorder', 'POST')
def postorder(context, flute, request):
    doc = request.bodyToMono(dict).block()
    basic_operations.post_order(context, doc)
    return ServerResponse.ok().body(Mono.just('OK'), str)

@Mapping('/foo', 'GET')
def foo(context, flute, request):
    report = basic_operations.get_aggregate_report(context)
    return ServerResponse.ok().body(Mono.just(report), report.__class__)