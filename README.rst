.. image:: https://github.com/ray-project/ray/raw/master/doc/source/images/ray_header_logo.png

.. image:: https://travis-ci.com/ray-project/ray.svg?branch=master
    :target: https://travis-ci.com/ray-project/ray

.. image:: https://readthedocs.org/projects/ray/badge/?version=latest
    :target: http://ray.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/badge/pypi-0.6.5-blue.svg
    :target: https://pypi.org/project/ray/

.. image:: https://img.shields.io/badge/powered%20by-ray-07A1E1.svg?style=popout&logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMTExNS4wMDAwMDBwdCIgaGVpZ2h0PSIxMDQyLjAwMDAwMHB0IiB2aWV3Qm94PSIwIDAgMTExNS4wMDAwMDAgMTA0Mi4wMDAwMDAiCiBwcmVzZXJ2ZUFzcGVjdFJhdGlvPSJ4TWlkWU1pZCBtZWV0Ij4KCjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAuMDAwMDAwLDEwNDIuMDAwMDAwKSBzY2FsZSgwLjEwMDAwMCwtMC4xMDAwMDApIgpmaWxsPSIjMDAwMDAwIiBzdHJva2U9Im5vbmUiPgo8cGF0aCBzdHlsZT0iZmlsbDojMDdBMUUxOyIgZD0iTTU1MzAgOTkwMyBjLTU3IC03IC0yMTIgLTQyIC0yNTUgLTU3IC0yMiAtOSAtNDggLTE1IC01NyAtMTYgLTEwIDAKLTE4IC00IC0xOCAtMTAgMCAtNSAtNCAtMTAgLTkgLTEwIC0yMCAwIC0yMTkgLTEwMSAtMjMwIC0xMTcgLTMgLTUgLTE4IC0xNgotMzMgLTI2IC03NyAtNDkgLTI0NSAtMjI3IC0zMDkgLTMyNyAtNTQgLTg1IC01OCAtOTMgLTc1IC0xMzAgLTkgLTE5IC0yNCAtNTMKLTM0IC03NSAtMjIgLTQ2IC01MCAtMTM4IC03NSAtMjQ1IC0xOSAtODMgLTI2IC0zMzEgLTEyIC00MzUgMTIgLTgzIDgyIC0zMDUKMTIxIC0zNzkgMTcgLTMzIDU2IC05NiA4NiAtMTQwIDMwIC00MyA2MCAtODUgNjUgLTkzIDMwIC00NCAxODUgLTE4NiAyNjIKLTIzOSAxMjYgLTg4IDE4NyAtMTE5IDMyNSAtMTYzIDIxOSAtNzAgNDgzIC04NiA2NTggLTQxIDE5IDUgNjQgMTYgMTAwIDI1IDY0CjE2IDEyMSA0MCAyMzMgOTYgbDU4IDMwIDgyNiAtODI3IDgyNiAtODI2IC0xNyAtMzEgYy05IC0xOCAtMjMgLTQzIC0zMSAtNTcKLTIzIC00MCAtNTUgLTExNSAtNTUgLTEyOCAwIC02IC05IC0zNiAtMjEgLTY3IGwtMjAgLTU1IC00NjMgMCAtNDYyIDAgLTE4IDUzCmMtMzggMTA5IC03OCAyMTEgLTkzIDIzNiAtMTA2IDE3MiAtMjM0IDMyMSAtMzQ4IDQwMyAtNSA0IC0yMyAxOCAtNDAgMzEgLTczCjU1IC0xNjAgMTA3IC0xODAgMTA3IC03IDAgLTE1IDQgLTE3IDggLTMgOSAtMTI0IDU1IC0yMDMgNzggLTExMSAzMSAtMjU2IDQ2Ci0zODkgNDAgLTExOCAtNiAtMTgxIC0xNyAtMzM4IC01OSAtNjcgLTE4IC0yNDcgLTEwNyAtMzM3IC0xNjcgLTEyMiAtODEgLTI4MgotMjUyIC0zNTEgLTM3NSAtNjggLTEyMSAtMTA5IC0yMDggLTEyNCAtMjY1IC0xMCAtMzYgLTIwIC03MSAtMjIgLTc4IC0zIC0xMAotMTAyIC0xMiAtNDcxIC0xMCBsLTQ2NyAzIC04IDM5IGMtMTggODcgLTE0MiAzMzYgLTE5OSA0MDEgLTEyOCAxNDUgLTE2NSAxODMKLTI0OSAyNTMgLTkwIDc1IC0zMTUgMTg5IC00MjAgMjEzIC0xNzAgMzggLTE5MyA0MSAtMzU1IDQyIC0xMDMgMSAtMTg5IC00Ci0yMTcgLTExIC0yNyAtNyAtNjkgLTE3IC05NSAtMjMgLTkyIC0yMSAtMTMzIC0zMyAtMTMzIC00MSAwIC00IC01IC04IC0xMCAtOAotNiAwIC00NSAtMTYgLTg2IC0zNSAtNDEgLTE5IC03NyAtMzUgLTgwIC0zNSAtOSAwIC0xMTYgLTcxIC0xNTQgLTEwMyAtNjUKLTUzIC0yMzAgLTIyMCAtMjMwIC0yMzMgMCAtNiAtNyAtMTcgLTE1IC0yNCAtMjggLTIzIC04NSAtMTE4IC0xMjAgLTIwMSAtMjAKLTQ2IC00MiAtOTcgLTUwIC0xMTQgLTE3IC0zNCAtMzkgLTEyMyAtNjEgLTI0NSAtMzMgLTE4NiAtMyAtNDg0IDY1IC02MzIgMTEKLTI2IDIxIC01MCAyMSAtNTMgMCAtOSA2NyAtMTQzIDkzIC0xODUgMzQgLTU2IDEwMSAtMTQxIDE1OCAtMjAwIDkxIC05NCAxMjYKLTEyMiAyNDQgLTE5OCAyMiAtMTQgMTc5IC05MSAyMzUgLTExNSAxOSAtOCA4NSAtMjcgMTQ1IC00MiA5OSAtMjUgMTI4IC0yOAoyODUgLTI4IDEzMCAwIDE5NCA1IDI1MCAxOCA0MSA5IDkzIDIxIDExNiAyNSAyMyA1IDYxIDE4IDg1IDI5IDEzNCA2MiAyMDUgOTYKMjE0IDEwMyA1IDQgMzkgMjcgNzMgNDkgMTAxIDY2IDI1NSAyMjUgMzM4IDM1MCA0MCA1OSAxMzEgMjYxIDE0NyAzMjQgbDEyIDUwCjQ2OCAzIDQ2NyAyIDEwIC0yNiBjNiAtMTQgNyAtMzAgNCAtMzUgLTMgLTYgMSAtMjEgMTAgLTM0IDkgLTEzIDE2IC0zMSAxNgotMzggMCAtMTIgNDIgLTk2IDEwOSAtMjIyIDQ1IC04NCAxOTIgLTI1MCAyOTYgLTMzMyA0NCAtMzYgMTM1IC05NCAxODAgLTExNQoyMiAtMTAgNDIgLTIxIDQ1IC0yNSAzIC00IDM1IC0yMCA3MSAtMzUgNjAgLTI2IDkzIC0zNiAyMjQgLTY4IDU2IC0xNCAxOTUKLTI3IDI5MCAtMjggMTQxIC0yIDM1MCA0NiA0OTUgMTEyIDI1IDExIDUyIDIzIDYwIDI3IDQ2IDIxIDEzMyA3MyAxNTMgOTMgMTMKMTIgNTIgNDQgODYgNzIgNzAgNTYgMTEyIDEwMCAxODAgMTg2IDgzIDEwNiAxMDcgMTQzIDE0MCAyMTkgMTkgNDEgMzkgODYgNDUKMTAwIDYgMTQgMjAgNTMgMzEgODggbDIwIDYyIDQ2MSAwIDQ2MiAwIDI3IC03NyBjNDEgLTExOCA3MyAtMTkzIDk1IC0yMjEgMTEKLTEzIDIwIC0zMCAyMCAtMzYgMCAtNiAtMzcxIC0zODEgLTgyNCAtODM0IGwtODI0IC04MjMgLTUzIDI2IGMtMzAgMTUgLTcxIDM1Ci05MiA0NiAtMjIgMTAgLTQzIDE5IC00OCAxOSAtNiAwIC0yOSA5IC01MiAxOSAtMjMgMTEgLTYwIDIyIC04MiAyNiAtMjIgNAotNTMgMTEgLTcwIDE2IC0xNiA1IC05MyAxMyAtMTcwIDE5IC0xMTMgOCAtMTYwIDcgLTI1MCAtNiAtMTMyIC0xOSAtMjU4IC01NAotMzU1IC05OCAtNjcgLTMxIC0yMTcgLTEyMiAtMjUwIC0xNTMgLTE0IC0xMyAtMjggLTIzIC0zMiAtMjMgLTEzIDAgLTE3NwotMTY5IC0yMDIgLTIwOCAtMTMgLTIwIC0zMSAtNDMgLTQwIC01MSAtOSAtNyAtMTYgLTE4IC0xNiAtMjMgMCAtNiAtOCAtMjIKLTE5IC0zNiAtODIgLTExNiAtMTQ2IC0zMDAgLTE4MiAtNTE5IC0xNSAtOTAgLTUgLTMxNiAxNyAtMzk5IDkgLTMyIDE4IC02OQoxOSAtODEgNiAtNDMgNDcgLTE0NCAxMDYgLTI1OSAzMyAtNjUgNjQgLTEyMSA2OCAtMTI0IDMgLTMgMTQgLTE3IDI0IC0zMiA3MwotMTE2IDI4OSAtMzA0IDQxMCAtMzU5IDI2IC0xMiA0NyAtMjUgNDcgLTMwIDAgLTUgMyAtOCA4IC03IDggMyA3NSAtMjMgODIKLTMyIDYgLTcgODYgLTMxIDIwNSAtNjIgNjUgLTE2IDExNCAtMjEgMjYwIC0yMiA5OSAwIDIwOSA0IDI0NSAxMCAxMTMgMjAgMzg3CjEyMiA0MTAgMTUyIDMgNCAzNyAyOSA3NyA1NSA0MCAyNyA5MSA2NSAxMTQgODUgNDkgNDIgMTQ4IDE0MiAxNDIgMTQyIC0yIDAKMTEgMTkgMzAgNDIgNjAgNzYgMTE3IDE2MyAxMTcgMTgxIDAgOSA0IDE3IDggMTcgMTcgMCAxMDcgMjQ5IDExNiAzMTggMiAyMSA5CjY2IDE2IDEwMCAxMyA3MiA2IDMyMiAtMTEgMzg0IC02IDIzIC0xNSA2MiAtMTkgODcgLTEyIDYzIC03NyAyMzggLTEwNSAyODEKLTUgOCAtMTUgMjUgLTIxIDM3IC0xMSAyMCA0NSA3OSA4MTIgODQ1IDQ1MyA0NTMgODI2IDgyNSA4MjkgODI3IDIgMiAxNyAtNgozMiAtMTcgNDYgLTMyIDEzMSAtNjkgMjMzIC0xMDAgMTM3IC00MiAxOTkgLTUzIDM0MCAtNTkgMTAzIC01IDE0NyAtMiAyNDkgMTYKNjggMTMgMTQ3IDMxIDE3NSA0MSAyOCAxMCA2NiAyMSA4NCAyNSAxNyA0IDMyIDEwIDMyIDE1IDAgNSAxMyAxMSAzMCAxNSAxNiA0CjQ1IDE3IDY1IDMxIDIwIDEzIDQ4IDMwIDY0IDM5IDQ1IDIzIDE5MSAxMzcgMjQ1IDE5MSA0OSA0OSAxNjMgMTk3IDE5OCAyNTcKNTIgOTAgMTI1IDI3NyAxNDMgMzY3IDI2IDEzNiAyNyA0MDIgMiA1MjUgLTQ5IDI0MiAtMTY3IDQ1OSAtMzQ4IDY0MyAtNzMgNzQKLTg1IDg0IC0yMTAgMTY3IC0xMDkgNzMgLTEzOSA4OCAtMjc5IDEzNSAtMjA3IDY5IC0zOTQgODcgLTU4NSA1NCAtNDkgLTgKLTEwNiAtMTggLTEyNSAtMjEgLTE5IC0zIC0zOSAtOSAtNDUgLTEzIC04IC02IC00MyAtMTYgLTg1IC0yNSAtMjQgLTUgLTgwCi0zMSAtODAgLTM3IDAgLTQgLTggLTggLTE4IC04IC0xMCAwIC0zOSAtMTMgLTY1IC0zMCAtMjYgLTE2IC00OSAtMzAgLTUxIC0zMAotNyAwIC0xNjQxIDE2NDAgLTE2NDQgMTY1MCAtMyA3IDE2IDUzIDQxIDEwMyA4NiAxNzUgMTIwIDMyNSAxMjEgNTM1IDEgMTQ4Ci0xMyAyNzMgLTM4IDM0NyAtOCAyMiAtMjQgNzIgLTM2IDExMCAtMjUgNzcgLTYxIDE0OSAtMTA5IDIyMCAtMTcgMjUgLTMxIDUwCi0zMSA1NCAwIDUgLTcgMTUgLTE2IDIyIC05IDggLTI3IDMwIC0zOSA0OSAtNTAgNzcgLTIwOCAyMTkgLTMxOSAyODYgLTk2IDU4Ci0xODEgMTAzIC0xOTQgMTA0IC04IDAgLTI4IDYgLTQ1IDEzIC01OCAyNCAtMTQwIDQ5IC0xOTcgNTkgLTU5IDEwIC0zMzIgMTgKLTM5MCAxMXogbTMxMiAtNjMyIGM4MSAtMTggMjI4IC0xMDMgMjk1IC0xNzAgMTI4IC0xMjcgMjA1IC0zMzcgMTg5IC01MTMgLTYKLTY2IC00MyAtMTkzIC03MyAtMjUzIC00NSAtODkgLTE3MiAtMjE0IC0yNjIgLTI2MCAtMTk1IC05OCAtNDA4IC0xMDQgLTU4MwotMTQgLTEzMCA2NiAtMTkwIDExNiAtMjU3IDIxNCAtMzcgNTUgLTk4IDE4MSAtOTkgMjA1IDAgOCAtNSA1MSAtMTIgOTUgLTE4CjEyMyA4IDI1NCA3NiAzODUgNjQgMTIzIDIxNSAyNTIgMzM0IDI4NyAzMCA4IDYwIDE5IDY1IDIzIDI1IDIwIDI0MSAyMSAzMjcgMXoKbS0zNDAwIC0zMzk0IGM3NSAtMTcgMTY0IC01NSAyMDkgLTg5IDUwIC0zOSAxNDkgLTEzNSAxNDkgLTE0NSAwIC02IDkgLTE4IDE5Ci0yNyAyMiAtMjAgNzggLTEzMCA4NCAtMTY2IDMgLTE0IDEwIC00NSAxNyAtNzAgMTcgLTYxIDEzIC0yMDcgLTcgLTI4OSAtMTgKLTczIC02NCAtMTc1IC05NCAtMjA3IC0xMCAtMTEgLTE5IC0yNSAtMTkgLTMwIDAgLTE1IC0xMDEgLTEwOCAtMTYwIC0xNDcKLTEwMyAtNjcgLTI3MSAtMTEzIC0zODQgLTEwNCAtODAgNiAtMTY4IDI3IC0yMTQgNTEgLTE3IDkgLTM2IDE2IC00MiAxNiAtMjIKMCAtMTE5IDY5IC0xNzAgMTIyIC04NiA4NyAtMTUyIDIxMSAtMTgwIDMzOCAtMzAgMTQwIDEyIDM1NiA5NCA0NzUgNjMgOTIgMjE2CjIyNSAyNTggMjI1IDggMCAxOSA1IDI1IDExIDYgNiA0OSAyMCA5NSAzMiA5OSAyNiAyMTUgMjcgMzIwIDR6IG0zMzY4IDcgYzExNQotMjQgMTk4IC02NiAyODAgLTE0MSAxOSAtMTggMzggLTMzIDQyIC0zMyAxMSAwIDk4IC0xMTggMTI4IC0xNzQgNDMgLTgwIDY0Ci0xNzYgNjQgLTI5MSAtMSAtMTcxIC01MiAtMzA1IC0xNjYgLTQzMSAtNTMgLTU4IC0xODIgLTE1MCAtMjI4IC0xNjEgLTE0IC0zCi0zMCAtOSAtMzUgLTE0IC02IC00IC00NCAtMTUgLTg1IC0yMyAtODUgLTE4IC0yMTEgLTEzIC0zMDAgMTEgLTczIDIwIC0xOTcKODAgLTIwNCA5OCAtMyA4IC0xMSAxNSAtMTkgMTUgLTMyIDAgLTE3MyAxNzYgLTE5MiAyNDAgLTQgMTQgLTEzIDM0IC0yMCA0NQotMTYgMjUgLTQyIDE1MyAtNDQgMjE3IC0xIDI2IDMgNzYgOSAxMTAgMTMgNzIgNjUgMjEyIDg2IDIyOSA4IDYgMTQgMTggMTQgMjUKMCAyMSAxMjUgMTQ5IDE3OCAxODMgMjYgMTYgNTkgMzMgNzUgMzYgMTUgNCAyNyAxMCAyNyAxNCAwIDEzIDEyMSA0NCAxOTUgNTEKMTEzIDExIDExNyAxMSAxOTUgLTZ6IG0zMzU3IDUgYzcwIC0xMCAxNTIgLTM1IDE5MyAtNjAgOCAtNSAzNiAtMjAgNjIgLTM0IDI1Ci0xMyA1NSAtMzYgNjYgLTUwIDExIC0xNCAyNCAtMjUgMzAgLTI1IDkgMCA2NSAtNjkgOTcgLTExOSA4MSAtMTI2IDk5IC0xODkKOTggLTM1MSAwIC0xMTEgLTQgLTE0NiAtMjIgLTE5OSAtMzEgLTk1IC0xMjkgLTI0MCAtMTkxIC0yODYgLTExMCAtODEgLTE0MgotMTAwIC0yMDIgLTEyMyAtMTIyIC00NiAtMzEwIC00OCAtNDI4IC02IC03NyAyNyAtMjYwIDE0MiAtMjYwIDE2MyAwIDMgLTE3CjI1IC0zOCA0OCAtMjEgMjMgLTU3IDgwIC04MCAxMjYgLTUxIDEwMyAtNzggMjQ2IC02MyAzMzAgNSAyOSA3IDU1IDUgNTkgLTcKMTAgNTIgMTYxIDg3IDIyMyA4NCAxNTAgMjg1IDI4MyA0NTkgMzA0IDk1IDEyIDEwMSAxMiAxODcgMHogbS0zMzYyIC0zNDAwCmMxMzMgLTI3IDE5NiAtNTcgMjg2IC0xMzQgMTU3IC0xMzQgMjMyIC0yOTEgMjMyIC00ODUgMSAtMjM5IC05MCAtNDEyIC0yODgKLTU1MSAtMzEgLTIyIC01OSAtMzkgLTYzIC0zOSAtNCAwIC0yNCAtOSAtNDUgLTIwIC02MCAtMzIgLTE4OCAtNTMgLTI5MiAtNDcKLTI1MiAxNSAtNDg0IDE4NyAtNTU1IDQxMiAtNyAyMiAtMTYgNDUgLTIwIDUwIC0xOCAyMiAtMzEgMTQxIC0yNSAyMTQgOSAxMDMKMjAgMTUwIDUwIDIxNSAxNCAzMCAyNSA1NyAyNSA2MCAwIDI0IDE1NyAyMDYgMTc4IDIwNiA0IDAgMTcgOCAyOCAxOCAzMSAyOQoxNjUgODkgMjI0IDEwMSA5NyAyMCAxNjkgMjAgMjY1IDB6Ii8+CjwvZz4KPC9zdmc+Cg==
    :target: https://github.com/ray-project/ray

