var startX,//触摸时的坐标
            startY,
             x, //滑动的距离
             y,
             aboveY=0; //设一个全局变量记录上一次内部块滑动的位置

         var inner=document.getElementById("inner");

            function touchSatrt(e){//触摸
                e.preventDefault();
                var touch=e.touches[0];
                startY = touch.pageY;   //刚触摸时的坐标
            }

            function touchMove(e){//滑动
                 e.preventDefault();
                 var  touch = e.touches[0];
                 y = touch.pageY - startY;//滑动的距离
                //inner.style.webkitTransform = 'translate(' + 0+ 'px, ' + y + 'px)';  //也可以用css3的方式
                inner.style.top=aboveY+y+"px"; //这一句中的aboveY是inner上次滑动后的位置
            }

            function touchEnd(e){//手指离开屏幕
              e.preventDefault();
              aboveY=parseInt(inner.style.top);//touch结束后记录内部滑块滑动的位置 在全局变量中体现 一定要用parseInt()将其转化为整数字;

            }//
             document.getElementById("outer").addEventListener('touchstart', touchSatrt,false);
             document.getElementById("outer").addEventListener('touchmove', touchMove,false);
             document.getElementById("outer").addEventListener('touchend', touchEnd,false);