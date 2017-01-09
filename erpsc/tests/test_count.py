"""Tests for the Count() class and related functions from erpsc."""

from erpsc.count import Count

#######################################################################################
################################ TESTS - ERPSC - COUNT ################################
#######################################################################################

def test_erpsc_count():
    """Test the ERPSCCount object."""

    # Check that ERPSCCount returns properly
    assert Count()

def test_scrape():
    """Test that Count object successful scrapes data."""

    counts = Count()

    # Add ERPs and terms
    counts.set_erps(['N400', 'P600'])
    counts.set_terms(['language', 'memory'])

    counts.scrape_data(db='pubmed')

    assert counts.dat_numbers
    assert counts.dat_percent

    check_funcs(counts)

def check_funcs(counts):
    """Given object with scraped data, test all the check functions."""

    # Check that all check functions run
    counts.check_cooc_erps()
    counts.check_cooc_terms()
    counts.check_top()
    counts.check_counts('erp')
    counts.check_counts('term')

    assert True
