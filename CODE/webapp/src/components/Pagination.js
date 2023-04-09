import React from 'react';
import classnames from 'classnames';
import '../styles/pagination.scss';
const Pagination = props => {
    const {
        onPageChange,
        currentPage,
        className
    } = props;

    const onNext = () => {
        onPageChange(currentPage + 1);
    };

    const onPrevious = () => {
        onPageChange(currentPage - 1);
    };

    return (
        <ul
            className={classnames('pagination-container', { [className]: className })}
        >
            <li
                className={classnames('pagination-item', {
                    disabled: currentPage === 1
                })}
                onClick={onPrevious}
            >
                <div className="arrow left" />
            </li>
            {/* {paginationRange.map((pageNumber, i) => {
                if (pageNumber === DOTS) {
                    return <li key={i} className="pagination-item dots">&#8230;</li>;
                }

                return (
                    <li key={i}
                        className={classnames('pagination-item', {
                            selected: pageNumber === currentPage
                        })}
                        onClick={() => onPageChange(pageNumber)}
                    >
                        {pageNumber}
                    </li>
                );
            })} */}

            <li
                className={classnames('pagination-item')}
                onClick={onNext}
            >
                <div className="arrow right" />
            </li>
        </ul>
    );
};

export default Pagination;
