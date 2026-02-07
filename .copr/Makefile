srpm:
	rpmbuild -bs $(spec) \
		--define "_sourcedir $(CURDIR)" \
		--define "_specdir $(CURDIR)" \
		--define "_builddir $(CURDIR)" \
		--define "_srcrpmdir $(outdir)" \
		--define "_rpmdir $(CURDIR)" \
		--define "dist .fc$(shell rpm --eval %{fedora})"