|

**Ray is a flexible, high-performance distributed execution framework.**


Ray is easy to install: ``pip install ray``

Example Use
-----------

+------------------------------------------------+----------------------------------------------------+
| **Basic Python**                               | **Distributed with Ray**                           |
+------------------------------------------------+----------------------------------------------------+
|.. code-block:: python                          |.. code-block:: python                              |
|                                                |                                                    |
|  # Execute f serially.                         |  # Execute f in parallel.                          |
|                                                |                                                    |
|                                                |  @ray.remote                                       |
|  def f():                                      |  def f():                                          |
|      time.sleep(1)                             |      time.sleep(1)                                 |
|      return 1                                  |      return 1                                      |
|                                                |                                                    |
|                                                |                                                    |
|                                                |  ray.init()                                        |
|  results = [f() for i in range(4)]             |  results = ray.get([f.remote() for i in range(4)]) |
+------------------------------------------------+----------------------------------------------------+


Ray comes with libraries that accelerate deep learning and reinforcement learning development:

- `Tune`_: Hyperparameter Optimization Framework
- `RLlib`_: Scalable Reinforcement Learning
- `Distributed Training <http://ray.readthedocs.io/en/latest/distributed_sgd.html>`__

.. _`Tune`: http://ray.readthedocs.io/en/latest/tune.html
.. _`RLlib`: http://ray.readthedocs.io/en/latest/rllib.html

