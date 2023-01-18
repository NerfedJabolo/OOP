# import pytest

# import clients_solution
# import clients

# basic_file = "test_files/basic_test.txt"
# empty_file = "test_files/empty_test.txt"
# negative_file = "test_files/negative_test.txt"
# positive_file = "test_files/positive_test.txt"
# equal_file = "test_files/equal_test.txt"
# zero_file = "test_files/zero_test.txt"


# @pytest.mark.timeout(1.0)
# def test_reading_from_file_into_list_empty_works():
#     """Testing if correct info is read and made into objects."""
#     assert clients.read_from_file_into_list(empty_file) == clients_solution.read_from_file_into_list(empty_file)


# @pytest.mark.timeout(1.0)
# def test_reading_from_file_into_list_basic_works():
#     """Testing if correct info is read and made into objects."""
#     assert clients.read_from_file_into_list(basic_file) == clients_solution.read_from_file_into_list(basic_file)


# @pytest.mark.timeout(1.0)
# def test_reading_from_file_into_list_negative_works():
#     """Testing if correct info is read and made into objects."""
#     assert clients.read_from_file_into_list(negative_file) == clients_solution.read_from_file_into_list(negative_file)


# @pytest.mark.timeout(1.0)
# def test_filter_by_bank_sprint():
#     """Testing filter by bank Sprint."""
#     # Should have [Ann, Mark].
#     assert clients.filter_by_bank(basic_file, "Sprint") == clients_solution.filter_by_bank(basic_file, "Sprint")


# @pytest.mark.timeout(1.0)
# def test_filter_by_bank_chase():
#     """Testing filter by bank Chase."""
#     # Should have [Josh].
#     assert clients.filter_by_bank(basic_file, "Chase") == clients_solution.filter_by_bank(basic_file, "Chase")


# @pytest.mark.timeout(1.0)
# def test_filter_by_nonexistent_bank():
#     """Testing filter by bank LHV."""
#     # Should have [].
#     assert clients.filter_by_bank(basic_file, "LHV") == clients_solution.filter_by_bank(basic_file, "LHV")


# @pytest.mark.timeout(1.0)
# @pytest.mark.dependency()
# def test_largest_earnings_per_day_basic_works_correctly():
#     """Testing if it gets correct largest earning client."""
#     # Should be Joseph
#     assert clients.largest_earnings_per_day(basic_file) == clients_solution.largest_earnings_per_day(basic_file)


# @pytest.mark.timeout(1.0)
# @pytest.mark.dependency(depends=["test_largest_earnings_per_day_basic_works_correctly"])
# def test_largest_earnings_per_day_equal_people_gets_with_less_time():
#     """Testing if it gets correct largest earning client when they have equal earnings per day."""
#     # Should be Josh
#     assert clients.largest_earnings_per_day(equal_file) == clients_solution.largest_earnings_per_day(equal_file)


# @pytest.mark.timeout(1.0)
# @pytest.mark.dependency(depends=["test_largest_earnings_per_day_basic_works_correctly"])
# def test_largest_earnings_per_day_none():
#     """Testing if it gets correct largest earning client."""
#     # Should be None
#     assert clients.largest_earnings_per_day(negative_file) == clients_solution.largest_earnings_per_day(negative_file)


# @pytest.mark.timeout(1.0)
# @pytest.mark.dependency(depends=["test_largest_earnings_per_day_basic_works_correctly"])
# def test_largest_earnings_per_day_earned_zero():
#     """Testing if it gets correct largest earning client."""
#     # Should be None
#     assert clients.largest_earnings_per_day(zero_file) == clients_solution.largest_earnings_per_day(zero_file)


# @pytest.mark.timeout(1.0)
# @pytest.mark.dependency()
# def test_largest_loss_per_day_basic_works_correctly():
#     """Testing if it gets correct largest losing client."""
#     # Should be Franz
#     assert clients.largest_loss_per_day(basic_file) == clients_solution.largest_loss_per_day(basic_file)


# @pytest.mark.timeout(1.0)
# @pytest.mark.dependency(depends=["test_largest_loss_per_day_basic_works_correctly"])
# def test_largest_loss_per_day_equal_people_gets_with_less_time():
#     """Testing if it gets correct largest losing client when they have equal earnings per day."""
#     # Should be Duke
#     assert clients.largest_loss_per_day(equal_file) == clients_solution.largest_loss_per_day(equal_file)


# @pytest.mark.timeout(1.0)
# @pytest.mark.dependency(depends=["test_largest_loss_per_day_basic_works_correctly"])
# def test_largest_loss_per_day_none():
#     """Testing if it gets correct largest losing client."""
#     # Should be None
#     assert clients.largest_loss_per_day(positive_file) == clients_solution.largest_loss_per_day(positive_file)


# @pytest.mark.timeout(1.0)
# @pytest.mark.dependency(depends=["test_largest_loss_per_day_basic_works_correctly"])
# def test_largest_loss_per_day_earned_zero():
#     """Testing if it gets correct largest losing client."""
#     # Should be None
#     assert clients.largest_loss_per_day(zero_file) == clients_solution.largest_loss_per_day(zero_file)
