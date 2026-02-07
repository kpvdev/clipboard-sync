srpm:
	mkdir -p $(outdir)
	cp *.sh *.service LICENSE README.md $(spec) $(outdir)/
	rpmbuild -bs $(spec) \
		--define "_sourcedir $(outdir)" \
		--define "_specdir $(outdir)" \
		--define "_builddir $(outdir)" \
		--define "_srcrpmdir $(outdir)" \
		--define "_rpmdir $(outdir)" \
		--define "dist .fc$(shell rpm --eval %{fedora})"
