srpm:
	dnf install -y git
	git archive --format=tar.gz --prefix=clipboard-sync-1.1.0/ HEAD > $(outdir)/clipboard-sync-1.1.0.tar.gz
	rpmbuild -bs $(spec) \
		--define "_sourcedir $(outdir)" \
		--define "_specdir $(outdir)" \
		--define "_builddir $(outdir)" \
		--define "_srcrpmdir $(outdir)" \
		--define "_rpmdir $(outdir)" \
		--define "dist .fc$(shell rpm --eval %{fedora})"
