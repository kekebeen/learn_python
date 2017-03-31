'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');
var browserSync = require ('browser-sync').create();

gulp.task('sass', function () {
   return gulp.src('./sass/app.scss')
       .pipe(sass().on('error', sass.logError ))
       .pipe(gulp.dest('./css/'))
       .pipe(browserSync.stream());
});

gulp.task('browser-sync', function() {
    browserSync.init({
        server: {
            baseDir: "./"
        }
    });
});

gulp.task('serve',['sass'], function () {
    browserSync.init({
        server: {
            baseDir: "./"
        }
    });

    gulp.watch('./sass/**/*.scss', ['sass']);
    gulp.watch('./*.html').on('change', browserSync.reload);
});


gulp.task('default', ['serve']);