Installation
------------

Ray can be installed on Linux and Mac with ``pip install ray``.

To build Ray from source or to install the nightly versions, see the `installation documentation`_.

.. _`installation documentation`: http://ray.readthedocs.io/en/latest/installation.html

More Information
----------------

- `Documentation`_
- `Tutorial`_
- `Blog`_
- `Ray paper`_
- `Ray HotOS paper`_

.. _`Documentation`: http://ray.readthedocs.io/en/latest/index.html
.. _`Tutorial`: https://github.com/ray-project/tutorial
.. _`Blog`: https://ray-project.github.io/
.. _`Ray paper`: https://arxiv.org/abs/1712.05889
.. _`Ray HotOS paper`: https://arxiv.org/abs/1703.03924

Getting Involved
----------------

- `ray-dev@googlegroups.com`_: For discussions about development or any general
  questions.
- `StackOverflow`_: For questions about how to use Ray.
- `GitHub Issues`_: For reporting bugs and feature requests.
- `Pull Requests`_: For submitting code contributions.

.. _`ray-dev@googlegroups.com`: https://groups.google.com/forum/#!forum/ray-dev
.. _`GitHub Issues`: https://github.com/ray-project/ray/issues
.. _`StackOverflow`: https://stackoverflow.com/questions/tagged/ray
.. _`Pull Requests`: https://github.com/ray-project/ray/pulls
