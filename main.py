"""Main module which executes all code for this project"""

from abstract_factory.main import main as abstract_factory_main
from adapter.main import main as adapter_main
from bridge.main import main as bridge_main
from Builder.main import main as builder_main
from chain_of_responsibility.main import main as chain_of_responsibility_main
from command.main import main as command_main
from composite.main import main as composite_main
from decorator_logging.main import main as decorator_main
from delegation.main import main as delegation_main
from dependency_injection.main import main as dependency_main
from facade.main import main as facade_main
from factory.main import main as factory_main
from flyweight.main import main as flyweight_main
from front_controller.main import main as controller_main
from Lazy.main import main as lazy_main
from mediator.main import main as mediator_main
from momento.main import main as momento_main
from Object_pool.main import main as pool_main
from observer.main import main as observer_main
from proxy.main import main as proxy_main

from servant.main import main as servant_main
from singleton.main import main as singleton_main
from state.main import main as state_main
from strategy.main import main as strategy_main
from template.main import main as template_main
from visitor.main import main as visitor_main


def main():
    """Main method which is executes all the design pattern examples"""
    # test all once documented
    abstract_factory_main()
    adapter_main()
    bridge_main()
    builder_main()
    chain_of_responsibility_main()
    command_main()
    composite_main()
    decorator_main()
    delegation_main()
    dependency_main()
    facade_main()
    factory_main()
    flyweight_main()
    controller_main()
    lazy_main()
    mediator_main()
    momento_main()
    pool_main()
    observer_main()
    proxy_main()
    servant_main()
    singleton_main()
    state_main()
    strategy_main()
    template_main()
    visitor_main()


if __name__ == "__main__":
    main()
