program feigenbaum_program
    implicit none
    integer, parameter :: dp = kind(1.0d0)   ! Double precision
    integer :: range_i, range_j, i, j, k
    real(dp) :: f, p, dp_val
    real(dp), dimension(3) :: mu

    ! Call the subroutine to print the Feigenbaum table
    call feigenbaum_table()

contains

    ! Function to calculate the Feigenbaum constant
    function feigenbaum(range_i, range_j, f) result(f_value)
        integer, intent(in) :: range_i, range_j
        real(dp), intent(in) :: f
        real(dp) :: f_value
        real(dp), dimension(3) :: mu
        real(dp) :: p, dp_val
        integer :: i, j, k

        ! Initialize mu values
        mu(1) = 0.0_dp
        mu(2) = 1.0_dp
        mu(3) = 0.0_dp
        f_value = f  ! Set initial f value

        ! Main iteration loop
        do i = 2, range_i
            mu(3) = mu(2) + (mu(2) - mu(1)) / f_value

            do j = 1, range_j
                p = 0.0_dp
                dp_val = 0.0_dp
                do k = 1, 2**i
                    dp_val = 1.0_dp - 2.0_dp * dp_val * p
                    p = mu(3) - p**2
                end do
                mu(3) = mu(3) - p / dp_val
            end do

            f_value = (mu(2) - mu(1)) / (mu(3) - mu(2))
            mu(1) = mu(2)
            mu(2) = mu(3)
        end do
    end function feigenbaum

    ! Subroutine to print the Feigenbaum table
    subroutine feigenbaum_table()
        integer :: i
        real(dp) :: f_value
        write(*,'(A)') "range_i          f"
        write(*,'(A)') "--------------------------------------"
        do i = 1, 15
            f_value = feigenbaum(i, 100, 3.2_dp)
            write(*,'(I4, A, F22.15)') i, " ", f_value
        end do
    end subroutine feigenbaum_table

end program feigenbaum_program
