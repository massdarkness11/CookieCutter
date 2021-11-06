cutterHeight = 25;
brimHeight = 2;
brimTranslate = 0.55;
handleHeight = 4;
handleRadius = 10;
innerPlatformHeight = 2.5;
detailHeight = 5;
stem = cutterHeight - handleHeight - innerPlatformHeight - detailHeight;
stemRadius = 3;
module shadow()
{
    offset(0.01)import("bulbasaur shadow.svg", center = true, dpi = 96);
}
module stencil()
{
    offset(0.01)import("bulbasaur stencil.svg", center = true, dpi = 96);
}
module model_insides()
{
    details();
    innerPlatform();
    handle();
    stem();
}
module details()
{
    difference()
    {
        translate ([0,0,handleHeight + stem + innerPlatformHeight + detailHeight/2])linear_extrude(height = detailHeight, center = true)
        stencil();
        
        //notouch();
    }
}
module innerPlatform()
{
    difference()
    {
        translate ([0,0,handleHeight + stem + innerPlatformHeight/2])linear_extrude(height = innerPlatformHeight, center = true)
        shadow();
        
        //notouch();
    }
}

module handle()
{
    translate ([0,0,handleHeight/2])linear_extrude(height = handleHeight, center = true, convexity = 10)
    circle(r = handleRadius);
    
}

module stem()//connects handle to base
{
    translate([0,0,handleHeight -0.125])
    rotate_extrude()
        mirror([1,-1,0])
        translate([0,0,0])
        rotate([180,0,0])  
        difference()
        {
            //square that is the stem
            square(size = stem+0.25);
            //circle that forms stem
            translate ([0, stem*2 + stemRadius, 0])     
            circle(r = stem*2, $fn = 100);   
        } 
    
}


module outer()
{
    translate ([0,0,cutterHeight/2])linear_extrude(height = cutterHeight, center = true)
    {
        difference()
        {
            offset(r = 1.6)shadow();
            offset(r = 0.6)shadow();
        }
    }
}
module cutter()
{
    outer();
    feet();
    
}

module feet()
{
    translate ([0,0,brimTranslate])linear_extrude(height = brimHeight, center = true)
    difference()
    {
    offset(r = 3.1) shadow();
    offset(r = 0.5) shadow();
    }
}

module notouch()
{
    translate ([0,0,(cutterHeight + 5)/2-1])linear_extrude(height = cutterHeight+5, center = true)
    difference(){
    offset(0.1)shadow();
    offset(-0.1)shadow();
    }
}

//notouch2();
module OuterCutter()
{
    difference(){
    cutter();
       //notouch();
    }
}

module makecutter(){
    minkowski(){
        linear_extrude(0.01)
        difference(){
            children();

            offset(-0.01)
            children();
        }

        union(){ //Cutting edge shape here
            cylinder(h=20,d1=0.01,d2=3);

            translate([0,0,19.9])
            cylinder(h=3,d=15);
        }
    }
}





//notouch();
model_insides();
OuterCutter();
