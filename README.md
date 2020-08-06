# Ansible Role: systemd-timesyncd

An Ansible role that manages [systemd-timesyncd](https://www.freedesktop.org/software/systemd/man/systemd-timesyncd.service.html) on Raspberry Pi OS and Debian based systems.

## Install

```
$ ansible-galaxy install escalate.systemd-timesyncd
```

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-systemd-timesyncd/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Example Playbook

```
- hosts: all
  roles:
    - escalate.systemd-timesyncd
```

## Dependencies

None

## License

MIT
