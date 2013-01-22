##########################################################################
#  
#  Copyright (c) 2012, John Haddon. All rights reserved.
#  Copyright (c) 2013, Image Engine Design Inc. All rights reserved.
#  
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#  
#      * Redistributions of source code must retain the above
#        copyright notice, this list of conditions and the following
#        disclaimer.
#  
#      * Redistributions in binary form must reproduce the above
#        copyright notice, this list of conditions and the following
#        disclaimer in the documentation and/or other materials provided with
#        the distribution.
#  
#      * Neither the name of John Haddon nor the names of
#        any other contributors to this software may be used to endorse or
#        promote products derived from this software without specific prior
#        written permission.
#  
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
#  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#  
##########################################################################

import IECore

import Gaffer

class BadNode( Gaffer.DependencyNode ) :
		
	def __init__( self, name="BadNode" ) :

		Gaffer.DependencyNode.__init__( self, name )

		self.addChild( Gaffer.IntPlug( "in1", Gaffer.Plug.Direction.In ) )
		self.addChild( Gaffer.IntPlug( "in2", Gaffer.Plug.Direction.In ) )

		self.addChild( Gaffer.IntPlug( "out1", Gaffer.Plug.Direction.Out ) )
		self.addChild( Gaffer.IntPlug( "out2", Gaffer.Plug.Direction.Out ) )
		self.addChild( Gaffer.IntPlug( "out3", Gaffer.Plug.Direction.Out ) )
		
	def affects( self, input ) :
		
		outputs = []
		if input.getName() == "in1" :
			outputs.append( self["out1"] )
		elif input.getName() == "in1" :
			outputs.append( self["out2"] )
			
		return outputs

	def compute( self, plug, context ) :

		if plug.isSame( self["out1"] ) :
			# good - pull on the right input and set the right plug
			plug.setValue( self["in1"].getValue() )
			# bad - try to set another plug at the same time
			self["out2"].setValue( 10 )
		elif plug.isSame( self["out2"] ) :
			# bad - pull on the wrong plug
			plug.setValue( self["in1"].getValue() )
		elif plug.isSame( self["out3"] ) :
			# bad - don't do anything
			pass
			
		
IECore.registerRunTimeTyped( BadNode )
