# cd /etc/puppet/code/environments/production/modules/profile/manifests

class profile {
        file { '/etc/profile.d/append-path.sh':
                owner   => 'root',
                group   => 'root',
                mode    => '0646',
                content => "PATH=/java/bin\n",
        }
}
# After fixing the above class ;
# the new PATH value is PATH=\$PATH:/java/bin\n

class profile {
        file { '/etc/profile.d/append-path.sh':
                owner   => 'root',
                group   => 'root',
                mode    => '0646',
                content => "\$PATH:/java/bin\n",
        }
}

