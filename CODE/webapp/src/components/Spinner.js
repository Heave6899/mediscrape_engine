import React from 'react'
import classes from '../styles/spinner.module.scss';

function Spinner({ className }) {
    return (
        <div className={classes.loader}>
            <i className={classes.loaderel}></i>
            <i className={classes.loaderel}></i>
        </div>
    )
}

export default Spinner