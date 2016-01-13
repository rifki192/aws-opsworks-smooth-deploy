# -*- coding: utf-8 -*-

"""AWS Opsworks Smooth Deploy
`Python Styling Guide <https://www.python.org/dev/peps/pep-0008/>`
`Docstring Guide <https://docs.python.org/devguide/documenting.html>`

This module provides functionalities to attach f

.. module:: opsworkssmoothdeploy
   :platform: Unix
.. moduleauthor:: Petra Barus <petra@urbanindo.com>
.. moduleauthor:: Rifki <rifki@urbanindo.com>
"""

import boto3
import json

__MINIMUM_ATTACHED_INSTANCES__ = 1

def get_current_instance_id():
    """Get instance ID from HTTP request and returns it.
    """
    return 'instanceid'

def get_instance_stack(instance_id):
    """Get the instance stack of the instance id and returns it.
    :param instance_id The ID of the instance.
    """
    return 'stack_id'

def get_elastic_load_balancer_id_from_stack(stack_id):
    """Get elastic load balancer that attached to a stack.
    :param stack_id The ID of the stack.
    """
    return;

def get_elastic_load_balancer_id_from_instance(instance_id):
    """Get elastic load balancer with which an instance being attached.
    :param instance_id The ID of the stack.
    """
    return 'elb'

def get_elastic_load_balancer_instance_count(elb):
    """Get elastic load balancer from HTTP request and returns it.
    :param elb The name of the elastic load balancer.
    """
    return 0

def attach_instance_to_elastic_load_balancer(instance_id, elb):
    """Attach an instance to load balancer.
    :param instance_id The ID of the instance to attach.
    :param elb         The name of the elastic load balancer.
    """
    pass

def detach_instance_from_elastic_load_balancer(instance_id, elb):
    """Detach an instance to load balancer.
    :param instance_id The ID of the instance to detach.
    :param elb         The name of the elastic load balancer.
    """
    pass

def detach(opsworks_stack_id):
    """Detach current instance from the load balancer if the active instance
    is still in threshold.
    :param opsworks_stack_id The ID of the opsworks stack.
    """
    pass

def attach():
    """Attach current instance to load balancer.
    :param opsworks_stack_id The ID of the opsworks stack.
    """
    pass
