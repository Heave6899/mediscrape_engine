import React from 'react'
// import '../styles/red-spinner.scss';
import classes from '../styles/red-spinner.module.scss';
function RedSpinner({ className }) {
    return (
        <div className={classes.loader}>
            <i className={`${classes.loaderel}`}></i>
            <i className={`${classes.loaderel}`}></i>
        </div>
    )
}

export default RedSpinner;